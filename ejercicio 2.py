import math
print("Cálculo de las raíces de una ecuación cuadrática: ")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

parte1= b**2 - 4*a*c

if parte1> 0:
    raiz1 = (-b + math.sqrt(parte1)) / (2*a)
    raiz2 = (-b - math.sqrt(parte1)) / (2*a)
    print(f"Las raíces reales son: {raiz1} y {raiz2}")
elif parte1 == 0:
    raiz = -b / (2*a)
    print(f"La ecuación tiene: {raiz}")
else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(-parte1) / (2*a)
    print(f"Las raíces complejas son: {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i")

