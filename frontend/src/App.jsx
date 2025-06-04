import { useState, useEffect } from "react";
import axios from "axios";
import SolicitudCard from "./components/SolicitudCard";

function App() {
  const [solicitudes, setSolicitudes] = useState([]);
  const [form, setForm] = useState({
    descripcion: "",
    tipo_area: "",
    responsable: "",
    fecha_estimacion: "",
  });

  const fetchSolicitudes = async () => {
    const res = await axios.get("http://localhost:8000/solicitudes");
    setSolicitudes(res.data);
  };

  useEffect(() => {
    fetchSolicitudes();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("http://localhost:8000/solicitudes", form);
    setForm({
      descripcion: "",
      tipo_area: "",
      responsable: "",
      fecha_estimacion: "",
    });
    fetchSolicitudes();
  };

  const cerrarSesion = () => {
    localStorage.removeItem("usuario");
    window.location.href = "/login";
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-lg max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold">Gestor de Solicitudes</h1>
          <button
            onClick={cerrarSesion}
            className="bg-red-600 text-white px-4 py-1 rounded hover:bg-red-700 transition"
          >
            Cerrar sesión
          </button>
        </div>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8"
        >
          <input
            name="descripcion"
            value={form.descripcion}
            onChange={handleChange}
            placeholder="Descripción"
            className="p-2 rounded border"
            required
          />
          <input
            name="tipo_area"
            value={form.tipo_area}
            onChange={handleChange}
            placeholder="Área"
            className="p-2 rounded border"
            required
          />
          <input
            name="responsable"
            value={form.responsable}
            onChange={handleChange}
            placeholder="Responsable"
            className="p-2 rounded border"
            required
          />
          <input
            name="fecha_estimacion"
            type="date"
            value={form.fecha_estimacion}
            onChange={handleChange}
            className="p-2 rounded border"
          />
          <button
            type="submit"
            className="col-span-1 md:col-span-4 bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
          >
            Crear Solicitud
          </button>
        </form>

        <h2 className="text-xl font-semibold mb-4">Solicitudes registradas</h2>
        <div className="space-y-4">
          {solicitudes.map((s) => (
            <SolicitudCard
              key={s.id}
              solicitud={s}
              onUpdate={fetchSolicitudes}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
