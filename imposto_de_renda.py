def calculadoraIR(salarioBruto):
    tabelaIr = [
        {'faixa': (0,1903.98), 'alíquota': 0, 'Dedução': 0},
        {'faixa': (1903.99,2826.68), 'alíquota': 7.5, 'Dedução': 142.80},
        {'faixa': (2826.66,3751.05), 'alíquota': 15, 'Dedução': 354.80},
        {'faixa': (3751.06,4664.68), 'alíquota': 22.5, 'Dedução': 636.13},
        {'faixa': (4664.69,float('inf')), 'alíquota': 27.5, 'Dedução': 869.36}
        
    ]
    
    imposto = 0
    for faixa in tabelaIr:
        if salarioBruto > faixa['faixa'][0] and salarioBruto <= faixa['faixa'][1]:
            imposto = (salarioBruto * faixa['alíquota']) / 100 - faixa['Dedução']
            break
        
    return imposto

salarioBruto = float(input('Informe seu salário bruto: '))
imposto = calculadoraIR(salarioBruto)
liquido = salarioBruto - imposto
print(f'O imposto de renda devido é de R$ {imposto:.2f}!')
print(f'O seu salário liquido é de {liquido}')