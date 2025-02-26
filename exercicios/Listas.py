numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Elian', 'Davi', 'Ezequiel', 'Alberto']
ano = [2005, 2024]

for i in nomes:
    print(i, end = ' ')

soma_impares = 0
for n in numeros:

    if n % 2 != 0:
        soma_impares += n

print(soma_impares)

lista_decrescente = sorted(numeros, reverse=True)
for i in lista_decrescente:
    print(i, end = ' ')

