# Instalar lib flask dentro do windows 
######
import pymysql
from flask import Flask, request

app = Flask(__name__)

conn = pymysql.connect(host="mysql.by4u.com.br",user='by4u02',password='Treina2021',database='by4u02',cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


@app.route("/pessoa/criar")
def criar():
    nome = request.args.get("nome")
    data_nascimento = request.args.get("data_nascimento")
    sql = "INSERT INTO pessoa(nome, data_nascimento)VALUES(%s,%s)"
    cursor.execute(sql,(nome,data_nascimento))
    conn.commit()
    return "OK"

@app.route("/pessoa/lista")
def lista():
    sql = "SELECT * FROM pessoa"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    
    html = f'''
    <h1>Lista de pessoas</h1>
    <hr/>
    '''
    for r in resultado:
        html = f"{html} Nome: {r['nome']} / Data Nascimento: {str(r['data_nascimento'])} <a href='http://localhost:5000/pessoa/deletar?id={r['id']}'>Deletar</a> <br/>"
        sql = "DELETE FROM pessoa WHERE id = 38"
        cursor.execute(sql)
        conn.commit()
    return html

    #print(resultado)
    return html