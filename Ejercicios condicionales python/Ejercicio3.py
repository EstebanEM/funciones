#Solicitar número al usuario y determinar si es negativo, positivo o cero.
print("¡hola!")
num =int(input("Por favor ingresa un número"))
if num<0:
    print("El número ", num, " es negativo.")
elif num>0:
    print("El número ", num, " es positivo.")    
else:
    print("El número es cero :D")