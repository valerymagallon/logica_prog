# FUNCIONES: Tareas o acciones a ejecutar
# SINTAXIS:
# def Nombre_de_la_función (Argumentos o Parámetros):
# contenido

#PARADIGMA O ENFOQUE FUNCIONAL / MODULAR

def Sumar(a, b): #Obtiene o recibe dos parámetros 
    suma = a + b
    return suma  #return: Devuelve, Retornar o Regresar un valor
def Restar(a, b):
    resta = a - b
    return resta
def Multiplicar(a, b):
    multiplicación = a * b
    return multiplicación
def Dividir(a, b):
    dividir = a / b
    return dividir

# Mandar a llamar o invocar una función y el resultado se asigna a una variable
s = Sumar(2, 3) #Envían o pasan los parámetros
r = Restar(3, 2) 
m = Multiplicar (2, 3)
d = Dividir (10, 2)

# Salida
print(f"La suma = {s}")
print(f"La suma = {Sumar(20, 10)}")
print(f"La resta = {r}")
print(f"La multiplicación = {m}")
print(f"La división = {d}")