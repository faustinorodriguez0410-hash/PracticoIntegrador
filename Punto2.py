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