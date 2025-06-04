from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid
from datetime import datetime

class Proceso(Base):
    __tablename__ = "procesos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String, nullable=False)
    id_solicitud = Column(UUID(as_uuid=True), ForeignKey("solicitudes.id"), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    solicitud = relationship("Solicitud", back_populates="procesos")
