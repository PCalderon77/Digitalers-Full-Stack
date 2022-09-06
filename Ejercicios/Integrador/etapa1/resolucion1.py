#Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno.
#Para ello se debe realizar primero una aplicación de consola la cual debe solicitar el nombre de un
#alumno y la cantidad de cursos en la que se
#encuentra inscripto.
#Estos dos valores deben almacenarse como una
#lista de dos elementos (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.
#Una vez hecho esto, se debe hacer que el programa, al iniciar, pregunte cuál de las siguientes dos
#operaciones se debe realizar: ingresar un alumno o ver la lista de alumnos ingresados. 
#Esto debe preguntarse infinitamente hasta que el usuario escriba “3”. 


alumnos= []

while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        print("Lista de alumnos:")
        for alumno in alumnos:
            nombre = alumno[0]
            cursos = alumno[1]
        # Necesito convertir "cursos" a una cadena para poder
        # concatenarlo con otras cadenas.
        print(nombre + " - " + str(cursos) + " cursos")
    elif opcion == "2":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        
        cursos = int(input("Ingrese la cantidad de cursos: "))
        if nombre_alumno == "":
           print("Error: no ha ingresado un nombre válido.")
        else:
           alumnos.append([nombre_alumno, cursos])
        print("Has ingresado el alumno correctamente.")
    elif opcion == "3":
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")
        
print("¡Gracias por utilizar el programa!")