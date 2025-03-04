print("Tabuada")
print("=" * 30)

while True:
    try:
        numero = int(input("Digite um numero para ver sua tabuada: "))
        break
    except ValueError:
        print("ERRO! Digite apenas numeros inteiros")

for n in range(1, 11):
    valor = numero * n
    print(f"{numero} x {n} = {valor}")