from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash

import forms
app = Flask(__name__)

app.secret_key = "esta es la clave secreta"

@app.errorhandler(404)
def page_not_found(error):
    return "nada", 404



@app.route("/")
def index():
    return render_template("index.html")

@app.before_request
def antes_de_cada_peticion():
    g.prueba = "Hola"
    print("Antes 1")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    print("Dentro 2")
    valor = g.prueba
    print(valor)
    alumn_form = forms.UserForm(request.form)
    if request.method == "POST" and alumn_form.validate():
        nom = alumn_form.nombre.data
        apaterno = alumn_form.apaterno.data
        amaterno = alumn_form.amaterno.data
        edad = alumn_form.edad.data
        correo = alumn_form.correo.data
        mensaje = "Bienvenido: {}".format(nom)
        flash(mensaje)
        print("Nombre:{}".format(nom))
        print("Email:{}".format(correo))
        print("Apellido paterno:{}".format(apaterno))
        return render_template("alumnos.html", form = alumn_form, nombre = nom, correo = correo, apaterno = apaterno, amaterno = amaterno, edad = edad)
    else:
        return render_template("alumnos.html", form = alumn_form)

@app.after_request
def despues_de_cada_peticion(response):
    print("Despues 3")
    return response


@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/")
def hola():
    return "<p> Hola Mundo</p>"

@app.route("/hola")
def func():
    return "<h1>Saludo desde Hola - UTL!!!</h1>"

@app.route("/saludo")
def func1():
    return "<h1>Saludo desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola {}</h1>".format(nom)

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>El valor es {}</h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(nom, id):
    return "<h1>ID: {} NOMBRE: {}</h1>".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "<h1>La suma de: {} + {} = {}</h1>".format(n1, n2, (n1+n2))

@app.route("/multiplica", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        return  '''
                    <h1>La multiplicacion de: {} x {} = {}</h1>
                '''.format(num1, num2, (num1*num2))
    else:
        return  '''
                <form action="/multiplica" method="POST">
                    <label>N1: </label>
                    <input type="text" name="n1"/>
                    <label>N2: </label>
                    <input type="text" name="n2"/>
                    <input type="submit">
                </form>

                '''
                
                
@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")



@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        return  '''
                    <h1>La multiplicacion de: {} x {} = {}</h1>
                '''.format(num1, num2, (num1*num2))
    else:
        return  '''
                <form action="/multiplica" method="POST">
                    <label>N1: </label>
                    <input type="text" name="n1"/>
                    <label>N2: </label>
                    <input type="text" name="n2"/>
                    <input type="submit">
                </form>

                '''

if __name__ == "__main__":
    app.run(debug=True)