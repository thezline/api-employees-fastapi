from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class EmpleadoCreate(BaseModel):
    nombre: str
    salario: float = Field(..., gt=0)
    fecha_ingreso: date
    vacaciones_disponibles: int = Field(..., ge=0)


class EmpleadoOut(BaseModel):
    id: int
    nombre: str
    salario: float
    fecha_ingreso: date
    vacaciones_disponibles: int

    class Config:
        from_attributes = True