from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    lista=["jorge","Marisa","Sergio","Raúl"]
    return render_template("index.html", titulo="Bienvenido", nombre_alumnos=lista)

@app.route('/hola')
def hola_mundo():
    return "Hola mundo"

@app.route('/dashboard/<nombre>')
def dashboard(nombre):
    return f"Bienvenido {nombre}"

@app.route('/login', methods= ['POST','GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        return redirect(url_for('dashboard', nombre=usuario))
    else:
        usuario = request.args.get('nombre')
        return render_template('login.html')




#app.run(host='0.0.0.0', port=81)
app.run()