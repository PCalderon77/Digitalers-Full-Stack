#Escriba un programa que permita crear una lista
#de nombres.
#Para ello, el programa tiene que pedir un número
#y luego solicitar esa cantidad de nombres para
#crear la lista. Por último, el programa tiene que
#mostrar la lista creada. 


cantidad = input("¿Cuantos nombres desea ingresar?: ")


cantidad = int(cantidad)

#Lista
nombres = []

#Variable
contador = 0


while contador < cantidad:
    #Variable aux
    name = input("Ingrese un nombre: ")
    #el append siempre agrega al final de las listas
    nombres.append(name)
    
    contador = contador + 1

print(nombres)