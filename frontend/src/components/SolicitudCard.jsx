import axios from "axios";

function SolicitudCard({ solicitud, onUpdate }) {
  const aprobar = async () => {
    const confirmado = confirm("¿Aprobar esta solicitud?");
    if (!confirmado) return;

    await axios.put(`http://localhost:8000/solicitudes/${solicitud.id}`, {
      aprobado_por: "Director X", // puedes reemplazar con input dinámico si quieres
      fecha_aprobacion: new Date().toISOString(),
      estatus: "Aprobada",
    });
    onUpdate();
  };

  const rechazar = async () => {
    const razon = prompt("¿Razón del rechazo?");
    if (!razon) return;

    await axios.put(`http://localhost:8000/solicitudes/${solicitud.id}`, {
      retroalimentacion: razon,
      estatus: "Rechazada",
    });
    onUpdate();
  };

  const color =
    solicitud.prioridad === "Alta"
      ? "border-red-500"
      : solicitud.prioridad === "Media"
      ? "border-orange-400"
      : "border-green-500";

  return (
    <div className={`bg-white p-4 rounded shadow-md border-l-4 ${color}`}>
      <p className="font-bold">{solicitud.folio}</p>
      <p>{solicitud.descripcion}</p>
      <p className="text-sm text-gray-500">
        Prioridad: {solicitud.prioridad} | Estatus: {solicitud.estatus}
      </p>
      <div className="mt-2 flex gap-2">
        <button
          onClick={aprobar}
          className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
        >
          Aprobar
        </button>
        <button
          onClick={rechazar}
          className="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700"
        >
          Rechazar
        </button>
      </div>
    </div>
  );
}

export default SolicitudCard;
