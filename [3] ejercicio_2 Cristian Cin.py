E1 = int(input("Introduzca la edad de la primera persona: "))
E2 = int(input("Introduzca la edad de la segunda persona: "))
E3 = int(input("Introduzca la edad de la tercera persona: "))
E4 = int(input("Introduzca la edad de la cuarta persona: "))

# Primer apartado. Añadimos cada edad a una lista y comprobamos cuál es la mayor de ellas.

lista_edades = [E1, E2, E3, E4]

print(E1 == max(lista_edades))

# Segundo apartado. Creamos una lista y mediante un loop comprobaremos si existe algún valor que
# sea superior al 30. De ser así, lo añadimos a la lista y comprobamos si la lista guarda 2 valores
# que superen el 30.

mayor_de_30 = []

for value in lista_edades:
    if value > 30:
        mayor_de_30.append(value)

print(len(mayor_de_30) == 2)

# Tercer apartado. Evalúamos la expresión tal y como se pide.

print(E1 % 2 == 0 and E3 % 2 == 0 and E4 % 2 != 0 or
      E1 % 2 == 0 and E3 % 2 != 0 and E4 % 2 == 0)

# Cuarto apartado. Creamos una lista para realizar pruebas. Mediante un "for" loop de 2 dimensiones,
# (es decir, un loop dentro de otro loop) comprobamos si para cada valor de la lista de edades, restándole
# otro valor de esa lista; el resultado se encuentra entre el 0 y el 10 (ha de ser mayor o igual que 0 a fin de
# evitar posibles valores negativos, ya que eso supondría que la expresión siempre fuera cierta).
# Si tal condición se cumple, añadiremos ese valor a la lista de pruebas creada con anterioridad.
# Luego, procederemos a evaluar si cualquier valor contenido en esa lista es menor o igual que 10.

testing_list = []

for value in lista_edades:
    for item in lista_edades:
        if item != value and 0 <= item - value <= 10:
            testing_list.append(item - value)

print(any(testing_list) <= 10)
