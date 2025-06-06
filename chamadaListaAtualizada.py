import random

# --- CLASSE 1: Alunos (Nomes e Estados Aleatórios) ---
class Alunos:
    def __init__(self):
        self.lista_alunos = [
            "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo",
            "Helena", "Igor", "Julia", "Kaique", "Larissa", "Marcos", "Natália",
            "Otávio", "Patrícia", "Rafael", "Sofia", "Thiago", "Vanessa", "William", "Yasmin", "Zé"
        ]
        self.estados = ["ativo", "transferido", "expulso"]
        self.estado_alunos = {}
        
        for indice in range(len(self.lista_alunos)):
            self.estado_alunos[indice] = random.choice(self.estados)
    
    def mostrar_alunos(self):
        for i, nome in enumerate(self.lista_alunos):
            print(f"{nome} ({self.estado_alunos[i]})")

# --- CLASSE 2: Notas (Gestão de Notas Aleatórias) ---
class Notas:
    def __init__(self, total_alunos=23):
        self.notas_alunos = {}
        self.gerar_notas_aleatorias(total_alunos)
    
    def gerar_notas_aleatorias(self, total_alunos):
        for indice in range(total_alunos):
            self.notas_alunos[indice] = [round(random.uniform(0, 10), 1) for _ in range(4)]
    
    def adicionar_nota(self, indice_aluno, nota):
        if 0 <= nota <= 10:
            if indice_aluno not in self.notas_alunos:
                self.notas_alunos[indice_aluno] = []
            self.notas_alunos[indice_aluno].append(nota)
            print(f"✅ Nota {nota} adicionada ao aluno {indice_aluno + 1}.")
        else:
            print("❌ Nota inválida! Deve ser entre 0 e 10.")
    
    def mostrar_notas(self):
        for indice, notas in self.notas_alunos.items():
            media = sum(notas) / len(notas)
            print(f" Notas = {notas} | Média = {media:.1f}")

# --- CLASSE 3: Chamada (Números da Chamada) ---
class Chamada:
    def __init__(self):
        self.numeros_chamada = tuple(range(1, 24))
    
    def mostrar_chamada(self):
        print("Números da chamada:", self.numeros_chamada)

# --- EXECUÇÃO ---
print("===== SISTEMA DE ALUNOS =====")
alunos = Alunos()
notas = Notas()
chamada = Chamada()

print("\n--- ALUNOS E ESTADOS ---")
alunos.mostrar_alunos()

print("\n--- NOTAS ALEATÓRIAS ---")
notas.mostrar_notas()

print("\n--- CHAMADA ---")
chamada.mostrar_chamada()

# Adicionar nota (sem mostrar a lista novamente)
print("\n--- ADICIONAR NOTA ---")
notas.adicionar_nota(0, 8.5)  # Exemplo: Adiciona 8.5 ao aluno 1 (Ana)