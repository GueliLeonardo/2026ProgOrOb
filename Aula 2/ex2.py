mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril' , 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] #Começa do 0
mes_numero = int(input("Digite o número do mês: "))
mes_numero -= 1

ptri = mes[:3]
stri = mes[3:6]
ttri = mes[6:9]
qtri = mes[9:12]
nomemes = mes[mes_numero]
if mes_numero >= 13 or mes_numero < 0:
    print("Número do mês inválido")
elif mes_numero <= 2:
    print("O mês é", nomemes, "e ele pertence ao primeiro trimestre do ano")
elif mes_numero <= 5:
    print("O mês é", nomemes, "e ele pertence ao segundo trimestre do ano")
elif mes_numero <= 8:
    print("O mês é", nomemes, "e ele pertence ao terceiro trimestre do ano")
else: 
    print("O mês é", nomemes, "e ele pertence ao quarto trimestre do ano")
