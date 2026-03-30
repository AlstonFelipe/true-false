"""
1. Desenvolvavum programa que funcione da seguinte maneira:

Solicite ao usuário que informe a quantidade total de pessoas em um grupo.
Para cada pessoa, peça que o usuário registre o sexo, utilizando a 
letra 'm' ou 'M' para masculino.
O programa deve contar e, ao final, exibir o total de pessoas do sexo masculino.


"""

total_pessoas = int(input("Informe a quantidade total de pessoas: "))

contador_masculino = 0
feminino = 0


for numero in range(total_pessoas):
    genero = input(f"Informe o genero da pessoa {numero+1} (m/M para masculino): ")
    
    
    if genero == 'm' or genero == 'M':
        contador_masculino += 1
    # uso de AND
    elif genero != 'm' and genero != 'M':
        print("Sexo diferente de masculino registrado.")

print(f"Total de pessoas do sexo masculino: {contador_masculino}")