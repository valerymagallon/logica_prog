#Ejercicio 4 
#Par o impar

número = float(input("Ingresa un número: "))

residuo = número % 2

if(residuo==0):
    print("Número PAR")
else:
    print("Número IMPAR")