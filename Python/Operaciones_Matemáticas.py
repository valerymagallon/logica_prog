# OPERACIONES MATEMÁTICAS
# Usando Operadores Matemáticos y Funiones Matemáticas

#IMPORTAR LIBRERÍA PARA FUNCIONAES MATEMÁTICAS
import math 

# ENTRADA DE DATOS

número1 = float(input("Escribe un número: ")) # Convertir de string a int
número2 = float(input("Ingrese otro número: "))

# PROCESO (Cálculos y Operaciones Matemáticas y/o Lógicas)
suma = número1 + número2
resta = número1 - número2
multiplicación = número1 * número2
división = número1 / número2

potencia1 = número1 ** número2
potencia2 = pow(número1, número2)
cuadrado = número1 ** 2
cubo = pow(número2, 3)
raíz_cuadrada1 = pow(número1, 1/2)
raíz_cuadrada2 = math.sqrt(número2)
raíz_cúbica = pow(9, 1/3)

módulo_residuo = número1 % número2
# SALIDA DE DATOS 
print("La suma =",suma)
print("La suma = " + str(suma)) # CONTCATENACIÓN (Unión de Textos)
# Convertir un tipo de dato en otro tipo de dato
print(f"La suma = {suma}")
print("La resta =",resta)
print("Lmultiplicación =",multiplicación)
print("La división =",división)
print(f"La potencia1 = {potencia1}")
print(f"La potencia2 = {potencia2}")
print(f"El cuadrado de número1 = {cuadrado}")
print(f"El cubo de número 2  = {cubo}")
print(f"La raíz cuadrada de número1= {raíz_cuadrada1}")
print(f"La raíz cuadrada de número2 = {raíz_cuadrada2}")
print(f"La raíz cúbica de 9 = {raíz_cúbica}")
print(f"El módulo de número 1 entre número 2= {módulo_residuo}")