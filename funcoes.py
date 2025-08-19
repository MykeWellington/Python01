'''
def minhaFuncao():
    print('Olá Clarify')
    
minhaFuncao()
minhaFuncao()
'''

cidades = ['São Paulo', 'Osasco','Poá','São Bernardo do Campo']
cidades2 = ['Suzano','Mogi','Diadema', 'Mauá']
contador = 0

def minhaFuncaoMelhorada(local, giro):
    print(str(giro) + ' - ' + local)
    
for cidade in cidades:
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)
    
#contador = 0    

for cidade in cidades2:
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)

    