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
# Rodar comando (flask run)