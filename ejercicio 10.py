cadena = input("Ingrese una cadena: ")
mayusculas = 0
for char in cadena:
    if char.isupper():
        mayusculas += 1

print(f"La cadena tiene {mayusculas} letra/s mayuscula/s.")
