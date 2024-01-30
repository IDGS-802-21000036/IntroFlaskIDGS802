from flask import Flask, request, render_template
import forms
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    alumn_form = forms.UserForm(request.form)
    if request.method == "POST":
        nom = alumn_form.nombre.data
        email = alumn_form.email.data
        apaterno = alumn_form.apaterno.data
        print("Nombre:{}".format(nom))
        print("Email:{}".format(email))
        print("Apellido paterno:{}".format(apaterno))
        return render_template("alumnos.html", form = alumn_form, nombre = nom, email = email, apaterno = apaterno)
    else:
        return render_template("alumnos.html", form = alumn_form)

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