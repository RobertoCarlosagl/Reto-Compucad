from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.solicitud import SolicitudCreate, SolicitudOut
from app.crud import solicitud as crud_solicitud
from typing import List
from uuid import UUID

router = APIRouter(
    prefix="/solicitudes",
    tags=["Solicitudes"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SolicitudOut)
def crear_solicitud(datos: SolicitudCreate, db: Session = Depends(get_db)):
    return crud_solicitud.crear_solicitud(db, datos)

@router.get("/", response_model=List[SolicitudOut])
def listar_solicitudes(db: Session = Depends(get_db)):
    return crud_solicitud.obtener_solicitudes(db)

@router.get("/{id}", response_model=SolicitudOut)
def obtener_por_id(id: UUID, db: Session = Depends(get_db)):
    solicitud = crud_solicitud.obtener_solicitud_por_id(db, id)
    if solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

@router.put("/{id}/finalizar", response_model=SolicitudOut)
def finalizar(id: UUID, db: Session = Depends(get_db)):
    return crud_solicitud.finalizar_solicitud(db, str(id))


@router.put("/verificar_evaluaciones")
def verificar_evaluaciones(db: Session = Depends(get_db)):
    actualizados = crud_solicitud.verificar_solicitudes_pendientes(db)
    return {"mensaje": f"{len(actualizados)} solicitudes actualizadas.", "folios": actualizados}

