'''• Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:'''


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