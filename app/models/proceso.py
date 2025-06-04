import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class Proceso(Base):
    __tablename__ = "procesos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    id_solicitud = Column(UUID(as_uuid=True), ForeignKey("solicitudes.id"), nullable=False)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
