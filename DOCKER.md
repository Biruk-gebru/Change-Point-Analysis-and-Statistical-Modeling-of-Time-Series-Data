# Docker Deployment Guide

## Quick Start

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Services

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## Architecture

```
Frontend (React + Nginx) → Backend (Flask) → Data Files
     Port 3000                  Port 5000
```

## Individual Service Commands

```bash
# Build specific service
docker-compose build backend
docker-compose build frontend

# Start specific service
docker-compose up backend
docker-compose up frontend

# Rebuild and restart
docker-compose up --build
```

## Troubleshooting

- Ensure ports 3000 and 5000 are available
- Check logs: `docker-compose logs <service-name>`
- Rebuild images if code changes: `docker-compose up --build`
