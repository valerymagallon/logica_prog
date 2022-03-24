# OPERACIONES MATEMÁTICAS
# Usando Operadores Matemáticos y Funiones Matemáticas

#IMPORTAR LIBRERÍA PARA FUNCIONAES MATEMÁTICAS
import math 

# ENTRADA DE DATOS

a = float(input("Ingrese el valor de a: ")) 
b = float(input("Ingrese el valor de b: ")) 
c = float(input("Ingrese el valor de c: ")) 

# PROCESO (Cálculos y Operaciones Matemáticas y/o Lógicas)

fórmula_general_x1 = (- b - math.sqrt(b ** 2) - 4 * (a) * (c))/ 2 * a 
fórmula_general_x2 = (- b + math.sqrt(b ** 2) - 4 * (a) * (c))/ 2 * a 

# SALIDA DE DATOS 

print(f"El resultado de x1 es = {fórmula_general_x1}")
print(f"El resultado de x2 es = {fórmula_general_x2}")