from funcoes_muito_usadas.Funcoes_uteis import titulo

titulo('Descobrindo o quadrante que um ponto esta')
coordenada_x = float(input('Digite o valor de X: '))
coordenada_y = float(input('Digite o valor de Y: '))

# Determina a qual quadrante o ponto percence
if coordenada_x > 0 and coordenada_y > 0:
    print(f'O ponto ({coordenada_x}, {coordenada_y}) se encontra no 1 quadrante')
elif coordenada_x < 0 and coordenada_y > 0:
    print(f'O ponto({coordenada_x}, {coordenada_y}) se encontra no 2 quadrante')
elif coordenada_x < 0 and coordenada_y < 0:
    print(f'O ponto ({coordenada_x, coordenada_y}) se encontra no 3 quadrante')
else:
    print(f'O ponto ({coordenada_x}, {coordenada_y}) se encontra no 4 quadrante')
