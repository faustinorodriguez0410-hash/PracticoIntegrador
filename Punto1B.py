#Parte B:  Lógica proposicional

#Aca implementamos una funcion para evaluar usaurios que son criticos y los que son son criticos

#(6)


A = [101, 102, 103, 104, 105, 106] #p
B = [104, 105, 106, 107, 108] #q
C = [102, 105, 109] #r

# Unimos todos los usuarios (p q r) en una sola lista
usuarios = []
for x in A:
    if x not in usuarios:
        usuarios.append(x)
for x in B:
    if x not in usuarios:
        usuarios.append(x)
for x in C:
    if x not in usuarios:
        usuarios.append(x)

criticos = []
no_criticos = []

for u in usuarios:
    p = u in A
    q = u in B
    r = u in C

    if (p or q) and r:
        criticos.append(u)
    else:
        no_criticos.append(u)

print("Usuarios que son críticos:", criticos)
print("Usuarios que no son críticos:", no_criticos)


#(7) clasificar los usuarios en critico y no critico 

#Críticos: [102, 105]
#No críticos: [101, 103, 104, 106, 107, 108, 109]

