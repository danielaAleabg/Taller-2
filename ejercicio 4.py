import math 
print("-------------\nMenú Calculadora-----------")
print("""1. Suma.
         2. Resta.
         3. Multiplicación.
         4. División.
         5. Comparar números pares e impares.
         6. Porcentajes.
         7. Razones trigonométricas.
         8. Salir""")

opcion = input("Seleccione una opción: ")

if opcion=="1":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"El resultado de la suma es: {num1 + num2}")
elif opcion == "2":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"El resultado de la resta es: {num1 - num2}")
elif opcion == "3":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"El resultado de la multiplicación es: {num1 * num2}")
elif opcion == "4":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        print(f"El resultado de la división es: {num1 / num2}")
    else:
        print("No se puede dividir entre cero.")
elif opcion == "5":
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
elif opcion == "6":
    num = float(input("Ingrese el número: "))
    porcentaje = float(input("Ingrese el porcentaje: "))
    print(f"El porcentaje de {num} es {num * (porcentaje / 100)}")

elif opcion == "7":
    angulo = float(input("Ingrese un ángulo en grados: "))
    print("""----MENÚ----
            1. SENO
            2. COSENO
            3. TANGENTE""")
    opcion=input("¿Qué deseas hallar: ")
    if (opcion=="1"):
        print(f"Seno: {math.sin(math.radians(angulo))}")
    elif opcion=="2":
        print(f"Coseno: {math.cos(math.radians(angulo))}")
    elif opcion=="3":
        print(f"Tangente: {math.tan(math.radians(angulo))}")
    else:
        print("Opcion incorrecta")
elif opcion=="8":
    print("Saliendo...")
else:
    print("Opcion INCORRECTA")
