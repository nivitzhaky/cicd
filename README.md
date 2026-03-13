# basic-docker-kubernetes

A minimal FastAPI todo API backed by Postgres, with Alembic migrations and Docker Compose.

## Quick start

```sh
docker compose up --build
docker ps
docker logs -f <container_id>
docker exec -it <container_id> bash
docker compose down
## or instead docker kill <container_id>
```

## Alembic commands

```sh
alembic init alembic

alembic revision --autogenerate -m "describe change"

alembic revision -m "describe change"

alembic upgrade head
```


The API will be available at http://localhost:8000.

## API endpoints

- `GET /healthz`
- `GET /todos`
- `POST /todos` (body: `{ "title": "..." }`)
- `GET /todos/{id}`
- `PATCH /todos/{id}` (body: `{ "title": "...", "is_done": true }`)
- `DELETE /todos/{id}`


```sh
# Build image locally
docker build -t todo-api:latest .
```

