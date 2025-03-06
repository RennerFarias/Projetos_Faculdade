import time

filmes = ['Oppenheimer' , 'Doctor Who' , 'Corra']
filmes_alugados = []

def listar_filmes():
    if filmes:
        print('Filmes disponíveis:')
        for i, filme in enumerate(filmes, start=1):
            print(f'{i} - {filme}')
            time.sleep(0.3)
    else:
        print('Nenhum filme disponível no momento.')

def alugar_filme():
    if not filmes:
        print('Nenhum filme disponível para alugar.')
    else:
        listar_filmes()
        numero = input('Digite o número do filme que deseja alugar: ')
        if numero.isdigit():
            numero = int(numero)
            if 1 <= numero <= len(filmes):
                filme = filmes.pop(numero - 1)
                filmes_alugados.append(filme)
                print(f'Filme {filme} alugado com sucesso')
            else:
                print('Número inválido. Escolha um filme da lista.')
        else:
            print('ERRO. DIGITE APENAS NÚMEROS')

def devolver_filme():
    if not filmes_alugados:
        print('Nenhum filme alugado para devolver.')
        return
    
    print('Filmes alugados:')
    for i, filme in enumerate(filmes_alugados, start=1):
        print(f'{i} - {filme}')
    
    numero = input('Digite o número do filme que deseja devolver: ')
    if numero.isdigit():
        numero = int(numero)
        if 1 <= numero <= len(filmes_alugados):
            filme = filmes_alugados.pop(numero - 1)
            filmes.append(filme)
            print(f'Filme {filme} devolvido com sucesso')
        else:
            print('Número inválido. Escolha um filme da lista de filmes alugados.')
    else:
        print('ERRO. DIGITE APENAS NÚMEROS')


def adicionar_filme():
    filme = input('Digite o nome do filme que deseja adicionar: ').strip().title()
    filmes.append(filme)
    print(f'Filme {filme} adicionado com sucesso')

def menu():
    while True:
        print('=' * 30)
        print('Locadora'.center(30))
        print('=' * 30)
        print('1 - Listar filmes')
        print('2 - Alugar filme')
        print('3 - Devolver filme')
        print('4 - Adicionar filme')
        print('5 - Sair')

        opcao = input('Digite sua opção: ')
        time.sleep(0.5)

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                listar_filmes()
            elif opcao == 2:
                alugar_filme()
            elif opcao == 3:
                devolver_filme()
            elif opcao == 4:
                adicionar_filme()
            elif opcao == 5:
                print('Programa encerrado com sucesso')
                break
            else:
                print('Opção inválida! Escolha entre 1 e 5.')
        else:
            print('ERRO. DIGITE APENAS NÚMEROS')
        time.sleep(1)

if __name__ == '__main__':
    menu()