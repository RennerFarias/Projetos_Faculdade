print("Turno Matutino [M]\n"
      "Turno Vespertino [V]\n"
      "Turno Noturno [N]\n")
while True:
    turno = input("Digite seu turno de estudo: [M / V / N] ").upper().strip()

    if turno not in "MVN":
        print("Valor Invalido!")
        continue

    else:
        break

if turno == "M":
    mensagem = "Bom dia!"

elif turno == "V":
    mensagem = "Boa tarde!"

else:
    mensagem = "Boa noite!"

print(f"{mensagem}")