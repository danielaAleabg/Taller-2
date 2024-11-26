num1 = int(input("Ingrese un número entero: "))
while True:
    num2 = int(input("Ingrese otro número entero: "))
    
    if num2 < num1:
        print(f"El número {num2} es menor que el anterior {num1}.")
        break
    
