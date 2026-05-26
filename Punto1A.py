# Consigna 1: Validación de usuarios y análisis de consistencia del sistema

A = [101, 102, 103, 104, 105, 106] # usurios que acceden a través de la API
B = [104, 105, 106, 107, 108] # usuarios que acceden a través de la web
C = [102, 105, 109] # usuarios que han generado errores 

#Parte A — Análisis con conjuntos

# (1)

#Calculando los usuarios que usan ambas plataformas

ambas_plataformas = []
for x in A:
    if x in B:
        ambas_plataformas.append(x)

print("Usuarios que usan ambas plataformas:", ambas_plataformas)

#Calculando usuarios que utilizan al menos una plataforma

al_menos_una = []
for x in A:
    if x not in al_menos_una:
        al_menos_una.append(x)
for x in B:
    if x not in al_menos_una:
        al_menos_una.append(x)

print("Usuarios que usan al menos una plataforma:", al_menos_una)

#Calculando usuarios que utilizan la plataforma y no presentan errores 

sin_errores = []
for x in al_menos_una:
    if x not in C:
        sin_errores.append(x)

print("Usuarios que utlizan la plataforma y no presentan errores:", sin_errores)

#Calculando usuarios que usan una plataforma en exclusivo

solo_api = []
for x in A:
    if x not in B:
        solo_api.append(x)

solo_web = []
for x in B:
    if x not in A:
        solo_web.append(x)

print("Usuarios que solo usan API:", solo_api)
print("Usuarios que solo usan WEB:", solo_web)

#(2)
#Aca tenemos que expresar por lo menos dos resultados usando comprensión de conjuntos
ambas_comp = [x for x in A if x in B]
solo_api_comp = [x for x in A if x not in B]


#(3)

#Tengo que detectar usuarios que estan en C pero no en A ni en B (Solo los que generan errores)

generadores_errores = []
for x in C:
    if x not in al_menos_una:
        generadores_errores.append(x)

print("Usuarios generadores de errores:", generadores_errores)

