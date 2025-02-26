
numeros = []

while True:
    # verificação de entrada valida
    try:
        numero1 = int(input("Digite o 1º numero: "))
        numero2 = int(input("Digite o 2º numero: "))
        numero3 = int(input("Digite o 3º numero: "))
        break

    except ValueError:
        print("Digite apenas numeros")
        continue

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

numeros.sort()

print(f"O maior numero é: {numeros[2]}")
print(f"O menor numero é: {numeros[0]}")

numeros.sort(reverse=True)
print(numeros)