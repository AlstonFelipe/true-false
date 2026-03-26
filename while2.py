"""2.Desenvolva
um programa que calcule e exiba a média aritmética 
de N notas fornecidas pelo usuário.
"""

notas = 0
contagem = 0
nota = 0

while nota != -1:
        nota = float(input("Digite uma nota (ou -1 para sair): "))
        contagem = contagem + 1
        notas = notas + nota
        
media = notas/contagem
print(f"A média aritmética das notas é: {media}")
