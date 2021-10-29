import os

from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect, url_for
from flask import jsonify
from flask import session
from flask import g
from flask import send_file
from flask import make_response
import functools
from werkzeug.security import generate_password_hash, check_password_hash

from utils import isUsernameValid, isEmailValid, isPasswordValid
import yagmail as yagmail
from forms import Formulario_Usuario, Formulario_registro
from db import get_db, close_db

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Usuario requerido:
# Es como si se estuviese llamando directamente a la función interna
''' def login_required(view):
    @functools.wraps( view ) # toma una función utilizada en un decorador y añadir la funcionalidad de copiar el nombre de la función.
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect( url_for( 'login' ) )
        return view( **kwargs )
    return wrapped_view '''

@app.route('/index') #Esto lo cree para poder acceder a él desde las otras pestañas.
def index():
    return render_template("index2.html")

@app.route('/')
def index2():
    return render_template("index.html")

@app.route('/check_in')
def check_in():
    return render_template("usuario/usuarios_check_in.html")

@app.route('/usuarios_editar_datos')
def usuarios_editar_datos():
    return render_template("usuario/usuarios_editar_datos.html")

@app.route('/usuarios_mis_vuelos')
def usuarios_mis_vuelos():
    return render_template("usuario/usuarios_mis_vuelos.html")

@app.route('/usuarios_reserva')
def usuarios_reserva():
    return render_template("usuario/usuarios_reserva.html")

@app.route('/usuarios_comentarios')
def usuarios_comentarios():
    return render_template("usuario/usuarios_comentarios.html")

@app.route('/piloto_comentarios_vuelo')
def piloto_comentarios_vuelo():
    return render_template("piloto/piloto_comentarios_vuelo.html")

@app.route('/piloto_editar_datos')
def piloto_editar_datos():
    return render_template("piloto/piloto_editar_datos.html")

@app.route('/piloto_vuelos_asignados')
def piloto_vuelos_asignados():
    return render_template("piloto/piloto_vuelos_asignados.html")

@app.route('/admin_aviones')
def admin_aviones():
    return render_template("admin/admin_aviones.html")

@app.route('/admin_pilotos')
def admin_pilotos():
    return render_template("admin/admin_pilotos.html")

@app.route('/admin_usuarios')
def admin_usuarios():
    return render_template("admin/admin_usuarios.html")

@app.route('/admin_vuelos')
def admin_vuelos():
    return render_template("admin/admin_vuelos.html")

''' @app.route('/login')
def login():
    return render_template("login.html") '''

@app.route('/registro')
def registro():
    form = Formulario_registro()
    return render_template("registro.html", form=form)

@app.route('/terminos_y_condiciones')
def terminos_y_condiciones():
    return render_template("terminos_y_condiciones.html")

@app.route('/recuperacion_contrasena')
def recuperacion_contrasena():
    return render_template("recuperacion_contrasena.html")

@app.route('/login')
def login():
    form = Formulario_Usuario()
    return render_template("login.html", form=form)




''' @app.before_request
def cargar_usuario_registsrado():
    print("before_request")
    id_usuario = session.get( 'id_usuario' )
    print("type(id_usuario):", type(id_usuario))
    print("id_usuario:", id_usuario)
    if id_usuario is None: 
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM Usuarios WHERE id = ?'
            ,(id_usuario,)
        ).fetchone()

@app.route('/logout')
def logout():
    session.clear()
    return redirect( 'login' ) '''


