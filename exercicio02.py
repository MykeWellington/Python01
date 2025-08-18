# Calcular o quanto o cliente deve receber de troco

valor_compra = float(input('Qual o valor da compra? R$ '))
valor_pago = float(input('Valor pago pelo cliente: R$ '))

troco = valor_pago - valor_compra

print(f'O troco é: R$ {troco:.2f}')
