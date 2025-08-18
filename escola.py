nome_aluno = input('Qual o nome do aluno?: ')
tipo_escola = input('Seu colégio é: \n [1] Público \n [2] Particular \n')
nota_1b = float(input('Digite sua nota do 1º Bimestre: '))
nota_2b = float(input('Digite sua nota do 2º Bimestre: '))
nota_3b = float(input('Digite sua nota do 3º Bimestre: '))
nota_4b = float(input('Digite sua nota do 4º Bimestre: '))
freq_aluno = int(input('Qual a frequencia do aluno?: '))
media_aluno = int((nota_1b + nota_2b + nota_3b + nota_4b) / 4)

freq_corte = 70 
media_corte = 7

if tipo_escola == '2':
    if media_aluno >= media_corte and freq_aluno >= freq_corte:
        resultado = 'Aprovado.'
        
    else:
        resultado = 'Reprovado.'
        
if tipo_escola == '1':
    if media_aluno >= media_corte or freq_aluno >= freq_corte:
        resultado = 'Aprovado.'
        
    else:
        resultado = 'Reprovado.'
        
if tipo_escola == '1':
    tipo = 'Pública'
else:
    tipo = 'Particular'
    
print(f'-Tipo: {tipo}\n -Frequencia de corte: {freq_corte} \n -Média de corte {media_corte}\n')
        
    
print(f'{nome_aluno}, sua média é: {media_aluno} e sua frequencia foi de {freq_aluno}. Você foi {resultado}')


'''
!= diferente
== igual
<= menor ou igual
>= maior ou igual
> maior
< menor
'''



