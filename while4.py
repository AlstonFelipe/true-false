"""
4.Elabore
um algoritmo que receba um número, conte quantos dígitos ele possui e exiba o
resultado. Por exemplo, se o número for 201, a saída deve ser 3"""


numero = int(input("Digite um número: "))

contador = 0

while numero > 0:
    numero = numero // 10
    contador = contador + 1

print(contador)