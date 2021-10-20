from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login.html') 

@app.route("/registro", methods=["GET", "POST"])
def registrarse():
    return render_template('Register.html') 

@app.route("/principal", methods=["GET", "POST"])
def ir_a_principal():
    return render_template('Feed_page.html')

@app.route("/perfil", methods=["GET", "POST"])
def ir_a_perfil():
    return render_template('Perfil.html')


@app.route("/Dashboard1", methods=["GET", "POST"])
def ir_a_DashboardAdmon():
    return render_template('Dashboard1.html')


@app.route("/Dashboard", methods=["GET", "POST"])
def ir_a_DashboardSuperAdmon():
    return render_template('Dashboard.html')        


@app.route("/BuscadorAdmon", methods=["GET", "POST"])
def buscar_admon():
    return render_template('buscador_administrador.html')  


@app.route("/perfil/mensaje", methods=["GET", "POST"])
def mensaje():
    return render_template('Mensaje.html')    


@app.route("/perfil/nuevoPost", methods=["GET", "POST"])
def newPost():
    return render_template('NewPublicacion.html')  


@app.route("/perfil/opciones", methods=["GET", "POST"])
def option():
    return render_template('optionPost.html')    

@app.route("/perfil/usuarios", methods=["GET", "POST"])
def users():
    return render_template("BusquedaUsuario.html")

@app.route("/super_administrador/editar", methods=["GET", "POST"])
def editUsers():
    return render_template("EditarUsuario.html")

@app.route("/super_administrador", methods=["GET", "POST"])
def superAdmin():
    return render_template("Dashboard_SuperAdministrador.html")

@app.route("/administrador", methods=["GET", "POST"])
def Admin():
    return render_template("Dashboard_Administrador.html")

@app.route("/administrador/publicacion", methods=["GET", "POST"])
def AdminPost():
    return render_template("optionPost_admin.html")

@app.route("/administrador/editar", methods=["GET", "POST"])    
def AdminEditUser():
    return render_template("EditarUsuario_permisosAdmin.html")

@app.route("/perfil/comentarios", methods=["GET", "POST"])    
def comentario():
    return render_template("Comentarios.html")


@app.route("/perfil/nuevo", methods=["GET", "POST"])    
def newComentario():
    return render_template("AddComent.html")
#***************************************************************************
