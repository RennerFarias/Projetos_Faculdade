def exibirMenu():
    # Exibi um menu personalizado do programa
    print("\033[33m=" * 30)
    print("Verificador de ano Bissexto".center(30))
    print("=" * 30, "\033[m")

exibirMenu()
while True:
    try:
        ano = int(input("Digite o ano para saber se ele é bissexto: "))
        break

    except ValueError:
        print("\033[31mValor invalido, digite um ano valido!\033[m")
        continue

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")

else:
    print(f"O ano {ano} não é bissexto")