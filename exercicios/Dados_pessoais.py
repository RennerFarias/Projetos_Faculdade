dados = {'nome': 'Elian',
         'idade': 19,
         'cidade': 'Lagoa Seca'}

def mostrar_dicionario(dicionario):
    print('=' * 34)
    dicionario_string = {str(k) : v for k, v in dicionario.items()}
    for item, valor in dicionario_string.items():
        print(f'{item.ljust(15)} -- {str(valor).rjust(15)}')

numeros = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

chave_verificar = 'idade'
if chave_verificar in dados:
    print(f'A chave {chave_verificar} existe')

frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha'
'''palavras = frase.split()
for posicao, palavra in enumerate(palavras):
    print(f'{palavra} -- {posicao}')'''



contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



