# Entendendo for e While, conceitos de loopings.
palavra = 'Tangamandápio'
contador = 0

for letra in palavra:
    print (str(contador) + ' - ' + letra)
    contador = contador + 1
    
cidades = ['São Paulo', 'Osasco','Poá','São Bernardo do Campo']

for cidade in cidades:
    print(cidade)
print('------------------------')    
print(cidades[3])

print('--------Trabalhando com While ------------')

botao_executar = True # boolean true/false.
contador = 0

while botao_executar:
    print(contador)
    contador = contador + 1
    if contador >= 100:
        botao_executar = False
        
print('Cabô o looping!')

    