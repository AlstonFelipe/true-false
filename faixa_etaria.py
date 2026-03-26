"""
1. Crie um programa em python que aponte a idade da pessoa e diga
 se ela é criança (0-12 anos), adolescente (13-17 anos),
 adulto jr (18-25), adulto (26-35), adulto sr (36-60), idoso (61+).

"""


idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você ainda é uma criança")
elif idade <= 17:
    print("Você é um adolescente? sera? ")
elif idade <= 25:
    print("Você é um adulto jr")
elif idade <= 35:
    print("Você é um adulto, ou acha que é")
elif idade <= 60:
    print("Você é um adulto sr, se não pisar na bola")
else:
    print("Você é um idoso, pode utilizar os bancos reservados")

