# Função principal do programa
def main():
    # Cria uma lista vazia para armazenar os nomes
    nomes = []

    # Solicita ao usuário para inserir nomes
    print("Digite um nome por vez. Para terminar, digite 'fim':")

    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == 'fim':
            break
        if nome:  # Adiciona o nome apenas se não for uma string vazia
            nomes.append(nome)

    # Ordena a lista de nomes em ordem alfabética
    nomes.sort()

    # Exibe a lista de nomes em ordem alfabética
    print("\nLista de nomes em ordem alfabética:")
    for nome in nomes:
        print(nome)

    # Exibe o número total de nomes digitados
    print(f"\nNúmero de nomes digitados: {len(nomes)}")

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
