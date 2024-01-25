def factorial(numero):

    if numero == 0:
        return 1

    else:
        return numero * factorial(numero - 1)


numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

if numero_ingresado >= 0:

    resultado = factorial(numero_ingresado)
    print(f"El factorial de {numero_ingresado} es: {resultado}")

else:
    print("El factorial solo está definido para números no negativos.")