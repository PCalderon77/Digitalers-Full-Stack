#Ingresar límite inferior y límite superior es decir 2 valores numéricos, mostrar todos los números comprendido
#entre esos límites.
#Además, se pide:
# a) Suma de valores mostrados por pantalla
# b) Mostrar cuantos son pares y cuantos impares
# c) Del rango de valores mostrados por pantalla indicar cantidad de números divisibles por 5
# d) Si se ingresó el valor cero indicarlo en el informe
# e) Mostrar la cantidad de valores en el rango mostrado que sean divisibles por 1 y por 3 conjuntamente.
# f) Cantidad de valores comprendido entre los limites ingresados


#Validar los datos ingresados
while True:
    limite_inferior=int(input("Ingrese el limite inferior: "))
    limite_superior=int(input("Ingrese el limite superior: "))
    if limite_superior > limite_inferior:
        break
    print("El limite superior debe ser mayor que el limite inferior, ingrese los valores nuevamente")

contador_numeros=0
contador_pares=0
contador_impares=0
contador_divisible_cinco=0
contador_divisible_tres=0
suma=0
print("Los numeros entre ", limite_inferior ," y ", limite_superior, "son:")
for i in range(limite_inferior+1,limite_superior):
    #Mostrar valores entre los limites
    print(i)
    #Sumar los valores mostrados
    suma+=i
    #Contar los numeros entre los limites
    contador_numeros +=1
    #Contar numeros impares y pares
    if i %2 ==0:
        contador_pares +=1
    else:
        contador_impares +=1
    #Contar numeros divisible por 5
    if i%5 == 0:
        contador_divisible_cinco +=1
    
    #contar numeros divisibles por 5
    if i%3 == 0 and i%1 ==0:
        contador_divisible_tres +=1

#Mostrar si el limite inferior es cero
if (limite_inferior or limite_superior)==0 :
    print("Usted ingreso el numero cero como limite inferior")
#Mostrar suma
print("La suma de los numeros comprendidos entre ",limite_inferior," y ",limite_superior," es ",suma)
#Mostrar contador
print("La cantidad de numeros entre ",limite_inferior," y ",limite_superior," es ",contador_numeros)
#Mostrar cantidad de numeros pares o impares
print("La cantidad de numeros pares entre ",limite_inferior," y ",limite_superior," son ",contador_pares)

print("La cantidad de numeros impares entre ",limite_inferior," y ",limite_superior," son ",contador_impares) 
#Mostrar cantidad de numeros divisibles por 5
print("La cantidad de numeros divisibles por 5 entre ",limite_inferior," y ",limite_superior," son ",contador_divisible_cinco)
#Mostrar cantidad de numeros divisibles por 3
print("La cantidad de numeros divisibles por 3 entre ",limite_inferior," y ",limite_superior," son ",contador_divisible_tres)






