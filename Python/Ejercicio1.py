# OPERACIONES MATEMÁTICAS
# Usando Operadores Matemáticos y Funiones Matemáticas

#IMPORTAR LIBRERÍA PARA FUNCIONAES MATEMÁTICAS
import math 

# ENTRADA DE DATOS

número1 = float(input("Ingresa la primera calificación: ")) 
número2 = float(input("Ingresa la segunda calificación: "))
número3 = float(input("Ingresa la tercera calificación: "))

# PROCESO (Cálculos y Operaciones Matemáticas y/o Lógicas)

promedio = (número1 + número2 + número3)/3 


# SALIDA DE DATOS 

print(f"El promedio de 3 calificaciones es = {promedio}")

if (promedio>=6.1):
    print("Aprobado")
elif(promedio<6):
    print("Reprobado")