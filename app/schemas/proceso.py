from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

# ---------- INPUT ----------
class ProcesoCreate(BaseModel):
    nombre: str
    descripcion: str
    id_solicitud: UUID

# ---------- OUTPUT ----------
class ProcesoOut(BaseModel):
    id: UUID
    nombre: str
    descripcion: str
    id_solicitud: UUID
    fecha_registro: datetime

    class Config:
        orm_mode = True
