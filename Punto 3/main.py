palabra=input("Ingrese una palabra")
def imprimirPrimeraUltima(plb):
    primera=palabra[0]
    ultima=palabra[len(palabra)-1]
    return ("La primera letra es '"+primera+"' La segunda letra es '"+ultima+"'")
mensaje=imprimirPrimeraUltima(palabra)
print(mensaje)