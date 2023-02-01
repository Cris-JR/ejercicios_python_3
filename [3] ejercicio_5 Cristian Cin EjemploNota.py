# Pide al usuario las tres notas requeridas y las guarda en una lista.
# Las notas guardadas pasan por expresiones condicionales que evalúan cuál será el valor de la nota final
# de acuerdo con los requisitos establecidos por el ejercicio. Finalmente, se imprimirá la nota final.

notas = [int(input("Introduzca la primera nota: ")),
        int(input("Introduzca la segunda nota: ")),
        int(input("Introduzca la tercera nota: "))]

nota_final = None

if notas[0] < 4 and notas[1] < 4 and notas[2] < 4:
    nota_final = 0
elif notas[0] > 4 and notas[1] > 4 and notas[2] > 4:
    nota_final = 0.3 * notas[0] + 0.2 * notas[1] + 0.5 * notas[2]
else:
    for value in notas:
        if value <= 4:
            nota_final = 2

print(f"La nota final que ha obtenido es: {nota_final}")
