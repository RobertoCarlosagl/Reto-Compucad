from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime, timedelta
from app.models.solicitud import Solicitud
from app.schemas.solicitud import SolicitudCreate
from fastapi import HTTPException
from app.utils.folio import generar_folio

# ----- ANALIZAR PALABRAS CLAVE PARA CLASIFICACIÓN -----

def asignar_prioridad(descripcion: str) -> str:
    descripcion = descripcion.lower()
    if "urgente" in descripcion or "auditoría" in descripcion:
        return "Alta"
    elif "cumplimiento" in descripcion or "normatividad" in descripcion:
        return "Media"
    else:
        return "Baja"

# ----- CRUD SOLICITUDES -----

def crear_solicitud(db: Session, datos: SolicitudCreate):
    prioridad = asignar_prioridad(datos.descripcion)
    folio = generar_folio(db)

    nueva = Solicitud(
        descripcion=datos.descripcion,
        tipo_area=datos.tipo_area,
        responsable=datos.responsable,
        fecha_estimacion=datos.fecha_estimacion,
        folio=folio,
        prioridad=prioridad
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_solicitudes(db: Session):
    return db.query(Solicitud).all()

def obtener_solicitud_por_id(db: Session, solicitud_id: UUID):
    return db.query(Solicitud).filter(Solicitud.id == solicitud_id).first()

def finalizar_solicitud(db: Session, solicitud_id: str):
    solicitud = db.query(Solicitud).filter(Solicitud.id == solicitud_id).first()
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if not solicitud.aprobado_por:
        raise HTTPException(status_code=400, detail="No se puede finalizar una solicitud no aprobada")
    solicitud.estatus = "Finalizada"
    db.commit()
    db.refresh(solicitud)
    return solicitud

def verificar_solicitudes_pendientes(db: Session):
    solicitudes = db.query(Solicitud).filter(Solicitud.estatus == "Pendiente").all()
    actualizados = []
    for solicitud in solicitudes:
        if datetime.utcnow() - solicitud.fecha_creacion > timedelta(days=3):
            solicitud.estatus = "Pendiente Evaluación"
            actualizados.append(solicitud.folio)
    db.commit()
    return actualizados
