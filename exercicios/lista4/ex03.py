'''Faça um programa que leia e valide as seguintes informações:
• Nome: maior que 3 caracteres;
• Idade: entre 0 e 150;
• Salário: maior que zero;
• Sexo: 'f' ou 'm';
• Estado Civil: 's', 'c', 'v', 'd’;
'''




nome = input("Digite seu nome: ")
while len(nome) < 3:
    nome = input("Digite seu nome: ")

print("=" * 30)

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 < idade <= 150:
            break
        else:
            print("Idade invalida.")
    except ValueError:
        print("Entrada invalida")
        continue

print("=" * 30)

while True:
    try:
        salario = float(input("Digite seu salario. Ele deve ser maior que 0: "))
        if salario > 0:
            break

        else:
            print("Salario invalido")

    except ValueError:
        print("Entrada invalida")

print("=" * 30)

sexo = input("digite seu sexo [F / M]: ").upper().strip()
while sexo not in "FM":
    sexo = input("digite seu sexo [F / M]: ").upper().strip()

if sexo == "F":
    sexo = "feminino"

else:
    sexo = "masculino"

print("=" * 30, "\nEstado civil")
print("[s] - Solteiro(a)\n"
      "[c] - Casado(a)\n"
      "[v] - Viuvo(a)\n"
      "[d] - divorciado(a)")

estadoCivil = input("Digite seu estado civil: ").lower().strip()
while estadoCivil not in "scvd":
    estadoCivil = input("Digite seu estado civil: ")

if estadoCivil == "s":
    estadoCivil = "Solteiro(a)"

elif estadoCivil == "c":
    estadoCivil = "Casado(a)"

elif estadoCivil == "v":
    estadoCivil = "Viuvo(a)"

elif estadoCivil == "d":
    estadoCivil = "Divorciado(a)"


print(f"{nome}, {idade} anos, {sexo}, {estadoCivil}")