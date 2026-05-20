#Hacer python -m pip install matplotlib
import matplotlib.pyplot as plt

# 5. Defino las funciones y los modelos de costo
def costo_A(x):
    return 40 * x + 200

def costo_B(x):
    return 70 * x + 50

def costo_C(x):
    return -2 * (x ** 2) + 80 * x + 100

# 8. Creo una función para saber cual es el plan más economico
def plan_mas_economico(x):
    costo_a = costo_A(x)
    costo_b = costo_B(x)
    costo_c = costo_C(x)
    
    # Busco el menor costo usando condicionales 
    if costo_a <= costo_b and costo_a <= costo_c:
        return "Plan A", costo_a
    elif costo_b <= costo_a and costo_b <= costo_c:
        return "Plan B", costo_b
    else:
        return "Plan C", costo_c
    
# 7. Evaluo las funciones para los valores dados
valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("Evaluando cual plan resulta más conveniente segun horas de uso mensual: ")
print("-" * 50)
for x in valores_x:
    a = costo_A(x)
    b = costo_B(x)
    c = costo_C(x)
    mejor_plan, menor_costo = plan_mas_economico(x)
    
    print(f"Horas (x): {x}")
    print(f"  Costo A: ${a} | Costo B: ${b} | Costo C: ${c}")
    print(f"  -> Conviene el {mejor_plan} (${menor_costo})")
    print("-" * 50)

# 6. Grafico en el intervalo [0, 50]
# Genero los valores del dominio 
dominio_x = []
for i in range(51):  # De 0 a 50 inclusive
    dominio_x.append(i)

valores_y_A = []
valores_y_B = []
valores_y_C = []

for x in dominio_x:
    valores_y_A.append(costo_A(x))
    valores_y_B.append(costo_B(x))
    valores_y_C.append(costo_C(x))

# Configuración del gráfico
plt.plot(dominio_x, valores_y_A, label='Plan A (40x + 200)', color='blue')
plt.plot(dominio_x, valores_y_B, label='Plan B (70x + 50)', color='red')
plt.plot(dominio_x, valores_y_C, label='Plan C (-2x^2 + 80x + 100)', color='green')

# Marco el eje X donde el costo es 0 para notar los negativos
plt.axhline(0, color='black', linewidth=1) 

plt.title('Comparación de Planes de Costo de Desarrollo')
plt.xlabel('Horas mensuales (x)')
plt.ylabel('Costo en $')
plt.legend()
plt.grid(True)
plt.show()