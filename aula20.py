# Instalar lib flask dentro do windows 
######
from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "Teste...."

@app.route("/abc")
def abc():
    return "UUUUUU"
# Rodar comando (flask run)