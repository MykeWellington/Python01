class Calculadora:
    def somar(self, *args):
        return sum(args)
    
    def multiplicar(self, *args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
            
    
calc = Calculadora()

print(calc.somar(5,6,7,8))
print(calc.multiplicar(5,6,7,8))