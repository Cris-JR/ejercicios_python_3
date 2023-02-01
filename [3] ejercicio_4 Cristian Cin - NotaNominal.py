# El programa pide al usuario la nota obtenida, tras lo que pasa por una cadena de condiciones
# para comprobar cómo se debe clasificar tal nota. En caso de que la nota no coincida con ningún número entre
# el 0 y el 10, se emite un mensaje a modo de error.

nota_obtenida = int(input("Introduzca la nota que ha obtenido: "))

if nota_obtenida in range(5):
    print("Ha obtenido un INSUFICIENTE.")
elif nota_obtenida == 5:
    print("Ha obtenido un SUFICIENTE.")
elif nota_obtenida == 6:
    print("Ha obtenido: BIEN.")
elif nota_obtenida in range(7, 9):
    print("Ha obtenido un NOTABLE.")
elif 9 <= nota_obtenida <= 10:
    print("¡Enhorabuena! Ha obtenido un SOBRESALIENTE.")
else:
    print("El valor de la nota debe ser un número entero entre el 0 y el 10.")