n1 = float(input("Digite um numero: "))
n2 = float(input("Digite mais um numero: "))
n3 = float(input("Digite mais um numero: "))
n4 = float(input("Digite mais um numero: "))
n5 = float(input("Digite mais um numero: "))

listaDeNumeros = [n1, n2, n3, n4, n5]
listaDeNumeros.sort()
soma = 0

for numero in listaDeNumeros:
    soma += numero

media = soma / 5

print(f"O maior numero informado e {listaDeNumeros[4]}")
print(f"A soma entre eles e {soma}")
print(f"A media entre eles e {media}")

