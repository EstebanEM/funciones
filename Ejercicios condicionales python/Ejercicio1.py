#Solicitar número al usuario y determinar si es par, impar o es cero. 
num = int(input("¡Hola!, por favor ingresa un número: "))
#Los número par son aquellos que al dividirlos en 2 el resultado es 0
#los numero impares son aquellos que al dividirlos en 2 dal otro valor que no sea el '0'
if num % 2 ==0:
    print("El número ", num, " es par.")
else:
    print("El numero", num, " es impar")