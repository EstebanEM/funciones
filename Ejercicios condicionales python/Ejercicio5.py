#Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 
print("Promedio de notas y definitiva")
not1=float(input("Por favor ingresa la primera nota: "))
not2=float(input("Por favor ingresa la segunda nota: "))
not3=float(input("Por favor ingresa la terceranota: "))
not4=float(input("Por favor ingresa la cuarta nota: "))
not5=float(input("Por favor ingresa la quinta nota: "))

pro = not1 + not2 + not3 + not4 + not5 //5 #aquí se suman las notas y se resta por la cantidad de notras para poder sacr el resultado

if pro >= 3.0:
    print("Aprobó :D ")
elif pro < 3.0:
    print("Reprobo :( ")