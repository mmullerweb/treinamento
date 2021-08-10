# Instalar lib flask dentro do windows 
######
from flask import Flask, request

app = Flask(__name__)

@app.route("/soma")
def soma():
    a = request.args.get("a")
    b = request.args.get("b")
    soma = int(a) + int(b)
    return "Soma é: " + str(soma)

@app.route("/subtracao")
def subtracao():
    a = request.args.get("a")
    b = request.args.get("b")
    subtracao = int(a) - int(b)
    return "Subtracao é: " + str(subtracao)

@app.route("/multiplicacao")
def multiplicacao():
    a = request.args.get("a")
    b = request.args.get("b")
    multiplicacao = int(a) * int(b)
    return "Multiplicacao é: " + str(multiplicacao)

@app.route("/divisao")
def divisao():
    a = request.args.get("a")
    b = request.args.get("b")
    divisao = int(a) / int(b)
    return "Divisao é: " + str(divisao)
# Rodar comando (flask run)

