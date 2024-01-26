#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.
num1=int(input("Por favor ingresa el primer número: "))
num2= int(input("Por favor ingresa el segundo número: "))

if num1 > num2:
    print("El número", num1, " es mayor a ", num2)
elif num1 < num2:
    print("El número", num1, " es menor a ", num2)