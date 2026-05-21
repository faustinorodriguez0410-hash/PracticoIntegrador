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