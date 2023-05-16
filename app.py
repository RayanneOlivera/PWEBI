from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("/components/index.html", titulo_pagina="Página inicial")

@app.route("/novaconta")
def novaconta():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    return f'Nome: {nome} <br> E-mail: {email} <br> \
    Senha: {senha} <br>Confirmação: {confsenha}'

    



    
if __name__ == "__main__":
    app.run(debug=True)