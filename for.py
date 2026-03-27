"""
while - não sabe a quantidade (ele só vai fazer se uma das 
condições são verdadeiras) - ele verifique no começo.
for - quando vc sabe a condição predefinida

variáveis aninhada só pode ser utilizada dentro do for
ex: 
"""


texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper () in VOGAIS:
    print(letra, end="")

print()

