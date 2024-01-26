#ejercicios en clase
#palindromo
#traslater
# replace  espacios
# tranforma en minusculas
#frase invertid
#upper todo mayuscula
#lower
#f en print encierra las variables en {}. print(f "texto {varibe} texto.....")
fr = input("Por favor ingresa la plabra:__")
fr = fr.replace(" " , "")
fra= fr [:: -1]#ingresa la frase
print(fra)
fr = fr.lower () #minusculas
fr = fr.replace(" " , "")

if fr == fra: #reversa a la frase
    print(" es palindromo")
else:
    print("no es palindromo")    