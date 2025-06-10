"""API simple para Vercel escrita en Python 3.9"""

# Importamos BaseHTTPRequestHandler para manejar las solicitudes HTTP
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    """Manejador principal de la función"""

    def do_GET(self):
        """Responde a una solicitud GET con un mensaje simple"""
        # Indicamos que la respuesta fue exitosa
        self.send_response(200)

        # Establecemos las cabeceras de la respuesta
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # Enviamos el cuerpo de la respuesta
        mensaje = "Respuesta de la API de imagenología"
        self.wfile.write(mensaje.encode("utf-8"))
