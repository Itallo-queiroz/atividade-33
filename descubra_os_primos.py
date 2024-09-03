# Função para verificar se um número é primo
def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Lista com números de 1 a 20
numeros = list(range(1, 21))

# Verificar e imprimir quais números são primos
primos = [num for num in numeros if primo(num)]

print("Os números primos de 1 a 20 são:", primos)
