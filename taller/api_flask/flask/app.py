from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<h1>Taller 13</h1> <br>  <p>Realizado por: Jeferson Cueva</p> "


@app.route("/edificios")
def edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/",
            auth=('jecueva11', 'root'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("edificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/departamentos")
def departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('jecueva11', 'root'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_prop':d['nombre_prop'], 'costo_depart':d['costo_depart'],
        'numero_cuartos':d['numero_cuartos'], 'edificio': obtener_edificio(d['edificio'])})
    return render_template("departamento.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('jecueva11', 'root'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
