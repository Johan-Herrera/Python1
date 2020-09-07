edadAct=input("Ingrese su edad actual")
añoAct=input("ingrese el año actual")

def calcularEdad2070(edadActual,añoActual):
    edad2070=2070-int(añoActual)+(int(edadActual))
    return edad2070

edad2070=calcularEdad2070(edadAct,añoAct)
print("Su edad en el 2070 sera de : "+str(edad2070))
