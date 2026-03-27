"""Desenvolva um programa em Python que solicite 
a quantidade de pessoas a serem cadastradas 
em um evento e, para cada uma, peça a idade e se 
possui convite (1 para sim e 0 para não), aplicando 
as regras de que menores de 16 anos não entram, 
pessoas entre 16 e 17 anos só entram com convite e 
maiores de 18 anos entram com ou sem convite, e ao 
final informe quantas pessoas entraram, quantas foram 
barradas e quantas entraram sem convite.
"""


quantidade = int(input("Quantas pessoas? "))
entraram = 0
barradas = 0
sem_convite = 0

contagem = 0

while contagem < quantidade:
    idade = int(input("Digite a idade: "))
    convite = int(input("Tem convite? (1=sim, 0=nao): "))

    if idade < 16:
        barradas = barradas + 1

    elif idade < 18:
        if convite == 1:
            entraram = entraram + 1
        else:
            barradas = barradas + 1

    else:
        entraram = entraram + 1
        if convite == 0:
            sem_convite = sem_convite + 1

    contagem = contagem + 1

print("Entraram:", entraram)
print("Barradas:", barradas)
print("Entraram sem convite:", sem_convite)






