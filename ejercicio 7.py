nombres = []
num = int(input("Ingrese la cantidad de estudiantes a registrar: "))
for i in range(num):
    nombre = input(f"Ingrese el nombre del estudiante #{i + 1}: ").strip()
    nombres.append(nombre)
consulta = input("\nIngrese el nombre del estudiante para buscar: ").strip()
if consulta in nombres:
    print(f"{consulta} está en la lista.")
else:
    print(f"{consulta} no está en la lista.")
