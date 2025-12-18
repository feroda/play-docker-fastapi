Project: play-docker-fastapi

This repository contains a mini application designed for deployment with Docker Compose, built using FastAPI.

Services:
- **FastAPI Application (api)**: A Python application built with FastAPI that exposes a `/api/` endpoint. This endpoint increments a hit counter stored in Redis and returns a "Hello from FastAPI" message along with the current hit count.
- **NGINX (nginx)**: Acts as a reverse proxy, serving static files from the `static/` directory and forwarding API requests to the FastAPI application. It listens on port `20001` of the host machine.
- **Redis (redis)**: A Redis instance used by the FastAPI application to store and retrieve the hit counter.

Networking:
All services are connected via a Docker network named `appnet`.

Deployment:
The entire application stack can be deployed using Docker Compose. The `compose.yml` file orchestrates the three services.

