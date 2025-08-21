class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.buzina = 'Biiiiii!'
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O {self.modelo} acelerou para {self.velocidade} Km/h')
        
           
    def parar(self):
        self.velocidade = 0
        print(f'O {self.modelo} parou.')
        
    def buzinar(self):
        self.buzina
        print(f'O {self.modelo} {self.buzina}!')
        
    def desacelerar(self, decremento):
        if self.velocidade - decremento <= 0:
            self.velocidade = 0
        else:
            self.velocidade -= decremento
            print(f'O {self.modelo} reduziu para {self.velocidade} KM/h')
        
# Criando um objeto carro
meu_carro = Carro('Amarelo', 'Fusca')
carro_visita = Carro('Marrom', 'Ford Bronco 1986')

meu_carro.acelerar(20)
meu_carro.acelerar(30)
meu_carro.parar()

carro_visita.acelerar(30)
carro_visita.acelerar(80)
carro_visita.desacelerar(100)
carro_visita.parar()
carro_visita.buzinar()

carros = [
    Carro('Cinza', 'Jimny' ),
    Carro('Cinza', 'Ford Bronco' ),
    Carro('Cinza', 'Lamb Urus' ),
    Carro('Cinza', 'Fox' ),
    Carro('Cinza', 'Gol quadrado' ),
    Carro('Cinza', 'MB Classe G' ),
    
]

for carro in carros:
    carro.acelerar(50)
    carro.desacelerar(40)
    carro.buzinar()
    carro.parar()