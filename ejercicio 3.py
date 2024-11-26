

letra = input("Ingrese una letra: ")
if len(letra) != 1:
    print("Debe ingresar un solo carácter.")
elif letra.lower() in "aeiou":
    print("Es vocal.")
else:
    print("No es vocal.")
