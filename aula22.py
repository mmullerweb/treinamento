# Instalar lib flask dentro do windows 
######
from flask import Flask, request

app = Flask(__name__)

@app.route("/pessoa/criar")
def criar():
    return ""