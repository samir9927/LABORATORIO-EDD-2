def esPalindromo(palabra):
    palabra=palabra.replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    a=0
    b= len(palabra)-1

    for i in range (0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    
    return True

palabra = input ("Ingrese una palabra o una frase: ")

if esPalindromo(palabra):
    print("Es una palabra o frase palindroma")
else:
    print("No es una palabra o frase palindroma")