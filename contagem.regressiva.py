import time
import os

# Programa: contagem_regressiva.py

# Solicita ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Exibe a contagem regressiva
    for i in range(numero, -1, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(i)
        time.sleep(1)
    print("Contagem regressiva finalizada!")
