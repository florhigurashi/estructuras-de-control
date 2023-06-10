#1. Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.

numeros = []
for i in range(4):
    numeros.append(int(input("Ingrese un número: ")))

cantidad_pares = 0
sumatoria_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        cantidad_pares += 1
        sumatoria_pares += numero

cantidad_impares = len(numeros) - cantidad_pares

print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)
print("Sumatoria de los números pares:", sumatoria_pares)

#2.Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

cantidad_mayores = 0
cantidad_menores = 0
maximo = numeros[0]
minimo = numeros[0]
for numero in numeros:
    if numero > 100:
        cantidad_mayores += 1
    elif numero < 100:
        cantidad_menores += 1

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero


print("Cantidad de números mayores a 100:", cantidad_mayores)
print("Cantidad de números menores a 100:", cantidad_menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)

#3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.

cantidad_mujeres = 0
cantidad_varones = 0
cantidad_mayores = 0
cantidad_menores = 0
for i in range(15):
    if sexos[i] == "F":
        cantidad_mujeres += 1
    elif sexos[i] == "M":
        cantidad_varones += 1

    if edades[i] >= 18:
        cantidad_mayores += 1
    else:
        cantidad_menores += 1

print("Cantidad de mujeres:", cantidad_mujeres)
print("Cantidad de varones:", cantidad_varones)
print("Cantidad de mayores de edad:", cantidad_mayores)
print("Cantidad de menores de edad:", cantidad_menores)

#4.Leer 10 números y mostrar solamente los números positivos, y su
#sumatoria.

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

numeros_positivos = [numero for numero in numeros if numero > 0]
sumatoria_positivos = sum(numeros_positivos)

print("Números positivos:", numeros_positivos)
print("Sumatoria de los números positivos:", sumatoria_positivos)

#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
#números.

numeros_negativos = []
for i in range(15):
    numero = int(input("Ingrese un número negativo: "))
    if numero < 0:
        numeros_negativos.append(numero)
    else:
        print("Este número no es negativo. Ingrese uno negativo.")
        i -= 1

numeros_positivos = [-numero for numero in numeros_negativos]
print("Números positivos correspondientes:")
print(numeros_positivos)
