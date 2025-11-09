from flask import Flask, redirect, url_for, session, jsonify, request
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# Habilitar CORS para el frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# Configurar OAuth
oauth = OAuth(app)

# Configurar Google OAuth
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.route('/')
def home():
    return jsonify({'message': 'OAuth Backend API', 'status': 'running'})

@app.route('/login')
def login():
    """Redirige al usuario a Google para autenticación"""
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    """Callback de Google OAuth"""
    try:
        token = google.authorize_access_token()
        user_info = token.get('userinfo')
        
        # Guardar información del usuario en la sesión
        session.permanent = True
        session['user'] = {
            'email': user_info['email'],
            'name': user_info['name'],
            'picture': user_info.get('picture', '')
        }
        
        # Redirigir al frontend con éxito
        return redirect('http://localhost:5173?login=success')
    except Exception as e:
        print(f"Error en autorización: {str(e)}")
        return redirect('http://localhost:5173?login=error')

@app.route('/user')
def get_user():
    """Obtener información del usuario autenticado"""
    user = session.get('user')
    if user:
        return jsonify({'authenticated': True, 'user': user})
    return jsonify({'authenticated': False}), 401

@app.route('/logout')
def logout():
    """Cerrar sesión del usuario"""
    session.pop('user', None)
    return jsonify({'message': 'Logout successful'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

