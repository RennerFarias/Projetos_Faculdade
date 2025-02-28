numero = float(input("Digite um numero: "))
inteiroOuDecimal = round(numero, 0) == numero

if numero > 0:
    sinal = "positivo"

else:
    sinal = "negativo"


if inteiroOuDecimal:
    print(f"O numero {numero} e inteiro e e {sinal}")

else:
    print(f"O numero {numero} e decimal e e {sinal}")