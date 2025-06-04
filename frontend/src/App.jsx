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

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-2xl font-bold mb-4">Gestor de Solicitudes</h1>

      <form
        onSubmit={handleSubmit}
        className="bg-white p-4 rounded shadow-md mb-8 grid grid-cols-1 gap-4"
      >
        <input
          name="descripcion"
          value={form.descripcion}
          onChange={handleChange}
          placeholder="Descripción"
          className="border p-2 rounded"
          required
        />
        <input
          name="tipo_area"
          value={form.tipo_area}
          onChange={handleChange}
          placeholder="Área"
          className="border p-2 rounded"
          required
        />
        <input
          name="responsable"
          value={form.responsable}
          onChange={handleChange}
          placeholder="Responsable"
          className="border p-2 rounded"
          required
        />
        <input
          name="fecha_estimacion"
          type="date"
          value={form.fecha_estimacion}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Crear Solicitud
        </button>
      </form>

      <h2 className="text-xl font-semibold mb-2">Solicitudes registradas</h2>
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
  );
}

export default App;
