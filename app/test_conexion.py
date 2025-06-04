from .database import SessionLocal

def probar_conexion():
    try:
        db = SessionLocal()
        print("✅ ¡Conexión a la base de datos exitosa!")
    except Exception as e:
        print("❌ Error de conexión:", e)
    finally:
        db.close()

probar_conexion()
