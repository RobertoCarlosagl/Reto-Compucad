from fastapi import FastAPI
from app.routers import solicitud, proceso
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Gestor de Procesos - Compucad Hackathon",
    version="1.0.0"
)

# Habilitar CORS (por si conectas desde React u otro frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringir esto si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(solicitud.router)
app.include_router(proceso.router)

# Ruta de prueba
@app.get("/")
def read_root():
    return {"mensaje": "API del gestor de procesos activa 🚀"}
