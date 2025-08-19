from random import randint

#Jogo de adivinhação com diversos gatilhos

print('########## Início do Jogo ##########')
print('---------- Adivinhe o Tesouro ----------')
print('---------- Feito: por Myke Wellington----------')
print('')

nivel = int(input('Escolha seu nível\n[1] Fácil\n[2] Medio\n [3] Difícil\nAqui: '))
print(nivel)



if nivel == '1':
    menor = 0
    maior = 50
    chences = 10
    print('Faremos então um jogo de 0 a 100!')
    
elif nivel == '2':
    menor = 0
    maior = 100
    chances = 7
    
else:
    
    menor = 0
    maior = 500
    chances = 5
    print('Então faremos um jogo de 0 a 1000')
    
random = randint(menor,maior)
chute = 0

    
print(f'Que os jogos comecem!\n Você tem {chances} chances para acertar\n Pense com cuidado!')
    

while chute != random:
    chute = input(f'Chute um número entre {menor} e {maior}\nAqui: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns! Você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else:
            print('')
            if chute > random:
                print(f'Erroouuu!!! \nDica: É um número menor que {chute}.')
            else:
                print(f'Erroouuu!!! \nDica: É um número maior que {chute}.')
                
            print('Você ainda tem {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Sua chances acabaram! Você perdeu! :/')
            print(f'O valor esperado era {random}.')
            print('')
            break
    




    print('########## Fim de Jogo ##########')
    print('---------- Obrigado por jogar ----------')