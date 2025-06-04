import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const usuarios = [
  { correo: "Abraham.pardo@compucad.com.mx", password: "retocumplido25" },
  { correo: "isc_rmejia2021@accitesz.com", password: "roberto21" },
];

function getSaludo() {
  const hora = new Date().getHours();
  if (hora < 12) return "Buenos días";
  if (hora < 19) return "Buenas tardes";
  return "Buenas noches";
}

function Login() {
  const [correo, setCorreo] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem("usuario")) navigate("/");
  }, []);

  const login = () => {
    const match = usuarios.find(
      (u) => u.correo === correo && u.password === password
    );
    if (match) {
      localStorage.setItem("usuario", match.correo);
      navigate("/");
    } else {
      setError("Credenciales incorrectas.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-md shadow-md w-full max-w-sm">
        <p className="text-center text-lg text-gray-700 mb-6">{getSaludo()}</p>

        {error && <p className="text-red-600 mb-4 text-center">{error}</p>}

        <input
          type="email"
          placeholder="Correo electrónico"
          value={correo}
          onChange={(e) => setCorreo(e.target.value)}
          className="w-full p-2 mb-4 border border-gray-300 rounded"
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 mb-4 border border-gray-300 rounded"
        />
        <div className="flex justify-center">
          <button
            onClick={login}
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
          >
            Iniciar sesión
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
