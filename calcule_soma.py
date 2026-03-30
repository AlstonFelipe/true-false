"""
3. Crie um programa que leia 5 números e calcule a soma e a média desses números,
exibindo os resultados.


"""

soma = 0

for incremento in range(5):
    numero = float(input(f"Digite o {incremento+1}º número: "))
    soma += numero

media = soma / 5

print(f"Soma é: {soma}")
print(f"Média é: {media}")

