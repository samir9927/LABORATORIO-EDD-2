numero = input("Ingrese un número: ")
lista_digitos=list(numero)

suma= sum ([int(c) for c in numero])
print(f"La suma de digitos del Número {numero} es {suma}")