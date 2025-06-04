import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class Solicitud(Base):
    __tablename__ = "solicitudes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    descripcion = Column(Text, nullable=False)
    tipo_area = Column(String(50), nullable=False)
    responsable = Column(String(150), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_estimacion = Column(DateTime, nullable=True)
    estatus = Column(String(50), default="Pendiente")
    folio = Column(String(50), unique=True, nullable=False)
    fecha_aprobacion = Column(DateTime, nullable=True)
    retroalimentacion = Column(Text, nullable=True)
    aprobado_por = Column(String(150), nullable=True)
    prioridad = Column(String, default="Baja")


