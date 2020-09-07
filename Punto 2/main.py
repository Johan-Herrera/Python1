numero = int(input("Ingrese un numero entero"))

def definirNumero(num):
    if num % 2 == 0:
        return('El número es par.')
    else:
        return('El número es impar.')

mensaje=definirNumero(numero)
print(mensaje)

