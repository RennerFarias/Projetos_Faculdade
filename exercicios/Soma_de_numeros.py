from math import radians
from random import randint

numeros = []
for i in range(1, 6):
    numeros.append(randint(1, 100))

soma_dos_numeros = 0
for numero in numeros:
    soma_dos_numeros += numero

print(f'Lista de numeros aleatorios gerados: ')
for n in numeros:
    print(n, end='  ')
print(f'\nA soma de todos os numeros e igual a {soma_dos_numeros}')
