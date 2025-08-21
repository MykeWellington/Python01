from flask import Flask, redirect, url_for, request, render_template
from requests import get

app = Flask(__name__)

@app.route('/')#Estrutura fixa das rotas
def pagina_inicial():
    return render_template ('inicio.html')

@app.route('/entrar')#Estrutura fixa das rotas
def fazer_login():
    return render_template ('login.html')

@app.route('/pagina403')#Estrutura fixa das rotas
def pagina_403():
    return render_template ('pagina403.html')

@app.route('/welcome')#Estrutura fixa das rotas
def welcome():
    return render_template ('welcome.html')

@app.route('/documentacao')#Estrutura fixa das rotas
def documentacao():
    return render_template ('documentacao.html')

@app.route('/validador', methods=['POST', 'GET'])#Estrutura fixa das rotas
def validador():
    acesso_usuario = 'Myke'
    acesso_senha = '123'
    if request.method == 'POST':
        usuario = request.form['c_usuario'] 
        senha = request.form['c_senha']
        if usuario == acesso_usuario and senha == acesso_senha:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))
    else:
        usuario = request.args.get('c_usuario')
        senha = request.args.get('c_senha')
        if usuario == acesso_usuario and senha == acesso_senha:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))



if __name__ == '__main__':
    app.run(debug=True)