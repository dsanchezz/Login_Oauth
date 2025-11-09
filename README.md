# Login OAuth - React + TypeScript + Python Flask

Sistema de autenticación con OAuth 2.0 usando Google como proveedor de identidad.

##  Características

- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: Python Flask + Authlib
- **Autenticación**: Google OAuth 2.0
- **Diseño**: Interfaz elegante con escala de grises
- **Seguridad**: Manejo seguro de sesiones con cookies

## Requisitos Previos

- Node.js (v16 o superior)
- Python 3.8+
- Una cuenta de Google Cloud Platform

## Configuración

### 1. Configurar Google OAuth

1. Ir a [Google Cloud Console](https://console.cloud.google.com/)
2. Crear un nuevo proyecto o seleccionar uno existente
3. Navegar a "APIs y servicios" > "Credenciales"
4. Hacer clic en "Crear credenciales" > "ID de cliente de OAuth 2.0"
5. Configurar la pantalla de consentimiento si es necesario
6. En la configuración del cliente OAuth:
   - **Tipo de aplicación**: Aplicación web
   - **Orígenes de JavaScript autorizados**: `http://localhost:5173`
   - **URIs de redireccionamiento autorizados**: `http://localhost:5000/authorize`
7. Copiar el **Client ID** y **Client Secret**

### 2. Configurar el Backend

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Copiar el archivo de ejemplo y configurar variables de entorno
# Crear un archivo .env en la carpeta backend con:
GOOGLE_CLIENT_ID=tu-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=tu-client-secret
SECRET_KEY=una-clave-secreta-super-segura-y-aleatoria
```

### 3. Configurar el Frontend

```bash
# Desde la raíz del proyecto
npm install

# Las dependencias de Tailwind ya están configuradas
```

## Ejecutar la Aplicación

### Terminal 1 - Backend:
```bash
cd backend
venv\Scripts\activate  # En Windows
# o: source venv/bin/activate  # En Linux/Mac
python app.py
```

El backend se ejecutará en: `http://localhost:5000`

### Terminal 2 - Frontend:
```bash
# Desde la raíz del proyecto
npm run dev
```

El frontend se ejecutará en: `http://localhost:5173`

## Uso

1. Abrir el navegador en `http://localhost:5173`
2. Hacer clic en "Continuar con Google"
3. Seleccionar tu cuenta de Google
4. Autorizar la aplicación
5. Serás redirigido de vuelta con tu sesión iniciada

##  Estructura del Proyecto

```
loginOauth/
├── backend/
│   ├── app.py              # Servidor Flask con OAuth
│   ├── requirements.txt    # Dependencias Python
│   └── README.md          # Documentación del backend
├── src/
│   ├── components/
│   │   └── Login.tsx      # Componente de login
│   ├── App.tsx            # Componente principal
│   └── index.css          # Estilos con Tailwind
├── tailwind.config.js     # Configuración Tailwind
└── package.json           # Dependencias Node
```

## Seguridad

- Las sesiones se manejan de forma segura con cookies HTTP-only
- CORS configurado para permitir solo el origen del frontend
- Las credenciales OAuth nunca se exponen al cliente
- Tokens de acceso manejados exclusivamente en el backend

## Notas Importantes

- **Desarrollo**: Las URLs están configuradas para desarrollo local
- **Producción**: Actualizar las URLs y configurar HTTPS
- **Secret Key**: Usar una clave aleatoria y segura en producción
- **Variables de Entorno**: Nunca commitear el archivo `.env`

## Tecnologías

- **Frontend**: React 19, TypeScript, Tailwind CSS, Vite
- **Backend**: Flask 3.0, Authlib 1.3, Flask-CORS
- **OAuth**: Google OAuth 2.0 con OpenID Connect

## Recursos

- [Authlib Documentation](https://docs.authlib.org/)
- [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [React Documentation](https://react.dev/)
