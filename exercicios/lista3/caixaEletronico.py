while True:
    print("Valor minimo de saque: 10 reais\n"
          "Valor maximo de saque: 600 reais")
    numero = int(input("Digite o valor a ser sacado: "))

    if 10 <= numero <= 600:
        break

    else:
        print("Valor invalido")
        continue

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

partes = []