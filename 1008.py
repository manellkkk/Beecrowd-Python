nome = input()
salarioFixo = float(input())
valorEmVendas = float(input())

salarioTotal = salarioFixo + (valorEmVendas * 0.15)

print("TOTAL = R$ {:.2f}".format(salarioTotal))