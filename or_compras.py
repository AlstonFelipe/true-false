# or quando umas das condições for verdadeira

#print(10>=5 or 10<5)
#print(10>==5 or 10<5)

camiseta = 580.50
calca = 690.90
saldo = 500.00
credito = 1000.00
total = saldo+credito

opcao_compras = input("1. Camiseta\n 2. Calça")
# forma_pagamento = input("1. Débito \n 2. Crédito")

if (opcao_compras == "1"):
    if(saldo >= camiseta or credito >= camiseta or total >= camiseta):
        print("parabéns pela compra !")

elif (opcao_compras == "2"):
    if (saldo >= calca or credito >= calca or total >=calca):
        print("parabéns pela compra !")