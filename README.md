
## Spy Cat Agency

### Running with Docker

### Prerequisites
- Docker and Docker Compose installed 
- Provide the necessary variables for PostgresSQL (see .env.sample)

### Steps
```bash
# Build and start
docker-compose up --build

# Or run in background
docker-compose up -d

# Stop
docker-compose down
```

Access the application at:
- **API**: http://localhost:8080
- **Docs**: http://localhost:8080/docs