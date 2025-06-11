import random

class Animal:
    def emitir_som(self):
        raise NotImplementedError("Método emitir_som deve ser implementado pelas subclasses")

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
    
    def __str__(self):
        return "Cachorro"

class Galinha(Animal):
    def emitir_som(self):
        return "Cacarejo"
    
    def __str__(self):
        return "Galinha"

class Cavalo(Animal):
    def emitir_som(self):
        return "Relincha"
    
    def __str__(self):
        return "Cavalo"

# Função para demonstrar o polimorfismo
def fazer_barulho(animal):
    print(f"{animal} faz: {animal.emitir_som()}")

# Criando instâncias dos animais
animais = [Cachorro(), Galinha(), Cavalo()]

# Demonstração do polimorfismo
for animal in animais:
    fazer_barulho(animal)

