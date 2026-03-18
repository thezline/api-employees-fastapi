import json
from datetime import date
from typing import List, Optional
from fastapi import HTTPException
from models.empleado import Empleado


class EmpleadoService:
    def __init__(self):
        self.file_path = "data/empleados.json"
        self.empleados: List[Empleado] = self._cargar_empleados()

    def _cargar_empleados(self) -> List[Empleado]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Empleado(**emp) for emp in data]
        except FileNotFoundError:
            return []
        except Exception as e:
            raise Exception(f"Error al leer empleados: {e}")

    def _guardar_empleados(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([emp.model_dump() for emp in self.empleados], f, indent=2, default=str)

    def get_all(self) -> List[Empleado]:
        return self.empleados

    def get_by_nombre(self, nombre: str) -> List[Empleado]:
        nombre = nombre.lower()
        return [e for e in self.empleados if nombre in e.nombre.lower()]

    def filter_by_fecha_ingreso(self, desde: Optional[date] = None, hasta: Optional[date] = None):
        result = self.empleados
        if desde:
            result = [e for e in result if e.fecha_ingreso >= desde]
        if hasta:
            result = [e for e in result if e.fecha_ingreso <= hasta]
        return result

    def filter_by_vacaciones(self, min_vacaciones: Optional[int] = None, exact_vacaciones: Optional[int] = None):
        result = self.empleados
        if min_vacaciones is not None:
            result = [e for e in result if e.vacaciones_disponibles >= min_vacaciones]
        if exact_vacaciones is not None:
            result = [e for e in result if e.vacaciones_disponibles == exact_vacaciones]
        return result

    def filter_by_salario(self, min_salario: Optional[float] = None, salario_exacto: Optional[float] = None):
        result = self.empleados
        if min_salario is not None:
            result = [e for e in result if e.salario >= min_salario]
        if salario_exacto is not None:
            result = [e for e in result if e.salario == salario_exacto]
        return result