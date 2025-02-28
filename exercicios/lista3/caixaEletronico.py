while True:
    print("Valor minimo de saque: 10 reais\n"
          "Valor maximo de saque: 600 reais")
    valor = int(input("Digite o valor a ser sacado: "))

    if 10 <= valor <= 600:
        break

    else:
        print("Valor invalido")
        continue

total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1

    else:
        if totalced > 0:
            print(f"Total de {totalced} cedulas de R${ced}")
        if ced == 100:
            ced = 50
            totalced = 0

        elif ced == 50:
            ced = 20
            totalced = 0

        elif ced == 20:
            ced = 10
            totalced = 0

        elif ced == 10:
            ced = 5
            totalced = 0

        elif ced == 5:
            ced = 1
            totalced = 0

        if total == 0:
            break
