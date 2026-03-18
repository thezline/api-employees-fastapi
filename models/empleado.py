from datetime import date
from pydantic import BaseModel, Field


class Empleado(BaseModel):
    id: int = Field(..., gt=0)
    nombre: str
    salario: float = Field(..., gt=0)
    fecha_ingreso: date
    vacaciones_disponibles: int = Field(..., ge=0)