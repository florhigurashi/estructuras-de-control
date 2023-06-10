#1. Realice un programa que solicite dos letras ingresadas por el usuario y
#verifique si son iguales o no, mostrando un mensaje.

letra1= str(input("Ingrese la primera letra:"))
letra2= str(input("Ingrese la segunda letra:"))

if letra1 == letra2:
    print("Las letras son iguales")
else:
    print("Las letras no son iguales")
    
#2. Hacer un programa que permita decidir si dos palabras son iguales o
#diferentes. Mostrar mensaje por pantalla.

palabra1= str(input("Ingrese la primera palabra:"))
palabra2= str(input("Ingrese la segunda palabra:"))

if palabra1==palabra2:
    print("Las palabras son iguales:")A
else: 
   print("Las palabras no son iguales:")

#3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota
#en mesa femenina o masculina.

genero= str(input("Ingrese f si es femenino:"))

if genero =="f":
    print("Usted vota en la mesa femenina")
else:
    print("Usted vota en mesa masculina")

#4. Realice un programa que lea dos números y diga cuál es el mayor.

num1= float(input("Ingrese el primer numero:"))
num2= float(input("Ingrese el segundo numero:"))   

if num1>num2:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")

#5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa

tipo_cambio=float(input("Ingrese el valor del dolar al dia de hoy:"))
monto-a-cambiar=int("Ingrese el monto de dinero del que dispone, indicando 'p' si son pesos o 'd' si son dolares:")

if =='p':
    
    disponible= monto-a-cambiar/tipo_cambio
    print("La cantidad de dolares de la que dispone es:")
    
elif =='d':
    disponible= monto-a-cambiar * tipo_cambio
    print("La cantidad de pesos de la que dispone es:") 
else:
    print("Lo siento, no entiendo esa opción.")

#6. Realice un programa donde el usuario ingrese su edad. Si es mayor de
#16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”

edad= int(input("Ingrese su edad:"))

if edad>16:
    print("Puede votar")
else:
    print("No vota")
    




    
        
    
    

 


    
    
    