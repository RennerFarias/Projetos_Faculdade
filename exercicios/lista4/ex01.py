entrada = input("Digite um número: ")
while not entrada.isdigit():
    print("Entrada inválida! Digite apenas números.")
    entrada = input("Digite um número: ")

numero = int(entrada)
print(numero)