---
dg-publish: true
---
# Docker

## Dockerfile - Buildtime

-   Contains commands a user could call to assemble an image

```python
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

-   `FROM` creates a layer from the `ubuntu:18.04` Docker image.
-   `COPY` adds files from your Docker client’s current directory.
-   `RUN` builds your application with `make`.
-   `CMD` specifies what command to run within the container.
-   `docker build -t python-imagename .`
-   `docker run python-imagename`

## Docker Compose - Runtime

docker-compose.yml

-   Startup multiple containers at same time and connect them
-   `docker compose up -d`
    -   -d (detached) runs services in the background
-   `docker compose stop`
-   `docker compose ps`
    -   To see what’s running

When you issue a `docker build`command, the current working directory is called the _build context_

## Postgres

`docker run -p 5432:5432 --name container-postgresdb -e POSTGRES_PASSWORD=admin -d postgres`