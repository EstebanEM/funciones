#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente.
num1=int(input("Por favor ingresa el primer número_  "))
num2=int(input("Por favor ingresa el segundo número_ "))
num3=int(input("Por favor ingresa el terser número_ "))
#el numero 1 e mayor al humero 2 y si el numero 2 es mayor al numero 3
if(num1>num2 and num2>num3): #orfganizacionde ascendente
    print("", num1, "", num2,"",num3)
elif(num2>num1 and num3>num2):
    print("", num2, "", num1,"",num3)
elif(num3>num1 and num1>num2):
    print("", num3, "", num1,"",num2)
elif(num3>num2 and num2>num1):
    print("", num3, "", num2,"",num1)
elif(num1>num3 and num3>num2):
    print("", num1, "", num3,"",num2)
elif(num2>num3 and num3>num1):
    print("", num2, "", num3,"",num1)
else:
    print("Se eingresaron numero iguales")