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

# Matriz transpuesta

MT = []

for j in range(3):

    fila = []

    for i in range(3):

        fila.append(M[i][j])

    MT.append(fila)

print("Matriz transpuesta:")

for fila in MT:
    print(fila)

M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]



T = []

for i in range(3):

    fila = []

    for j in range(3):

        suma = 0

        for k in range(3):

            suma = suma + M[i][k] * C[k][j]

        fila.append(suma)

    T.append(fila)

print("Matriz T:")

for fila in T:
    print(fila)