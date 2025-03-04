while True:
    try:
        base = int(input("Digite a base: "))
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

while True:
    try:
        expoente = int(input("Digite o expoente: "))
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

resultado = 1
for n in range(1, expoente + 1):
    resultado *= base

print(resultado)