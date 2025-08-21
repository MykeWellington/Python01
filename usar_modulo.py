import operacoes
import meu_modulo

print(operacoes.somar(2,5))
print(meu_modulo.saudacao('Myke'))
print(meu_modulo.despedida('Myke'))

try: 
    print(operacoes.dividir(10,0))
    
except ValueError as erro:
    print(f'Erro ao dividir por zero {erro}')
    


 