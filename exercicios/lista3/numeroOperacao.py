from time import sleep

def lerNumero(mensagem):
    '''
    Verifica se a entrada e valida
    :param mensagem: Mensagem a ser exibida para receber um numero
    :return: o numero lido
    '''
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada invalida!! Digite apenas numeros")

def lerOpcao(mensagem, primeiraOpcao, ultimaOpcao):
    '''
    Le a opcao que o usuario deseja

    :param mensagem: texto a ser exibido para ler o numero
    :param primeiraOpcao: define um valor minimo para receber a opcao
    :param ultimaOpcao:  Define um valor maximo para receber a opcao
    :return: A opcao verificada
    '''
    while True:
        try:
            opcao = int(input(mensagem))
            if primeiraOpcao <= opcao <= ultimaOpcao:
                return opcao
            else:
                print("Opcao invalida. Digite uma opcao valida")
                continue
        except ValueError:
            print("Entrada invalida!! Digite apenas numeros")

def propriedadesDoNumero(numero):
    '''
    Determina as propriedades do numero, identificando se ele e inteiro ou decimal, par ou impar, e positivo ou negativo
    :param numero: numero a ser analisado
    :return: uma string para cada propriedade correspondente
            - "inteiro" ou "decimal" (tipo do número)
            - "par" ou "ímpar" (se é par ou ímpar)
            - "positivo" ou "negativo" (seu sinal)
    '''
    valor = ""
    tipoNumero = ""
    sinal = ""

    valor = "inteiro" if int(numero) == numero else "decimal"
    tipoNumero = "par" if numero % 2 == 0 else "impar"
    sinal = "positivo" if numero > 0 else "negativo"

    return valor, tipoNumero, sinal


def exibirMenu():
    '''
    exibe um menu para o programa
    :return: O menu com as opcoes disponiveis para o usuario
    '''
    print("1) Adicao -> a + b\n"
          "2) Subtracao-> a - b\n"
          "3) Multiplicacao -> a * b\n"
          "4) Divisao -> a / b\n"
          "5) Exponenciacao -> a^b\n"
          "6) Radiciação -> Raiz de a por b\n"
          "7) Ler novos numeros\n"
          "8) Sair")

opcao = numero1 = numero2 = None
print("=" * 30)
numero1 = lerNumero("Digite o primeiro numero [a]: ".center(30))
numero2 = lerNumero("Digite o segundo numero [b]: ".center(30))
print("=" * 30)

while opcao != 8:
    sleep(0.5)
    print()
    exibirMenu()
    opcao = lerOpcao("Digite sua opcao: ", 1, 8)
    sleep(0.5)

    if opcao == 1:
        operador = "+"
        operacao = numero1 + numero2


    elif opcao == 2:
        operador = "-"
        operacao = numero1 - numero2

    elif opcao == 3:
        operador = "*"
        operacao = numero1 * numero2

    elif opcao == 4:
        operador = "/"
        operacao = numero1 / numero2

    elif opcao == 5:
        operador = "^"
        operacao = numero1 ** numero2


    elif opcao == 6:
        if numero2 == 0:
            print("Erro: Não é possível calcular a raiz com índice zero.")
            continue

        elif numero1 < 0 and numero2 % 2 == 0:
            print("Erro: Resultado seria um número complexo.")
            continue

        else:
            if numero2 < 0:
                print("Erro: Resultado seria um número complexo.")
                continue

            operacao = numero1 ** (1 / numero2)
            operador = "√"

    elif opcao == 7:
        numero1 = lerNumero("Digite o primeiro numero [a]: ")
        numero2 = lerNumero("Digite o segundo numero [b]: ")
        continue

    elif opcao == 8:
        print("Saindo do programa...")





    valor, tipoNumero, sinal = propriedadesDoNumero(operacao)
    if operador == "√":
        if numero2 == 2:
            print(f"√{numero1} = {operacao:.1f}")
        else:
            print(f"{int(numero2)}√{numero1} = {operacao:.1f}")

    else:
        print(f"{numero1} {operador} {numero2} = {operacao:.2f}")
    sleep(0.5)
    print(f"\n{operacao:.2f} e um numero {valor}, {tipoNumero}, {sinal}")
    sleep(0.5)

