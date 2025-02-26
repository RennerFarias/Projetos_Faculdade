from funcoes_muito_usadas import Funcoes_uteis
from funcoes_muito_usadas.Funcoes_uteis import verificar_entrada_float
from time import sleep

Funcoes_uteis.titulo('Tabuada')

numero = verificar_entrada_float('Digite o numero que deseja ver a tabuada')

for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}', end='  ')

while True:
    try:
        continuar = str(input(f'\nDeseja ver a tabuada de 11 ate 20 do numero {numero}? '
                          f'"s" para sim, "n" para nao ')).strip().lower()
        if continuar in {'s', 'n'}:
            break
        else:
            continue
    except ValueError:
        print('Entrada invalida')

if continuar == 's':
    for i in range(11, 21):
        print(f'{numero} * {i} = {numero * i}', end='  ')
    print('Programa encerrado')
else:
    print('Programa encerrado')

