import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import App from "./App.jsx";
import Login from "./pages/Login.jsx";
import "./index.css";

// Componente de protección
function RutaPrivada({ children }) {
  const logueado = localStorage.getItem("usuario");
  return logueado ? children : <Navigate to="/login" />;
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <RutaPrivada>
              <App />
            </RutaPrivada>
          }
        />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
