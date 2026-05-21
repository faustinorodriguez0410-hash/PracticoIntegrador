M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

print("Promedio por función:")

for i in range(3):
    suma = 0

    for j in range(3):
        suma = suma + M[i][j]

    promedio = suma / 3

    print("Funcion", i + 1, ":", promedio)

print("\nPromedio por servidor:")

for j in range(3):
    suma = 0

    for i in range(3):
        suma = suma + M[i][j]

    promedio = suma / 3

    print("Servidor", j + 1, ":", promedio)