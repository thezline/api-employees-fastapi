from datetime import date
from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException
from schemas.empleado import EmpleadoOut
from services.empleado_service import EmpleadoService


router = APIRouter(prefix="/empleados", tags=["empleados"])

service = EmpleadoService()


@router.get("/", response_model=List[EmpleadoOut])
async def obtener_todos_empleados():
    """Devuelve todos los empleados"""
    return service.get_all()


@router.get("/buscar/", response_model=List[EmpleadoOut])
async def buscar_por_nombre(nombre: str = Query(..., min_length=2)):
    """Busca empleados por nombre (parcial, no sensible a mayúsculas)"""
    resultados = service.get_by_nombre(nombre)
    if not resultados:
        raise HTTPException(404, detail="No se encontraron empleados con ese nombre")
    return resultados


@router.get("/por-fecha-ingreso/", response_model=List[EmpleadoOut])
async def filtrar_por_fecha_ingreso(
    desde: Optional[date] = Query(None, description="Fecha desde (YYYY-MM-DD)"),
    hasta: Optional[date] = Query(None, description="Fecha hasta (YYYY-MM-DD)")
):
    """Filtra empleados por rango de fecha de ingreso"""
    if desde and hasta and desde > hasta:
        raise HTTPException(400, detail="La fecha 'desde' no puede ser mayor a 'hasta'")
    return service.filter_by_fecha_ingreso(desde, hasta)


@router.get("/por-vacaciones/", response_model=List[EmpleadoOut])
async def filtrar_por_vacaciones(
    minimo: Optional[int] = Query(None, ge=0, description="Mínimo de vacaciones"),
    exacto: Optional[int] = Query(None, ge=0, description="Vacaciones exactas")
):
    """Filtra por cantidad de vacaciones (mínimo o exacto)"""
    if minimo is not None and exacto is not None:
        raise HTTPException(400, detail="Enviar solo 'minimo' o 'exacto', no ambos")
    return service.filter_by_vacaciones(min_vacaciones=minimo, exact_vacaciones=exacto)


@router.get("/por-salario/", response_model=List[EmpleadoOut])
async def filtrar_por_salario(
    minimo: Optional[float] = Query(None, ge=0, description="Salario mínimo"),
    exacto: Optional[float] = Query(None, ge=0, description="Salario exacto")
):
    """Filtra por salario (mínimo o exacto)"""
    if minimo is not None and exacto is not None:
        raise HTTPException(400, detail="Enviar solo 'minimo' o 'exacto', no ambos")
    return service.filter_by_salario(min_salario=minimo, salario_exacto=exacto)