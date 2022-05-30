# Calculadora con condicionales #
# ver https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/condicional_if.html #

a = input("Ingrese el primer numero: ")
b = input("Ingrese el segundo numero: ")

print("Seleccione una opcion: ")
print(" 1.SUMA ")
print(" 2.RESTA ")
print(" 3.MULTIPLICACION ")
print(" 4.DIVISION ")

o = input(" ")

aCast = int(a)
bCast = int(b)
oCast = int(o)

if oCast == 1 :

    rSum = aCast + bCast
    print("El resultado de la SUMA es:", rSum)

elif oCast == 2 :

    rRest = aCast - bCast
    print("El resultado de la RESTA es:", rRest)
elif oCast == 3 :

    rMulti = aCast * bCast
    print("El resultado de la MULTIPLICCION es:", rMulti)
elif oCast == 4 :

    rDiv = aCast / bCast
    print("El resultado de la DIVISION es:", rDiv)
else :
    print("ERROR, OPCION NO DISPONIBLE")


