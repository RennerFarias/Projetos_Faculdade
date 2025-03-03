
while True:
    try:
        numero = float(input("Digite um numero: "))
        break

    except ValueError:
        print("Digite apenas numeros")

valor = ""



if int(numero) == numero:
    valor = "inteiro"

else:
    valor = "decimal"

print(valor)