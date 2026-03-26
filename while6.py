"""
6.Crie
um programa em Python que leia números inteiros do teclado até que o usuário
digite 0. Ao final, exiba a soma de todos os números digitados.
"""
numeros = 0
qts_numeros = 0
while True:
    numero = int(input("Digite o numero para ser somado): "))
    if numero == 0:
        break
    numeros = numeros + numero
    qts_numeros = qts_numeros + 1

print(f"Quantidade de números digitados: {qts_numeros}")
print(f"A soma de todos os números digitados é: {numeros}")

