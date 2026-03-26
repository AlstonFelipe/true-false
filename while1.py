"""1.Crie
um programa que solicite ao usuário uma nota entre zero e dez. Se o valor
informado for inválido, exiba uma mensagem de erro e continue solicitando uma
nota válida até que o usuário a forneça."""

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota > 0 and nota >= 10:
    nota = float(input("voce errou, digite uma nota entre 0 e 10: "))
print(f"Voce digitou a nota {nota}")