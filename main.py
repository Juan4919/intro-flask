#importar libreria flask
from flask import Flask,render_template

#Iniciar app con Flask
app = Flask(__name__)

#- inicializar parametros para servidor de flask -
#set FLASK_APP=main.py

#- comando para ejecutar el servidor - 
#flask --app main run 


#- comando para ejecutar servidor en otro puerto (default 5000) - 
#flask --app main run -p 5002

#- comando para ejecutar el servidor en modo debug, y realizar cambios en tiempo real -
#flask --app main --debug run 

@app.route("/hola")
def hola_mundo():
    return "Bienvenido al mundo flask"

#Ejercicio: Crear una ruta que devuelva una lista de frutas, el path sería /frutas

@app.route("/frutas")
def lista_frutas():
    listafrutas= ['Pera', 'manzana', 'platano']
    return listafrutas

@app.route("/nombre/<name>")
def tunombre(name):
    return f"hola {name} como estás"

#Ejercicio : realizar una ruta que devuelve el cuadrado de un numero dado, /numero/<parametro> 

@app.route("/numero/<parametro>")
def cuadrado(parametro):
    parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#Ejercicio : realizar una ruta que pueda solicitar o realizar operaciones de 
#suma, resta, multiplicación o división 
    
@app.route("/operacion/<int:valor1>/<string:ope>/<int:valor2>")
def calculo(valor1,ope,valor2):
    if ope =="sum":
        return f"la suma de {valor1} y {valor2} es {valor1+valor2}"
    elif ope =="res":
        return f"la resta de {valor1} y {valor2} es {valor1-valor2}"
    elif ope =="multi":
        return f"la multiplicacion de {valor1} y {valor2} es {valor1*valor2}"
    elif ope =="div":
        return f"la division de {valor1} y {valor2} es {valor1/valor2}"

@app.route("/<dato>")
def mihtml(dato):
    listafrutas= ['Pera', 'manzana', 'platano']
    return render_template("hola.html", variable = dato,frutas = listafrutas)
