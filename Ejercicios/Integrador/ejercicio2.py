
codigo=[]
vendedor=[]
monto_vendido=[]

while True:
    print("""
    Menú de opciones:
    -----------------
    1 - Añadir un vendedor.
    2 - Mostrar la informacion de todos los vendedores.
    3 - Mostrar los vendedores con premio
    4 - Mostrar el vendedor que mas vendio
    5 - Mostrar el promedio de ventas
    6 - Mostrar el monto de dinero total vendido
    7 - Salir.
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        #Validar los datos ingresados
        while True:
            nombre = input("Ingrese el nombre del vendedor: ")
            if len(nombre) >= 3:
                break
            print("Ingrese un nombre con tres letras o más")
               
        while True:
             monto = input("Ingrese el monto que vendido el vendedor: ")
             if monto.isdigit() and int(monto) > 0:
                 monto = int(monto)
                 break
             else:
                 print("Ingrese un entero mayor a cero")

        while True:
             id = input("Ingrese el codigo del vendedor: ")
             if id.isdigit() and int(id) > 0:
                 id = int(id)
                 break
             else:
                 print("Ingrese un entero mayor a cero")
        
        #Cargar datos validados en las listas
        codigo.append(id)
        vendedor.append(nombre)
        monto_vendido.append(monto)
       
    elif opcion == "2":
        # Mostrar vendedores cargados
       if not vendedor:
           print("No hay vendedores")
       else:
           print("| codigo | vendedor | monto vendido |")
           for i in range(len(codigo)):
               print(" | " ,codigo[i], " | " ,vendedor[i] ," | $", monto_vendido[i], " | ")
    elif opcion == "3":
        #Creo una lista para almacenar los vendedores con premio
        vendedores_premio=[]
        #Cargo los vendedores con premio en la lista
        for l in range(len(monto_vendido)):
            if monto_vendido[l]>5000:
                vendedores_premio.append([vendedor[l],codigo[l]])
        #mostramos los vendedores con premio
        if len(vendedores_premio)>0:
            print("Los vendedores que tienen premio por haber superado el monto de $5000 son:")
            print(f"| vendedor | codigo |")
            for vendedor_con_premio in vendedores_premio:
                print(f"| {vendedor_con_premio[0]} | {vendedor_con_premio[1]} |")
        else:
            print("Ningun vendedor supero el monton de $5000")
        
    elif opcion == "4":
        #Mostramos el vendedor que mas vendio
        index=monto_vendido.index(max(monto_vendido))
        vendedor_mayor_venta= vendedor[index]
        print("El vendedor que mas vendio es: ",vendedor_mayor_venta)
    elif opcion == "5":
        #mostramos el promedio de ventas
        ventas=0
        for venta in monto_vendido:
            ventas=ventas+venta
        
        promedio_ventas= ventas/len(monto_vendido)
        print("El promedio de ventas es: ",promedio_ventas)
    elif opcion == "6":
        #Mostramos el total recaudado por los vendedores
        total=0
        for venta in monto_vendido:
            total=total+venta
        
        print("El total recaudado por los vendedores es: ", total)
    elif opcion == "7":
        print("Gracias por utilizar este programa...")
        break
        
    else:
        print("Opción incorrecta")
    