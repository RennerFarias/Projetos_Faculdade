from time import sleep

temperaturaConvertida = opcao = simbolo = None

def exibirMenu():
    print("=" * 30)
    print("Convertor de temperaturas".center(30))
    print("=" * 30)
    sleep(1)
    print("Opcao 1 - Celsius → Kelvin\n"
        "Opcao 2 - Celsius → Fahrenheit\n"
        "Opcao 3 - Fahrenheit → Celsius\n"
        "Opcao 4 - Fahrenheit → Kelvin\n"
        "Opcao 5 - Kelvin → Celsius\n"
        "Opcao 6 - Kelvin → Fahrenheit\n"
        "Opcao 7 - Sair do Programa")


def celsiusParaFahrenheit(valor):
    temperaturaConvertida = valor * 1.8 + 32
    return temperaturaConvertida

def celsiusParaKelvin(valor):
    temperaturaConvertida = valor + 273
    return temperaturaConvertida

def fahrenheitParaCelsius(valor):
    temperaturaConvertida = (valor - 32) / 1.8
    return temperaturaConvertida

def fahrenheitParaKelvin(valor):
    temperaturaConvertida = (valor - 32) * 5/9 + 273
    return temperaturaConvertida

def kelvinParaCelsius(valor):
    temperaturaConvertida = valor - 273
    return temperaturaConvertida

def kelvinParaFahrenheit(valor):
    temperaturaConvertida = (valor - 273) * 1.8 + 32
    return temperaturaConvertida

# Loop Principal
while True:
    exibirMenu()

    try:
        opcao = int(input("Digite sua Opcao: "))
        if opcao not in range(1, 8):
            print('\033[31mOpcao inválido! Escolha uma opcao valida.\033[m')
            continue
        sleep(0.5)

    except ValueError:
        print("ERRO. Digite apenas numeros. ")
        continue



    if opcao == 1 or opcao == 2:
        simbolo = "°C"

    elif opcao == 3 or opcao == 4:
        simbolo = "F"

    elif opcao == 5 or opcao == 6:
        simbolo = "K"

    elif opcao == 7:
        print("Programa encerrado")
        break

    else:
        print('\033[31mOpcao inválido! Escolha uma opcao valida.\033[m')
        continue

    try:
        temperatura = float(input(f"Digite a temperatura que deseja converter({simbolo}): "))
        sleep(0.5)
    except ValueError:
        print('\033[31mERRO. Digite apenas números.\033[m')
        continue

    if opcao == 1:
        temperaturaConvertida = celsiusParaKelvin(temperatura)

    elif opcao == 2:
        temperaturaConvertida = celsiusParaFahrenheit(temperatura)

    elif opcao == 3:
        temperaturaConvertida = fahrenheitParaCelsius(temperatura)

    elif opcao == 4:
        temperaturaConvertida = fahrenheitParaKelvin(temperatura)

    elif opcao == 5:
        temperaturaConvertida = kelvinParaCelsius(temperatura)

    elif opcao == 6:
        temperaturaConvertida = kelvinParaFahrenheit(temperatura)

    elif opcao == 7:
        print("Saindo do programa...")
        break

    else:
        print('\033[31mOpção inválida! Escolha entre 1 e 7.\033[m')

    print(f"Temperatura Convertida: {temperaturaConvertida:.2f} {simbolo}")
    sleep(1)

