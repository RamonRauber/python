import numpy as np
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
    
    @abstractmethod
    def calcular_custo(self):
        pass

class Carro(Veiculo):
    def calcular_custo(self):
        return self.distancia * 0.5
    
    def __str__(self):
        return "Carro"

class Bicicleta(Veiculo):
    def calcular_custo(self):
        return self.distancia * 0.1
    
    def __str__(self):
        return "Bicicleta"

class Caminhao(Veiculo):
    def calcular_custo(self):
        return self.distancia * 1.0
    
    def __str__(self):
        return "Caminhão"

# Criando instâncias dos veículos com distância 200
veiculos = [Carro(200), Bicicleta(200), Caminhao(200)]

# Calculando os custos usando polimorfismo
custos = np.array([veiculo.calcular_custo() for veiculo in veiculos])

# Exibindo os resultados
print("Custos de transporte para 200 km:")
for veiculo, custo in zip(veiculos, custos):
    print(f"{veiculo}: R${custo:.2f}")

print("\nArray NumPy com os custos:")
print(custos)