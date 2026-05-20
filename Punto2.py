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