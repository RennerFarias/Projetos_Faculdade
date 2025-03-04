opcao = 0
while opcao != 2:
    print("1) Inserir dados\n"
          "2) Sair")
    while True:
        try:
            opcao = int(input("Digite sua opcao: "))
            if 1 <= opcao <= 2:
                break
            else:
                print("Opcao invalida")
        except ValueError:
            print("Entrada invalida")



    if opcao == 1:
        while True:
            # Valida a entrada da populacao do pais A
            try:
                populacaoInicialA = int(input("Digite a populacao inicial do pais A: "))
                if populacaoInicialA > 0:
                    break
                else:
                    print("Entrada invalida!")
            except ValueError:
                print("Entrada invalida!")

        populacaoFinalA = populacaoInicialA

        while True:
            try:
                taxaCrescimentoA = float(input("Digite a taxa de crescimento do pais A, em porcentagem: "))
                break
            except ValueError:
                print("Entrada invalida")

        print("=" * 50)

        while True:
            try:
                populacaoInicialB = int(input("Digite a populacao inicial do pais B: "))
                if populacaoInicialB > 0:
                    break
                else:
                    print("Entrada invalida!")
            except ValueError:
                print("Entrada invalida!")

        populacaoFinalB = populacaoInicialB

        while True:
            try:
                taxaCrescimentoB = float(input("Digite a taxa de crescimento do pais B, em porcentagem: "))
                break
            except ValueError:
                print("Entrada invalida")

        print("=" * 50)

        anos = 0
        while populacaoFinalA < populacaoFinalB:
            populacaoFinalA = int(populacaoFinalA * (1 + taxaCrescimentoA/100))
            anos += 1
            populacaoFinalB = int(populacaoFinalB * (1+ taxaCrescimentoB/100))

        print(f"A população do país A ultrapassará ou igualará a população do país B em {anos} anos\n"
              f"A populacao inicial do pais A era {populacaoInicialA} a uma taxa de crecimento de {taxaCrescimentoA}%\n"
              f"A populacao inicial do pais B era {populacaoInicialB} a uma taxa de crescimento de {taxaCrescimentoB}%\n"
              f"Apos {anos} anos a populacao do pais A ira atingir {populacaoFinalA} e do pais B {populacaoFinalB}")

        print("=" * 50)

    elif opcao == 2:
        print("Saindo do programa")

    else:
        print("Opcao invalida")
