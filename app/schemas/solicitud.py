from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class SolicitudBase(BaseModel):
    descripcion: str
    tipo_area: str
    responsable: str
    fecha_estimacion: Optional[datetime] = None
    estatus: Optional[str] = "Pendiente"
    folio: Optional[str] = None 
    retroalimentacion: Optional[str] = None
    aprobado_por: Optional[str] = None
    fecha_aprobacion: Optional[datetime] = None
    prioridad: Optional[str] = "Baja"
    
class SolicitudCreate(SolicitudBase):
    fecha_creacion: Optional[datetime] = None  # <- AGREGA ESTA LÍNEA

class SolicitudOut(SolicitudBase):
    id: UUID
    fecha_creacion: datetime
    prioridad: str
    class Config:
        orm_mode = True
        

