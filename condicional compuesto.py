#1. Introducir los lados de un triángulo y visualizar por pantalla si dicho
#triángulo es equilátero, isósceles o escaleno.

#lado1 = float(input("Introduce el primer lado del triángulo: "))
#lado2 = float(input("Introduce el segundo lado del triángulo: "))
#lado3 = float(input("Introduce el tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 != lado2 != lado3 != lado1:
    print("El triángulo es escaleno.")
else:
    print("El triángulo es isósceles.")

#2. Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%

importe = float(input("Introduce el importe a pagar: "))
forma_pago = int(input("Selecciona la forma de pago (1: Contado, 2: Tarjeta, 3: Débito): "))

if forma_pago == 1:
    descuento = importe * 0.1
    importe_total = importe - descuento
    print("Importe:", importe)
    print("Descuento:", descuento)
    print("Importe total a pagar:", importe_total)
elif forma_pago == 2:
    interes = importe * 0.1
    importe_total = importe + interes
    print("Importe:", importe)
    print("Interés:", interes)
    print("Importe total a pagar:", importe_total)
elif forma_pago == 3:
    descuento = importe * 0.05
    importe_total = importe - descuento
    print("Importe:", importe)
    print("Descuento:", descuento)
    print("Importe total a pagar:", importe_total)
else:
    print("Forma de pago no válida.")
    
#3. Realice un programa que lea tres números, muestre cuál es el mayor y
#determine si es par o impar.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num

print("El número mayor es:", mayor)

if mayor % 2 == 0:
   print("El número mayor es par.")
else:
    print("El número mayor es impar.")

#4.Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.

num = int(input("Introduce un número del 1 al 7: "))

if num == 1:
    print("El número", num, "corresponde al día Lunes.")
elif num == 2:
    print("El número", num, "corresponde al día Martes.")
elif num == 3:
    print("El número", num, "corresponde al día Miércoles.")
elif num == 4:
    print("El número", num, "corresponde al día Jueves.")
elif num == 5:
    print("El número", num, "corresponde al día Viernes.")
elif num == 6:
    print("El número", num, "corresponde al día Sábado.")
elif num == 7:
    print("El número", num, "corresponde al día Domingo.")
else:
    print("Número no válido. Introduce un número del 1 al 7.")
 
#5. Realice un programa que pida un número del 1 al 12 y diga el nombre
#del mes correspondiente.

num = int(input("Introduce un número del 1 al 12: "))

if num == 1:
    print("El número", num, "corresponde al mes de Enero.")
elif num == 2:
    print("El número", num, "corresponde al mes de Febrero.")
elif num == 3:
    print("El número", num, "corresponde al mes de Marzo.")
elif num == 4:
    print("El número", num, "corresponde al mes de Abril.")
elif num == 5:
    print("El número", num, "corresponde al mes de Mayo.")
elif num == 6:
    print("El número", num, "corresponde al mes de Junio.")
elif num == 7:
    print("El número", num, "corresponde al mes de Julio.")
elif num == 8:
    print("El número", num, "corresponde al mes de Agosto.")
elif num == 9:
    print("El número", num, "corresponde al mes de Septiembre.")
elif num == 10:
    print("El número", num, "corresponde al mes de Octubre.")
elif num == 11:
    print("El número", num, "corresponde al mes de Noviembre.")
elif num == 12:
    print("El número", num, "corresponde al mes de Diciembre.")
else:
    print("Número no válido. Introduce un número del 1 al 12.")    

