# Ejercicio 8

from re import I


número = float(input("Ingresa un número: "))


if(número <0 and número > -100):
    for número in range (-1, -100, -2):
        print(f"{número}")
    
elif(número >0 and número <100):
    número= 2
    while (número<100):
        print(f"{número}")
        número= número + 2

else:
    print("No válido")