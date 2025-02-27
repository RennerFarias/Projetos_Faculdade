while True:
    numero = int(input("Digite um numero menor que 1000: "))

    if 0 < numero < 1000:
        break

    else:
        continue

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

partes = []
if centenas > 0 :
    partes.append(f"{centenas} centena" + ("s" if centenas > 1 else ""))

if dezenas > 0:
    partes.append(f"{dezenas} dezena" + ("s" if dezenas > 1 else ""))

partes.append(f"{unidades} unidade" + ("s" if unidades > 1 else ""))

for parte in partes:
    print(parte)