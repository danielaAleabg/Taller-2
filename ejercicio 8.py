numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número entero #{i + 1}: "))
    numeros.append(numero)
sum_negativos = 0
positivos = []
for num in numeros:
    if num < 0:
        sum_negativos += num
    elif num > 0:
        positivos.append(num)
if len(positivos) > 0:
    promedio_positivos = sum(positivos) / len(positivos)
    print(f"Promedio de los números positivos: {promedio_positivos}")
else:
    print("No se ingresaron números positivos.")
print(f"Sumatoria de los números negativos: {sum_negativos}")
