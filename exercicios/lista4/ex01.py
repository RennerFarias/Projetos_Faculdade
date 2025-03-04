# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido.

entrada = input("Digite um número: ")
while not entrada.isdigit():
    print("Entrada inválida! Digite apenas números.")
    entrada = input("Digite um número: ")

numero = int(entrada)
print(numero)