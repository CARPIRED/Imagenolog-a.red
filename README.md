# Imagenolog-a.red
Imagenología Médica Clínica Basada en la Evidencia

## Uso de la aplicación

1. Coloque su clave de API de OpenAI en la variable de entorno `OPENAI_API_KEY`.
2. Ejecute el script `app.py` para enviar el prompt de imagenología médica al modelo.
   
```bash
python app.py
```

El script imprimirá la respuesta devuelta por la API.

## Despliegue en Vercel

1. Instale la [CLI de Vercel](https://vercel.com/docs/cli) con `npm i -g vercel`.
2. Ejecute `vercel login` para autenticar su cuenta.
3. Desde este directorio, ejecute `vercel` y siga las instrucciones en pantalla.
4. Al finalizar el despliegue, abra la URL proporcionada para ver la página y la API en funcionamiento.

El archivo `vercel.json` ya configura `public/index.html` como página principal y la función de Python en `/api/imagenologia`.
