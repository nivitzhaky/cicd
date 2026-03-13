import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_ui.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_index_returns_html(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_index_contains_todo_form(client):
    response = client.get("/")
    body = response.text
    assert "addForm" in body
    assert "titleInput" in body


def test_index_contains_filter_buttons(client):
    response = client.get("/")
    body = response.text
    assert 'data-filter="all"' in body
    assert 'data-filter="active"' in body
    assert 'data-filter="done"' in body


def test_index_references_api_endpoint(client):
    response = client.get("/")
    assert "/todos" in response.text


def test_index_not_in_openapi_schema(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    paths = response.json()["paths"]
    assert "/" not in paths
