# SenaWFM

Workforce Management System SaaS application.

## Running the Backend

Ensure Docker is running to host the PostgreSQL database.

```bash
docker compose up -d
cd backend
source .venv/bin/activate
uvicorn src.main:app --reload --port 8000
```

## Running the Frontend

```bash
cd frontend
npm run dev
```

You can then visit `http://localhost:3000` to see the landing page, and `http://localhost:3000/health` to verify connectivity with the backend.
