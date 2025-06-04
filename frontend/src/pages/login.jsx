import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../../src/styles/login.css"; // importa tu estilo CSS puro

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
    <div className="container">
      {/* Lado izquierdo */}
      <div className="left">
        <img src="/img/login.png" alt="Fondo login" className="logo" />
        <button className="btn-modal">Quiénes Somos</button>
        <button className="btn-modal">Ayuda</button>
        <div className="contact-info">
          <p>Correo: abraham.pardo@compucad.com.mx</p>
          <p>LinkedIn: Abraham Pardo</p>
        </div>
      </div>

      {/* Lado derecho */}
      <div className="right">
        <div className="login-box">
          <h2>LOGIN</h2>
          <h4>{getSaludo()}</h4>
          {error && <p className="alert error">{error}</p>}
          <form onSubmit={(e) => e.preventDefault()}>
            <input
              type="email"
              placeholder="Correo electrónico"
              value={correo}
              onChange={(e) => setCorreo(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <button type="submit" onClick={login}>
              Iniciar sesión
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
