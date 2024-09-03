# Lista de nomes
nomes = [
    "Itallo",
    "Bruno",
    "Carla",
    "Daniel",
    "Eduarda",
    "Felipe",
    "Girona",
    "Cleitin",
    "Isabella",
    "João"
]

# Solicita ao usuário que informe um índice
indice = int(input("Informe um número inteiro equivalente ao índice (0-9): "))

# Verifica se o índice está dentro do intervalo válido
if 0 <= indice < len(nomes):
    # Retorna o nome correspondente ao índice informado
    nome = nomes[indice]
    print(f"O nome no índice {indice} é {nome}.")
else:
    print("Índice inválido. Por favor, informe um número entre 0 e 9.")
