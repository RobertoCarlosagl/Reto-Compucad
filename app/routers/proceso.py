from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
import os
import shutil

from app.schemas.proceso import ProcesoCreate, ProcesoOut
from app.crud import proceso as crud_proceso
from app.database import SessionLocal

router = APIRouter(
    prefix="/procesos",
    tags=["Procesos"]
)

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear proceso
@router.post("/", response_model=ProcesoOut)
def crear_proceso(proceso: ProcesoCreate, db: Session = Depends(get_db)):
    return crud_proceso.crear_proceso(db, proceso)

# Listar procesos
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

# ----------- Subida y descarga de archivos -----------

UPLOAD_DIR = "uploads"

@router.post("/{proceso_id}/upload")
async def subir_archivo(proceso_id: UUID, archivo: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ruta = os.path.join(UPLOAD_DIR, f"{proceso_id}_{archivo.filename}")
    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(archivo.file, buffer)
    return {"mensaje": f"Archivo {archivo.filename} subido correctamente."}

@router.get("/{proceso_id}/download/{filename}")
def descargar_archivo(proceso_id: UUID, filename: str):
    ruta = os.path.join(UPLOAD_DIR, f"{proceso_id}_{filename}")
    if not os.path.exists(ruta):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    return FileResponse(ruta, filename=filename)
