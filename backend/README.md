# Backend OAuth con Flask y Authlib

## Configuración

1. Crear un entorno virtual de Python:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
- Copiar `.env.example` a `.env`
- Configurar las credenciales de Google OAuth

## Obtener credenciales de Google OAuth

1. Ir a https://console.cloud.google.com/
2. Crear un nuevo proyecto o seleccionar uno existente
3. Habilitar la API de Google+ 
4. Ir a "Credenciales" > "Crear credenciales" > "ID de cliente de OAuth 2.0"
5. Configurar:
   - Tipo de aplicación: Aplicación web
   - URIs de redireccionamiento autorizados: `http://localhost:5000/authorize`
   - Orígenes de JavaScript autorizados: `http://localhost:5173`

## Ejecutar el servidor

```bash
python app.py
```

El servidor se ejecutará en http://localhost:5000

