# 🧠 Gestor de Procesos – Reto Compucad 2025

Sistema web desarrollado para gestionar solicitudes de procesos internos con control de aprobación, seguimiento, generación de folio automático y priorización inteligente.

---

## 🚀 Tecnologías utilizadas

### Backend
- **Python 3.10+**
- **FastAPI** – Framework web rápido y moderno
- **SQLAlchemy** – ORM para manejo de base de datos
- **Alembic** – Migraciones automáticas
- **PostgreSQL** (con Supabase como hosting)
- **UUID** – Identificadores únicos para cada solicitud y proceso

### Frontend
- **React 18+** con **Vite**
- **Tailwind CSS** para estilos rápidos y responsivos
- **Axios** – Cliente HTTP
- **React Router DOM** – Navegación protegida
- **React Hooks** – Manejo de estado y efectos

---

## ⚙️ Instalación y ejecución

### 🐍 Backend

1. Clona el repositorio:

```bash
git clone https://github.com/RobertoCarlosagl/Reto-Compucad.git
cd Reto-Compucad


2. Crea entorno virtual:
python -m venv env

3. Activa entorno (Windows):
.\env\Scripts\activate

4. Instala dependencias:
pip install -r requirements.txt

5. Ejecuta el servidor:
uvicorn app.main:app --reload

Accede a la API en:

Swagger UI: http://localhost:8000/docs

 Frontend
1. Abre otra terminal y entra a la carpeta frontend/
cd frontend

2. Instala dependencias:
npm install

3. Ejecuta la app:
npm run dev

4. Accede a la app:
http://localhost:5173

🔐 Acceso
Usuarios válidos
Correo	Contraseña
Abraham.pardo@compucad.com.mx	retocumplido25
isc_rmejia2021@accitesz.com	roberto21

Si no hay sesión, el sistema redirige automáticamente al login.

Funcionalidades backend
📩 Crear solicitud con:
descripción
tipo de área
responsable
fecha estimada
🧠 Asignación automática de prioridad (Alta, Media, Baja)
🔢 Folio generado automáticamente con formato: CCADPRC-0001
🔒 Restricción de finalización: solo solicitudes aprobadas pueden finalizarse
⏱ Autoevaluación de estatus si pasan más de 3 días sin acción
📎 CRUD de procesos vinculados a cada solicitud
📂 Carga y descarga de archivos (adjuntos en procesos)


Funcionalidades frontend
🔐 Login protegido con usuarios válidos
🧾 Formulario para crear solicitudes
📋 Listado de solicitudes con:
folio
prioridad
estatus
✅ Botones para aprobar o rechazar
🧠 Saludo dinámico (según la hora)
🎨 Interfaz responsiva, con diseño limpio y profesional
🔓 Cerrar sesión desde cualquier pantalla


📂 Estructura de carpetas
gestor_procesos_compucad/
├── app/
│   ├── crud/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── utils/
│   └── main.py
├── alembic/
├── frontend/
│   ├── public/img/
│   │   └── login.png
│   ├── src/
│   │   ├── components/
│   │   │   └── SolicitudCard.jsx
│   │   ├── pages/
│   │   │   └── Login.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
├── requirements.txt
├── README.md
└── .env

Consideraciones
🔐 El login es simulado con usuarios hardcodeados (sin Firebase por tiempo)
📡 Backend desplegable en cualquier servicio con PostgreSQL (ej. Supabase)
💾 Las rutas protegidas en frontend evitan acceso directo sin sesión

👨‍💻 Autor
Roberto Carlos Mejia Aguilera 
Desarrollado para el Reto Hackathon 2025 – Compucad

✅ Conclusión
Este sistema demuestra una solución modular, funcional, segura y profesional para la gestión de procesos internos. Está listo para escalar, mejorar visualmente o integrarse con servicios externos.

README PARTE DOS PARA QUE LO CALEN PUES
3. Pruebas en Swagger (backend API)
Acceda a 👉 http://localhost:8000/docs

📩 Crear una solicitud
Método: POST /solicitudes

Campos requeridos:
descripcion: "Solicito equipo de desarrollo"
tipo_area: "TI"
responsable: "Juan Pérez"
fecha_estimacion: "2025-06-10"
✅ Al guardar, genera un folio automático (ej. CCADPRC-0001)
✅ También asigna una prioridad automática (según keywords)
Ver todas las solicitudes
Método: GET /solicitudes

✅ Verifica que se muestre el nuevo folio y estatus "Pendiente"
 Aprobar una solicitud
Método: PUT /solicitudes/{id}
Pasa el ID de la solicitud creada
Cambia los valores:
aprobado_por: "Abraham"
estatus: "Aprobada"

✅ Se guarda la fecha de aprobación
🚫 Finalizar una solicitud sin aprobar
Método: PUT /solicitudes/finalizar/{id}
Resultado esperado: ❌ Error 400, porque aún no está aprobada

✅ Finalizar una solicitud aprobada
Primero aprueba la solicitud como en el paso anterior
Luego llama: PUT /solicitudes/finalizar/{id}
✅ Estatus cambia a "Finalizada"


🧾 4. Pruebas en el frontend (React UI)
Abrir: 👉 http://localhost:5173
👤 Login
Ingresa con uno de los usuarios autorizados
Saludo cambia según la hora del día
Si el login es correcto, te lleva al dashboard

📝 Crear solicitud
Llena el formulario con:
Descripción
Tipo de área
Responsable
Fecha estimada
Haz clic en “Crear solicitud”
✅ Se muestra en la lista de abajo


 Visualización
Las solicitudes tienen:
Folio
Prioridad visual (color)
Estatus
Botones “Aprobar” y “Rechazar”

✅ Aprobar una solicitud
Da clic en “Aprobar”
El estatus cambia automáticamente

❌ Rechazar una solicitud
Da clic en “Rechazar”
Se solicita una retroalimentación
El estatus cambia a “Rechazada”

Cerrar sesión
Arriba a la derecha hay un botón “Cerrar sesión”
Te regresa al login
No puedes acceder a rutas protegidas sin iniciar sesión de nuevo

