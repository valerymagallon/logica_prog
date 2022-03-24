# OPERACIONES MATEMÁTICAS
# Usando Operadores Matemáticos y Funiones Matemáticas

#IMPORTAR LIBRERÍA PARA FUNCIONAES MATEMÁTICAS
import math 

# ENTRADA DE DATOS

número1 = float(input("Escribe el radio: ")) 

#DEFINIR UNA CONSTANTE 
PI = 3.1416 
radio = número1
diametro = radio * 2


# PROCESO (Cálculos y Operaciones Matemáticas y/o Lógicas)

perímetro = 2 * PI * radio
área = PI * (radio ** 2)

# SALIDA DE DATOS 

print(f"El área del circulo es = {área}")
print(f"El perímetro del círculo es = {perímetro}")