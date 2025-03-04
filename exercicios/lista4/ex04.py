


populacaoInicialA = 80000
taxaCrescimentoA = 1.03
populacaoFinalA = populacaoInicialA

populacaoInicialB = 200000
taxaCrescimentoB = 1.015
populacaoFinalB = populacaoInicialB

anos = 0
while populacaoFinalA < populacaoFinalB:
    populacaoFinalA = int(populacaoFinalA * taxaCrescimentoA)
    anos += 1
    populacaoFinalB = int(populacaoFinalB * taxaCrescimentoB)

print(f"A população do país A ultrapassará ou igualará a população do país B em {anos} anos\n"
      f"A populacao inicial de A era {populacaoInicialA} e a do pais B era {populacaoInicialB}\n"
      f"Apos {anos} anos a populacao do pais A ira atingir {populacaoFinalA} e do pais B {populacaoFinalB}")

