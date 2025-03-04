'''• Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
por eles.
• Altere o programa anterior para mostrar no final a soma dos números'''



n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
print(f"Os numeros inteiros entre {n1} e {n2} e: ")
soma = 0
for n in range(n1, n2+1):
    print(n, end=" ")
    soma += n

print(f"A soma entre os numeros e {soma}")