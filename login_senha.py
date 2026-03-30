"""
4. Desenvolva um programa que solicite ao usuário um nome e uma senha,
garantindo que a senha não seja igual ao nome de usuário. Se forem iguais,
exiba uma mensagem de erro e peça as informações novamente.
"""

for tentativa in range(5):  # limite de 5 tentativas
    nome = [input("Digite o nome de usuário: ")]
    senha = [input("Digite a senha: ")]
    
    if senha == nome or senha == "":
        print("Erro: a senha não pode ser igual ao nome ou vazia.\n")
    else:
        print("Cadastro realizado com sucesso!")
        break
else:
    print("Número máximo de tentativas atingido.")

    