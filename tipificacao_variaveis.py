#Aula 1: Tipos de dados e variáveis.

# -------------strings (textos)-------------

nome = 'Anaximandro'
curso = "Escola de Thales"
mensagem = 'Bem vindo ' + nome + ' ao curso ' + curso
print(mensagem)
# para chamar uma variável dentro de um texto utilizamos o "+".

# Agora vamos deixar o usuário digitar seu nome.
nome_usuario = input('Digite o seu nome: ')
curso_usuario = input('Qual seu curso?: ')

#Usando f-string (Forma mais moderna de formatar uma string).
mensagem2 = f'Olá {nome_usuario}, seja bem vindo ao curso {curso_usuario}!'
print(mensagem2) 

#Algumas funções úteis de string
print(nome_usuario.upper()) # vamos deixa-lo em maiúsculo com .upper   
print(nome_usuario.lower()) # vamos deixa-lo em minúsculo com .lower  
print(nome_usuario.title()) # vamos deixa-lo a primeira letra em maiúsculo com .title


# Também podemos repetir strings com o operador *
linha = '-' * 30
print(linha)
print('Saia da frente do Sol')
print(linha)

