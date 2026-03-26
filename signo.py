"""
2.  Crie um programa em python que aponte o signo da pessoa
 referente ao dia e mês de nascimento.
"""


dia = int(input("Digite o dia que vc nasceu: "))
mes = int(input("Digite o mês que vc nasceu: "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    
    print("Seu signo deve ser Aquário")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("Seu signo deve ser Peixes")
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print("Seu signo deve ser Áries")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("Seu signo deve ser Touro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("Seu signo deve ser Gêmeos")
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    print("Seu signo deve ser Câncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print("Seu signo deve ser Leão")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print("Seu signo deve ser Virgem")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print("Seu signo deve ser Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Seu signo deve ser Escorpião")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Seu signo deve ser Sagitário")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print("Seu signo deve ser Capricórnio")
else:
    print("Verifique a data que vc digitou")