# Imagenolog-a.red
Imagenología Médica Clínica Basada en la Evidencia

## Uso de la aplicación

1. Coloque su clave de API de OpenAI en la variable de entorno `OPENAI_API_KEY`.
2. Ejecute el script `app.py` para enviar el prompt de imagenología médica al modelo.
   
```bash
python app.py
```

El script imprimirá la respuesta devuelta por la API.

## Uso de la API

La función desplegada en Vercel se encuentra en `/api/imagenologia` y ahora
acepta un parámetro `prompt` mediante la cadena de consulta. Responde en formato
JSON con el valor del `prompt` recibido o un mensaje de error si el parámetro no
se proporciona.

Ejemplo de llamada:

```bash
curl "https://<tu-deploy>.vercel.app/api/imagenologia?prompt=hola"
```

Respuesta esperada:

```json
{
  "prompt": "hola",
  "mensaje": "Solicitud recibida"
}
```
