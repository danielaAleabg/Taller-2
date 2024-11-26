salario_minimo = 1160000  
nombre = input("Ingrese el nombre del empleado: ")
apellido = input("Ingrese el apellido del empleado: ")
documento = input("Ingrese el documento de identidad: ")
sueldo = float(input("Ingrese el sueldo del empleado: "))

if sueldo > salario_minimo:
    print(f"{nombre} {apellido} (Documento: {documento}) gana un sueldo superior al salario mínimo.")
else:
    print(f"{nombre} {apellido} (Documento: {documento}) no gana un sueldo superior al salario mínimo.")
