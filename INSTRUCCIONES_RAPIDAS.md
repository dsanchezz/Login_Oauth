# Instrucciones Rápidas de Inicio

## Primer Uso - Configuración Inicial

### Paso 1: Obtener Credenciales de Google OAuth
1. Ve a https://console.cloud.google.com/
2. Crea un proyecto nuevo
3. Ve a "APIs y servicios" > "Credenciales"
4. Crea un "ID de cliente de OAuth 2.0"
5. Configura:
   - **Orígenes autorizados**: `http://localhost:5173`
   - **URIs de redirección**: `http://localhost:5000/authorize`
6. Copia el Client ID y Client Secret

### Paso 2: Configurar Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Crear archivo `.env` en la carpeta `backend/`:
```
GOOGLE_CLIENT_ID=tu-client-id-aqui
GOOGLE_CLIENT_SECRET=tu-client-secret-aqui
SECRET_KEY=clave-secreta-aleatoria-aqui
```

### Paso 3: Configurar Frontend
```bash
cd ..
npm install
```

## Uso Diario - Iniciar Aplicación

### Terminal 1 (Backend):
```bash
cd backend
venv\Scripts\activate
python app.py
```

### Terminal 2 (Frontend):
```bash
npm run dev
```

### Acceder:
Abre tu navegador en: http://localhost:5173

## Lista de Verificación

- [ ] Credenciales de Google OAuth obtenidas
- [ ] Archivo `.env` creado en `backend/`
- [ ] Dependencias Python instaladas (`pip install -r requirements.txt`)
- [ ] Dependencias Node instaladas (`npm install`)
- [ ] Backend corriendo en puerto 5000
- [ ] Frontend corriendo en puerto 5173

## Solución de Problemas Comunes

### Error: "Client ID not found"
→ Verifica que el archivo `.env` esté en la carpeta `backend/` con las credenciales correctas

### Error: "CORS"
→ Asegúrate de que el backend esté corriendo en puerto 5000 y el frontend en 5173

### Error: "Redirect URI mismatch"
→ Verifica en Google Console que la URI de redirección sea exactamente: `http://localhost:5000/authorize`

### Error al instalar dependencias Python
→ Asegúrate de tener Python 3.8+ instalado: `python --version`

## Contacto y Ayuda

Si tienes problemas, revisa:
1. README.md principal
2. backend/README.md para detalles del backend
3. La consola del navegador para errores de JavaScript
4. La terminal del backend para errores de Python

