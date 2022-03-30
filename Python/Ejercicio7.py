#Ejercicio 7


nivel_agua = float(input("Ingresa el nivel de agua en metros: "))

if(nivel_agua >=6.1):
    print("Desbordamiento de agua en cisterna")
elif(nivel_agua ==6):
     print("Apagar bomba")
elif(nivel_agua >=4 and nivel_agua <6):
    print("Desacelerar bomba")
elif(nivel_agua >=2 and nivel_agua <4):
    print("¡Bomba trabajando!")
elif(nivel_agua >0 and nivel_agua <2):
    print("Acelerar bomba de agua")
elif(nivel_agua ==0):
    print("Encender bomba de agua")
elif(nivel_agua <0):
    print("Fuga de cisterna")
else:
    print("No es un valor aceptado")