def divisao(a, b):
    try:#tenta efetuar a divisão
        resultado = a / b
        print(f'O resultado da divisão de  {a} por {b} é: {resultado}')
    except ZeroDivisionError: #Se houver um erro de divisão por zero, o codigo entra dentro do except e é executado.
        print('Erro: Não é possível dividir por zero')
        
    except TypeError: #Caso algum valor não seja um número, esse except será executado.
        print('Erro: Ambos os valores precisam ser número')
        
    except Exception as erro: # Esse elemento captura qualquer outro erro que não tenha sido tratado nos anteriores.
        print(f'Erro inesperado: {erro}')
    else: # O bloco else é executado se o codigo dentro do try for bem sucedido (sem erros)
        print('Operação realizada com sucesso!')
    finally: #O bloco finally sempre é executado, independente do cenário (erro ou sucesso)
        print('Processo de divisão finalizado')
        
# Teste 01: Divisão normal.
divisao (10, 2)
# Teste 02: Divisão por 0.
divisao (10, 0)
# Teste 03: Divisão com tipos inválidos
divisao (10, '2')
# Teste 04: Divisão com erro inesperado
divisao (0.9, 2)