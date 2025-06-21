# Imagenolog-a.red
Imagenología Médica Clínica Basada en la Evidencia

## Uso de la aplicación

### Configurar `OPENAI_API_KEY`

1. **Local:** exporte su clave en la terminal antes de ejecutar el script:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

2. **Vercel:** añada la variable en su proyecto con el CLI de Vercel:

   ```bash
   vercel env add OPENAI_API_KEY
   ```

### Ejecutar el script

Ejecute `app.py` para enviar el prompt de imagenología médica al modelo:

```bash
python app.py
```

El script imprimirá la respuesta devuelta por la API.

### Despliegue en Vercel

Si desea exponer la API en la nube, ejecute el comando de despliegue de Vercel en la raíz del repositorio:

```bash
vercel --prod
```

### Uso de la API

Una vez desplegada, la función puede invocarse en `/api/imagenologia`.
Prueba la respuesta con `curl`:

```bash
curl "https://<tu-deploy>.vercel.app/api/imagenologia"
```

La respuesta será un mensaje de texto similar a:

```
Respuesta de la API de imagenología
```
