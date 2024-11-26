print("Conversor de unidades de longitud")
print("""
         1.metros.
         2.kilómetros.
         3.centímetros.
         4.millas.
         5.pies
         6.pulgadas.
         7.salir""")

opcion1= input("Ingrese la unidad: ")

if opcion1 == "1":
    print("_______MENÚ_______")
    print("1.kilometros")
    print("2.centimetros")
    print("3.millas")
    print("4.pies")
    print("5.pulgadas")
    metros=int(input("Ingrese el número: "))
    opcion=input("¿Cuál deseas convertir?: ")
    if (opcion=="1"):
          kilometros = metros / 1000
          print(kilometros)
    elif(opcion=="2"):
        centimetros = metros * 100
        print(centimetros)
    elif(opcion=="3"):
        millas = metros * 0.000621371
        print(millas)
    elif(opcion=="4"):
        pies = metros * 3.28084
        print(pies)
    elif(opcion=="5"):
        pulgadas = metros * 39.3701
        print(pulgadas)
    else:
        print("Opción no válida.")
elif opcion1 == "2":
    print("_______MENÚ_______")
    print("1.metros")
    print("2.centimetros")
    print("3.millas")
    print("4.pies")
    print("5.pulgadas")
    kilometros=int(input("Ingrese el número: "))
    opcion=input("¿Cuál deseas convertir?: ")
    if (opcion=="1"):
          metros = kilometros * 1000
          print(metros)
    elif(opcion=="2"):
        centimetros = kilometros * 100000
        print(centimetros)
    elif(opcion=="3"):
        millas = kilometros * 0.621371
        print(millas)
    elif(opcion=="4"):
        pies = kilometros * 1000 * 3.28084
        print(pies)
    elif(opcion=="5"):
        pulgadas = kilometros * 1000 * 39.3701   
        print(pulgadas)
    else:
        print("Opción no válida.")
elif(opcion=="3"):
    print("_______MENÚ_______")
    print("1.metros")
    print("2.kilometros")
    print("3.millas")
    print("4.pies")
    print("5.pulgadas")
    centimetro=int(input("Ingrese el número: "))
    opcion=input("¿Cuál deseas convertir?: ")
          
    if (opcion=="1"):
          metros = centimetros / 100
          print(metros)
    elif(opcion=="2"):
        kilometros = centimetros / 100000
        print(kilometros)
    elif(opcion=="3"):
        millas = centimetros / 160934.4
        print(millas)
    elif(opcion=="4"):
        pies = centimetros / 30.48
        print(pies)
    elif(opcion=="5"):
        pulgadas = centimetros / 2.54   
        print(pulgadas)
    else:
        print("Opción no válida.")
elif(opcion=="4"):
    print("_______MENÚ_______")
    print("1.metros")
    print("2.kilometros")
    print("3.centimetros")
    print("4.pies")
    print("5.pulgadas")
    millas=float(int(input("Ingrese el número: ")))
    opcion=input("¿Cuál deseas convertir?: ")
    if (opcion=="1"):
          metros = millas / 0.000621371
          print(metros)
    elif(opcion=="2"):
        kilometros = metros / 1000
        print(kilometros)
    elif(opcion=="3"):
        centimetros = millas / 0.000621371 * 100
        print(centimetros)
    elif(opcion=="4"):
        pies = metros * 3.28084
        print(pies)
    elif(opcion=="5"):
        pulgadas = metros * 39.3701 
        print(pulgadas)
    else:
        print("Opción no válida.")
elif(opcion=="5"):
    print("_______MENÚ_______")
    print("1.metros")
    print("2.kilometros")
    print("3.centimetros")
    print("4.millas")
    print("5.pulgadas")
    pies=float(int(input("Ingrese el número: ")))
    opcion=input("¿Cuál deseas convertir?: ")
    if opcion == 1:
        metros = pies / 3.28084
        print(metros)
    elif opcion == 2:
        kilometros = (pies / 3.28084) / 1000
        print(kilómetros)
    elif opcion == 3:
        centimetros = (pies / 3.28084) * 100
        print(centímetros)
    elif opcion == 4:
        millas = pies / 5280
        print(millas)
    elif opcion == 5:
        pulgadas = pies * 12
        print(pulgadas)
    else:
        print("Opción no válida.")
elif(opcion=="6"):
    print("_______MENÚ_______")
    print("1.metros")
    print("2.kilometros")
    print("3.centimetros")
    print("4.millas")
    print("5.pies")
    pulgadas=float(int(input("Ingrese el número: ")))
    opcion=input("¿Cuál deseas convertir?: ")
    if opcion == "1":
        metros = pulgadas / 39.3701
        print(metros)
    elif opcion == "2":
        kilometros = (pulgadas / 39.3701) / 1000
        print(kilómetros)
    elif opcion == "3":
        centimetros = pulgadas * 2.54
        print(centímetros)
    elif opcion == "4":
        millas = pulgadas / 63360
        print(millas)
    elif opcion == "5":
        pies = pulgadas / 12
        print(pies)
    else:
        print("Opción no válida.")
elif(opcion=="7"):
    print("Saliendo...")
else:
    print("INCORRECTO")










          
    
