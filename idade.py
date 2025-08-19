executar = True

while executar:
    try:  
        anoNascimento = int (input('Em que ano você nasceu? '))
        anoAtual =  int(input('Em que ano estamos? '))
        idade = anoAtual - anoNascimento
        print (f'Você tem: {idade} anos')

    except ValueError:
        print('Por favor, digite um número válido para os anos.')  
    
    opcao = input('\nDeseja testar novamente? \nSim ou Não? ').strip().lower()#strip é importante para tirar os espaços.
    lista = ['não', 'nao', 'n']
    if opcao in lista :
        executar = False
    