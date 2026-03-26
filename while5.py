"""
5.Desenvolva
um programa em Python que peça ao usuário para criar uma senha e, em seguida,
solicite que ele a digite novamente. Continue pedindo até que as duas senhas
correspondam.
"""
senha = input("Crie uma senha: ")
senha_confirmacao = input("Digite a senha novamente: ")

while senha != senha_confirmacao:
    print("As senhas não correspondem. Tente novamente.")
    senha = input("Crie uma senha: ")
    senha_confirmacao = input("Digite a senha novamente: ")

print("Senha criada com sucesso!")


