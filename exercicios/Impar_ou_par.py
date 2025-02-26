print('Numero Par ou Impar')

# Garante que a entrada seja valida
while True:
    try:
        numero = int(input('Escolha um numero: '))
        break
    except ValueError:
        print('Digite apenas numeros')

# Verifica se o numero e impar ou Par
if numero % 2 == 0:
    print(f'O numero {numero} e \033[1mPar\033[m')
else:
    print(f'O numero {numero} e \033[1mImpar\033[m')