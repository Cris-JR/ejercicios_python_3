# El programa pide al usuario que inserte tres números, los cuales serán almacenados en una lista
# con el objetivo de comprobar cuál de ellos es el mayor de los tres.

numero_1 = float(input("Inserte el primer número: "))
numero_2 = float(input("Inserte el segundo número: "))
numero_3 = float(input("Inserte el tercer número: "))

lista_numeros = [numero_1, numero_2, numero_3]

print(f"El mayor número de los tres es: {max(lista_numeros)}")
