from random import randint

#Jogo de adivinhação com diversos gatilhos

print('########## Início do Jogo ##########')
print('---------- Adivinhe o Tesouro ----------')
print('---------- Feito: por Myke Wellington----------')
print('')

menor = 0
maior = 100
random = randint(0,100)
chute = 0
chances = 10

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