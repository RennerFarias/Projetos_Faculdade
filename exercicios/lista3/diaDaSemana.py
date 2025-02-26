diasSemana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]

dia = int(input("Digite um numero para saber o dia correspondente da semana: "))

if dia > 7:
    dia = (dia % 7)


print(f" o número {dia} corresponde ao dia {diasSemana[dia - 1]}")
