'''• Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.'''


listaDeNumeros = []
impares = []
pares = []
for i in range(1, 11):
    while True:
        try:
            numero = int(input("Digite um numero: "))
            listaDeNumeros.append(numero)
            break
        except ValueError:
            print("Digite apenas numeros inteiros")

print("Numeros informados: ")
for numero in listaDeNumeros:
    print(numero, end=" ")
    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

print("\nNumeros pares informados: ")
for par in pares:
    print(par, end=" ")

print("\nNumeros impares informados: ")
for impar in impares:
    print(impar, end=" ")

