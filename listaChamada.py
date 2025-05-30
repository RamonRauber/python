from functools import reduce


# Lista de alunos: [número, nome, [notas]]
turma = [
    [15, "Luis Eduardo", [7.5, 8.0, 6.5]],
    [7, "Heloysa Sandaka", [9.0, 8.5, 7.0]],
    [3, "Eduardo", [6.0, 5.5, 7.5]],
    [22, "Ruan Ricardo", [8.5, 9.5, 10.0]],
    [10, "Kaua Hellmann", [5.0, 6.5, 7.0]],
    [1, "Alexandre", [9.5, 9.0, 8.5]],
    [18, "Marcus", [4.5, 5.0, 6.0]],
    [5, "Gustavo Barbosa", [8.0, 7.5, 9.0]],
    [12, "Luan Viera", [6.5, 7.0, 7.5]],
    [23, "Vitor Hugo", [10.0, 9.5, 9.0]],
    [9, "José Gabriel", [5.5, 6.0, 6.5]],
    [4, "Gidean", [7.0, 8.5, 9.0]],
    [20, "Murilo", [6.0, 5.0, 7.0]],
    [11, "Leonardo", [8.5, 9.0, 7.5]],
    [2, "Bill Vaz", [4.0, 5.5, 6.0]],
    [17, "Luis Henrique Mattos", [9.0, 8.0, 9.5]],
    [6, "Gustavo de Almeida", [7.5, 6.5, 8.0]],
    [14, "Lucas Matheus", [6.0, 7.5, 7.0]],
    [8, "Isabela", [5.5, 6.0, 5.0]],
    [19, "Millena", [8.0, 9.5, 7.5]],
    [13, "Lucas Kruger", [4.5, 5.0, 6.5]],
    [21, "Ramon", [7.0, 8.0, 9.0]],
    [16, "Luis Henrique Kubaski", [5.0, 6.5, 7.0]],
]






# Função para calcular média
def calcular_media(notas):
    return reduce(lambda a, b: a + b, notas) / len(notas)

# Função para ordenar por nome (ordem alfabética)
def ordenar_por_nome(turma):
    return sorted(turma, key=lambda aluno: aluno[1].lower())  # Ignora maiúsculas/minúsculas

# Função para exibir a turma
def exibir_turma(turma, titulo="RELATÓRIO DA TURMA"):
    print(f"\n=== {titulo} ===")
    for aluno in turma:
        numero, nome, notas = aluno
        media = calcular_media(notas)
        print(f"Nº {numero:2d}: {nome:22} | Notas: {notas} | Média: {media:.2f}")

# Exibir turma ordenada por número (original)
exibir_turma(sorted(turma, key=lambda x: x[0]), "TURMA ORDENADA POR NÚMERO E POR ORDEM ALFABETICA")



