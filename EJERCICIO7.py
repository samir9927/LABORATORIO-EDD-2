def sumaPares(inicio, fin):
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

inicio_rango = int(input("Ingrese el inicio del rango: "))
fin_rango = int(input("Ingrese el final del rango: "))

resultado = sumaPares(inicio_rango, fin_rango)


print(f"La suma de los números pares en el rango [{inicio_rango}, {fin_rango}] es: {resultado}")
