from flask import Flask, render_template, request, flash

app = Flask(__name__)

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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/terminos_y_condiciones')
def terminos_y_condiciones():
    return render_template("terminos_y_condiciones.html")

@app.route('/recuperacion_contrasena')
def recuperacion_contrasena():
    return render_template("recuperacion_contrasena.html")


