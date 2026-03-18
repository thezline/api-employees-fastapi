from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import empleados

app = FastAPI(
    title="API Empleados - FastAPI",
    description="API básica de gestión de empleados (JSON)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        ".vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(empleados.router)

@app.get("/")
async def root():
    return {"message": "API de Empleados - ve a /docs"}