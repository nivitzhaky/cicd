from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .db import get_db
from .models import Todo
from .schemas import TodoCreate, TodoRead, TodoUpdate

app = FastAPI(title="Todo API")

templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/todos", response_model=list[TodoRead])
def list_todos(db: Session = Depends(get_db)):
    return db.query(Todo).order_by(Todo.id).all()


@app.post("/todos", response_model=TodoRead, status_code=201)
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(title=payload.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.patch("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    if payload.title is not None:
        todo.title = payload.title
    if payload.is_done is not None:
        todo.is_done = payload.is_done

    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return Response(status_code=204)

