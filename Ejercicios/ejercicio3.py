#El programa debe chequear que la fila y la
#columna tengan valores válidos.
#En este caso, las únicas filas válidas son 0 y 1;
#las columnas, 0, 1 y 2. Si alguno de los dos
#valores es inválido, debe mostrar un mensaje
#de error
matriz =[[3.3 , 6.1, 4.0],[4.9, 5.7, 6.4]]

print(matriz)

fila = int(input("ingrese el valor de una fila:"))

columna = int(input("ingrese el valor de una columna:"))

if fila< len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("Error en las columnas")
else:
    print("Error en las columnas")