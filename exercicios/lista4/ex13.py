'''• Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.'''




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