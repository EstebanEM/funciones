#Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje "Usted es mayor de edad", de lo contrario "Usted es menor de edad". Si el número ingresado es negativo o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.
nom=input("¡Hola! ¿Cómo te llamas?. ")
edad= int(input("por favor ingresa tu edad. "))

if edad >= 18:
    print(nom," eres mayor de edad. :)")
else:
    print(nom, " ere menor de edad. :)")