"""3.Desenvolva um programa que calcule a média de alunos por 
turma. Para isso, siga os passos abaixo:

Solicite ao usuário a quantidade de turmas;
Para cada turma, peça que o usuário informe a quantidade de alunos;
Certifique-se de que o número de alunos por turma não ultrapasse 40;
Ao final, exiba a média de alunos por turma.
"""
turmas = int(input("Digite a quantidade de turmas:   "))
qtd_alunos = int(input("Digite a quantidade de alunos:   "))
resto = qtd_alunos % turmas
media = qtd_alunos / turmas
                 
while media > 40:
    print("A quantidade de alunos por turma não pode ultrapassar 40. Tente novamente.")
    qtd_alunos = int(input("Digite a quantidade de alunos:   "))

print(f"A média de alunos por turma é: {media:.2f}")



