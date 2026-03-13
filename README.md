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

## Create EC2 Intance
download PEM and save as repository secrect

### install docker and git
```sh
sudo yum update -y
sudo yum install -y docker git
sudo service docker start
sudo usermod -aG docker ec2-user

sudo mkdir -p /usr/local/lib/docker/cli-plugins

sudo curl -SL https://github.com/docker/compose/releases/download/v5.1.0/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
docker compose version

sudo curl -SL https://github.com/docker/buildx/releases/download/v0.32.1/buildx-v0.32.1.linux-amd64 -o /usr/local/lib/docker/cli-plugins/docker-buildx
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-buildx
docker buildx version
```

### clone YOUR repo
```sh
sudo git clone https://github.com/nivitzhaky/cicd.git
```

### add inbound rule 
TCP port 8000  mask 0.0.0.0/0

```sh
cd cicd\
sudo docker compose up -d
```
### test
test machineip:8080

### change H1 title 
commit and push and test again


