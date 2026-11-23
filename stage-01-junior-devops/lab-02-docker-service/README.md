# Lab 02: Docker Service & CI

A lightweight Flask HTTP service containerized with Docker and verified on every push and pull request to `main` using GitHub Actions.

## Endpoints

- `GET /` — Returns JSON with `service`, `environment` (`APP_ENV`, defaults to `development`), and container `hostname`.
- `GET /health` — Returns `{"status": "ok"}` with HTTP `200`.

## Project Structure

- `.github/workflows/ci.yml` — GitHub Actions CI workflow
- `app/app.py` — Flask application
- `app/requirements.txt` — Python dependencies
- `.dockerignore` — Files excluded from Docker build context
- `docker-compose.yml` — Local Compose service definition
- `Dockerfile` — Container image build and healthcheck definition

## Local Usage

Docker Compose:
`docker compose up --build`

Docker CLI:
`docker build -t lab-02-docker-service:local .`
`docker run -d --name lab-02-web -p 8080:8080 -e APP_ENV=local lab-02-docker-service:local`
`curl -s http://localhost:8080/health`
`curl -s http://localhost:8080/`
`docker rm -f lab-02-web`

## CI Pipeline

`.github/workflows/ci.yml` runs on `push` and `pull_request` events targeting `main`:
1. Checks out the repository.
2. Builds the Docker image (`lab-02-docker-service:ci`).
3. Starts the container, runs smoke checks against `/health` and `/`, and cleans up the test container.
