while True:
    try:
        numero = int(input("Digite um numero inteiro para calcular seu fatorial: "))
        if numero > 0:
            break
        else:
            print("Digite um numero maior que 0")
    except ValueError:
        print("ERRO! Digite apenas numeros inteiros")

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(fatorial)