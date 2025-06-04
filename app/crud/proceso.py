from sqlalchemy.orm import Session
from uuid import UUID
from app.models.proceso import Proceso
from app.schemas.proceso import ProcesoCreate
from fastapi import HTTPException

def crear_proceso(db: Session, datos: ProcesoCreate) -> Proceso:
    nuevo = Proceso(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
        id_solicitud=datos.id_solicitud
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_procesos(db: Session):
    return db.query(Proceso).all()

def obtener_proceso_por_id(db: Session, proceso_id: UUID):
    proceso = db.query(Proceso).filter(Proceso.id == proceso_id).first()
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return proceso

def eliminar_proceso(db: Session, proceso_id: UUID):
    proceso = db.query(Proceso).filter(Proceso.id == proceso_id).first()
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    db.delete(proceso)
    db.commit()
    return {"mensaje": "Proceso eliminado correctamente"}
