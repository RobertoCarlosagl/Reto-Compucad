from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.schemas.proceso import ProcesoCreate, ProcesoOut
from app.crud import proceso as crud_proceso
from app.database import SessionLocal

router = APIRouter(
    prefix="/procesos",
    tags=["Procesos"]
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo proceso
@router.post("/", response_model=ProcesoOut)
def crear_proceso(proceso: ProcesoCreate, db: Session = Depends(get_db)):
    return crud_proceso.crear_proceso(db, proceso)

# Listar todos los procesos
@router.get("/", response_model=List[ProcesoOut])
def listar_procesos(db: Session = Depends(get_db)):
    return crud_proceso.obtener_procesos(db)

# Obtener proceso por ID
@router.get("/{proceso_id}", response_model=ProcesoOut)
def obtener_proceso(proceso_id: UUID, db: Session = Depends(get_db)):
    return crud_proceso.obtener_proceso_por_id(db, proceso_id)

# Eliminar proceso
@router.delete("/{proceso_id}")
def eliminar_proceso(proceso_id: UUID, db: Session = Depends(get_db)):
    return crud_proceso.eliminar_proceso(db, proceso_id)
