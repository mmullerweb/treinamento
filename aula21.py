# Instalar lib flask dentro do windows 
######
from flask import Flask, request

app = Flask(__name__)

@app.route("/soma")
def soma():
    ###### validar se e vazio retornando mensagem para tela
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
def subtracao():
    a = request.args.get("a")
    b = request.args.get("b")
    multiplicacao = int(a) * int(b)
    return "multiplicacao é: " + str(multiplicacao)

@app.route("/divisao")
def subtracao():
    a = request.args.get("a")
    b = request.args.get("b")
    divisao = int(a) * int(b)
    return "divisao é: " + str(divisao)
# Rodar comando (flask run)