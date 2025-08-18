nome = input('Qual seu nome?: ')
nota_1b = input('Digite sua nota do 1º Bimestre: ')
nota_2b = input('Digite sua nota do 2º Bimestre: ')
nota_3b = input('Digite sua nota do 3º Bimestre: ')
nota_4b = input('Digite sua nota do 4º Bimestre: ')
media = (float(nota_1b) + float(nota_2b) + float(nota_3b) + float(nota_4b)) / 4
mensagem = (f'Bem vindo:  {nome} sua média é:  {media}')
print(mensagem)
