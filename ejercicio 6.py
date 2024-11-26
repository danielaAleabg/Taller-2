print("""____MENÚ____
        1.A
        2.B
        3.C
        4.VOTO EN BLANCO""")
eleccion = input("Ingrese su elección: ")
if eleccion == "1":
    print("Usted ha votado por el candidato A.")
elif eleccion == "2":
    print("Usted ha votado por el candidato B.")
elif eleccion == "3":
    print("Usted ha votado por el candidato C.")
elif eleccion == "4":
    print("Usted ha realizado un voto en blanco.")
else:
    print("Opción errónea.")
