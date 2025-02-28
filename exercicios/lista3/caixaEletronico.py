while True:
    print("Valor minimo de saque: 10 reais\n"
          "Valor maximo de saque: 600 reais")

    # Solicita o valor do Saque
    valor = int(input("Digite o valor a ser sacado: "))

    # Verifica se o valor do saque esta dentro do limite permitido
    if 10 <= valor <= 600:
        break

    else:
        print("Valor invalido")
        continue

# Notas disponiveis para saque
notasDisponiveis = [200, 100, 50, 20, 10, 5, 1]
quantidadeDeNotas = {}

# Calculo da quantidade de notas necessarias
for nota in notasDisponiveis:
    if valor >= nota:
        quantidadeDeNotas[nota] = valor // nota
        valor %= nota

# Exibe o resultado
print("Notas fornecidas: ")
for nota, quantidadeDeNotas in quantidadeDeNotas.items():
    print(f"{quantidadeDeNotas} nota(s) de R${nota}")