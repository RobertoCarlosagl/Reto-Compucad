from sqlalchemy.orm import Session
from app.models.solicitud import Solicitud
from app.schemas.solicitud import SolicitudCreate
import uuid
from datetime import datetime
from app.utils.folio import generar_folio

def crear_solicitud(db: Session, datos: SolicitudCreate):
    ultima = db.query(Solicitud).order_by(Solicitud.fecha_creacion.desc()).first()

    if ultima and ultima.folio.startswith("CCADPRC-"):
        ultimo_numero = int(ultima.folio.split("-")[-1])
    else:
        ultimo_numero = 0

    nuevo_folio = generar_folio(ultimo_numero)

    # 🧠 Clasificación automática de prioridad
    descripcion = datos.descripcion.lower()
    if any(palabra in descripcion for palabra in ["urgente", "emergencia", "inmediato"]):
        prioridad = "Alta"
    elif any(palabra in descripcion for palabra in ["cumplimiento", "auditoría", "auditoria"]):
        prioridad = "Media"
    else:
        prioridad = "Baja"

    nueva = Solicitud(
        id=uuid.uuid4(),
        tipo_area=datos.tipo_area,
        responsable=datos.responsable,
        fecha_estimacion=datos.fecha_estimacion,
        estatus=datos.estatus,
        folio=nuevo_folio,
        retroalimentacion=datos.retroalimentacion,
        aprobado_por=datos.aprobado_por,
        fecha_aprobacion=datos.fecha_aprobacion,
        fecha_creacion=datos.fecha_creacion,
        prioridad=prioridad,  # ✅ Aquí insertamos el resultado
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


from fastapi import HTTPException

def finalizar_solicitud(db: Session, id: str):
    solicitud = db.query(Solicitud).filter(Solicitud.id == id).first()

    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")

    if not solicitud.aprobado_por or not solicitud.fecha_aprobacion:
        raise HTTPException(
            status_code=400,
            detail="No se puede finalizar. La solicitud no ha sido aprobada formalmente."
        )

    solicitud.estatus = "Finalizada"
    db.commit()
    db.refresh(solicitud)
    return solicitud

from datetime import datetime, timedelta, timezone

def verificar_solicitudes_pendientes(db: Session):
    hoy = datetime.now(timezone.utc)
    solicitudes = db.query(Solicitud).filter(Solicitud.estatus == "Pendiente").all()

    actualizadas = []
    for s in solicitudes:
        if s.fecha_creacion and (hoy - s.fecha_creacion).days > 3:
            s.estatus = "Pendiente Evaluación"
            actualizadas.append(s.folio)

    db.commit()
    return actualizadas


