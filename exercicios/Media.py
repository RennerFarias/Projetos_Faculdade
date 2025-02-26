# calculo de media aritmetica
import funcoes_muito_usadas
from funcoes_muito_usadas.Funcoes_uteis import titulo

titulo('Tabuada')

valores = []
while True:
    while True:
        try:
            valor = float(input('Digite um valor para calcular a media aritimetica total: '))
            valores.append(valor)
            print(f'Valor {valor} adicionado')
            break
        except ValueError:
            print('Digite apenas numeros')

    if len(valores) >= 2:
        parar = str(input('\nDeseja continuar inserindo valores? [S/N] ')).lower()
        if parar == 'n':
            break

media = sum(valores)/len(valores)

print('\nValores adicionados:', end=' ')
print(";".join(map(str, valores)))
print(f'\nA media aritmetica dos valores e {media}')

