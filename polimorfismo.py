# Classe base (superclasse) que representa o animal
class Animal:
    def fazerSom(self):
        # Metodo generico que será sobrescrito pelas subclasses
        # O uso do pass indica que não há implementações aqui
        pass
    
class Cachorro(Animal):
    def fazerSom(self):
        #implementação específica para cachorro
        return 'Au au!'
    
class Gato(Animal):
    def fazerSom(self):
        #implementação especifica para gato
        return 'Miauuu!'
    
class Galinha(Animal):
    def fazerSom(self):
        #implementação especifica para a galinha
        return 'có có có có'
    
class Vaca(Animal):
    def fazerSom(self):
        return 'Muuuu'

#Função que recebe qualquer objeto do tipo animal (ou subclasse)
# E chama o metodo fazerSom() - uso efetivo do polimorfismo  
def fazerAnimalFalar(animal:Animal):
    print(animal.fazerSom())
    
#Criando objetos
cachorro = Cachorro()
gato = Gato()
galinha = Galinha()
vaca = Vaca()

#Chama o metodo de cada animal de forma polimorfica
fazerAnimalFalar(cachorro)
fazerAnimalFalar(gato)
fazerAnimalFalar(galinha)
fazerAnimalFalar(vaca)

animais = [
    Cachorro(), Gato(), Galinha(), Vaca()
]

for animal in animais:
    fazerAnimalFalar(animal)