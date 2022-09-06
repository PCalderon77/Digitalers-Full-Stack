#Crear un programa que solicite una fila y una
#columna e imprima en pantalla el número en
#esa posición según la siguiente matriz:
# matriz =[[3.3 , 6.1, 4.0],[4.9, 5.7, 6.4]]
matriz =[[3.3 , 6.1, 4.0],[4.9, 5.7, 6.4]]

print(matriz)

fila = int(input("ingrese el valor de una fila:"))

columna = int(input("ingrese el valor de una columna:"))

print(matriz[fila][columna])
