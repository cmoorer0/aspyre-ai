from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router

# create the FastAPI app instance
app = FastAPI()

# frontend will run on http://localhost:3000 during development
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# CORS setup: allows the frontend to call the backend in the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # which domains are allowed
    allow_credentials=True,
    allow_methods=["*"],          # which HTTP methods are allowed (GET, POST, etc.)
    allow_headers=["*"],          # which headers are allowed
)

# Simple health-check endpoint
@app.get("/health")
def health_check():
    return{"status": "ok", "service": "aspyre-backend"}

app.include_router(auth_router)

