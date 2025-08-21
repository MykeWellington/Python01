from flask import Flask, render_template

# Criar o app flsk
app = Flask(__name__)# dizendo que o nome será Flask

# Rota para a página inicial
@app.route('/')
def inicio():
    return '<h1> Olá Mundo </h1> <br> <h3> Bem vindo a minha página inicial! <br> <a href="/contato" >Fale comigo <h/3>'

@app.route('/contato')
def contato():
    return '<a href="mailto: mykewellington@gmail.com"> Me mande um e-mail! <hr> <a href="/" > <<< Página inicial </a>'

#Rota com variáveis na url
@app.route('/especial/<nome>')
def rotaespecial(nome):
    return f'<h1> <div style="background-color: lightblue;"> Seja bem vindo {nome} ao meu Sistema! </div> </h1> '


if __name__ == '__main__':
    app.run(debug=True)