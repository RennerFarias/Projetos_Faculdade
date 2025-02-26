from datetime import datetime
print('Classificacao de faixa etaria')

def geracao_de_nascimento(anos):
    '''
    Define a qual geracao o usuario pertence
    '''
    geracao = '  '
    ano_atual = datetime.now().year
    ano_nascimento = ano_atual - anos
    if 1946 <= ano_nascimento <= 1964:
        geracao = 'Baby Boomers'
    elif 1965 <= ano_nascimento <= 1980:
        geracao = 'Geracao X'
    elif 1981 <= ano_nascimento <= 1996:
        geracao = 'Geracao Y ou Millennials'
    elif 1997 <= ano_nascimento <= 2010:
        geracao = 'Geracao Z'
    else:
        geracao = 'Geracao Alfa'
    return geracao



# Garante que a entrada seja valida
while True:
    try:
        idade = int(input('Digite sua idade: '))
        break
    except ValueError:
        print('\033[31mEntrada invalida!\033[m. Digite apenas numeros')


geracao = geracao_de_nascimento(idade)

if 0 <= idade <= 12:
    print(f'Com {idade} anos de idade voce e uma crianca\nE pertence a geracao {geracao}')
elif 13 <= idade <= 18:
    print(f'Com {idade} ano, voce e um adolescente\nE pertence a geracao {geracao}')
else:
    print(f'Com {idade} anos, voce e um adulto\nE pertence a geracao {geracao}')
