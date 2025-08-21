# Classe que representa a tabela do imposto de renda (IR)
class TabelaIR:
    def __init__(self): 
        #Lista de dicionários com as faixas salariais e valores
        self.tabela = [
            {'faixa': (0,1903.98), 'alíquota': 0, 'Dedução': 0},
            {'faixa': (1903.99,2826.68), 'alíquota': 7.5, 'Dedução': 142.80},
            {'faixa': (2826.66,3751.05), 'alíquota': 15, 'Dedução': 354.80},
            {'faixa': (3751.06,4664.68), 'alíquota': 22.5, 'Dedução': 636.13},
            {'faixa': (4664.69,float('inf')), 'alíquota': 27.5, 'Dedução': 869.36}
        ]
        
##Classe responsável por calcular o imposto com base na tabela

class CalculadorIr:
    def __init__(self, salarioBruto, tabelaIR):
        self.salarioBruto = salarioBruto
        self.tabelaIR = tabelaIR
        
    def calcular(self):
        imposto = 0 #inicializa o imposto com zero
        # percorre cada faixa da tabela
        for faixa in self.tabelaIR.tabela:
            if self.salarioBruto > faixa['faixa'][0] and self.salarioBruto <= faixa ['faixa'][1]:
                imposto = (self.salarioBruto * faixa ['alíquota']) / 100 - faixa['Dedução']
                break
        return imposto
# Cria uma instância da tabela de IR
tabelaIR = TabelaIR()
#Pedindo o salário bruto do usuário
salarioBruto = float(input('Informe o seu salário bruto:\n (Apenas números):  '))

# Cria uma calculadora de IR com o S
calculadora = CalculadorIr(salarioBruto,tabelaIR)

#Calcula o imposto devido

imposto = calculadora.calcular()

print(f'O imposto de renda devido é de R$ {imposto:.2f}!')