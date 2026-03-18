from fastapi import FastAPI
from routers import empleados

app = FastAPI(
    title="API Empleados - FastAPI",
    description="API básica de gestión de empleados (JSON)",
    version="1.0.0"
)

app.include_router(empleados.router)


@app.get("/")
async def root():
    return {"message": "API de Empleados - ve a /docs"}