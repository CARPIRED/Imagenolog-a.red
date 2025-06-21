"""API simple para Vercel escrita en Python 3.9"""

# Importamos BaseHTTPRequestHandler para manejar las solicitudes HTTP
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json


class handler(BaseHTTPRequestHandler):
    """Manejador principal de la función"""

    def do_GET(self):
        """Responde a una solicitud GET aceptando un parámetro 'prompt'."""
        # Parseamos los parámetros de la URL
        query_components = parse_qs(urlparse(self.path).query)
        prompt = query_components.get("prompt", [None])[0]

        if not prompt:
            # Si el parámetro falta o está vacío, respondemos con error
            self.send_response(400)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            respuesta = {"error": "Falta el parámetro 'prompt'"}
            self.wfile.write(json.dumps(respuesta).encode("utf-8"))
            return

        # Si el parámetro está presente, devolvemos un mensaje de éxito
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()

        respuesta = {"prompt": prompt, "mensaje": "Solicitud recibida"}
        self.wfile.write(json.dumps(respuesta).encode("utf-8"))
