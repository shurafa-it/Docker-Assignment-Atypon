# Microservices App with Docker

A Python-based microservices application containerized with Docker and orchestrated using Docker Compose.

## Architecture

The application consists of 4 services connected via a custom Docker network:

- **authentication-service** (port 5001) — Handles user authentication
- **enter-data-service** (port 5000) — Accepts data input after authentication, stores in MySQL
- **analytics-service** (port 5002) — Reads data from MySQL, analyzes it, stores results in MongoDB
- **show-results-service** (port 5003) — Retrieves analytics results from MongoDB after authentication

## Databases
- **MySQL** — Stores raw records
- **MongoDB** — Stores analytics results

## Tech Stack
- Python (Flask)
- Docker & Docker Compose
- MySQL
- MongoDB

## How to Run
```bash
git clone https://github.com/shurafa-it/Docker-Assignment-Atypon.git
cd Docker-Assignment-Atypon
docker-compose up --build
```

## Services & Endpoints

| Service | Port | Endpoint | Method |
|---|---|---|---|
| enter-data | 5000 | /enter | POST |
| authentication | 5001 | /auth | POST |
| analytics | 5002 | /analyze | GET |
| show-results | 5003 | /results | GET |

## Demo
[Watch the project walkthrough on YouTube](https://youtu.be/IREPK8Xci4Q)
