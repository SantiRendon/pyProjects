# |como castear variables STRING a INT en python|
# ver https://ellibrodepython.com/casting-python #

x = input("Ingrese el primer numero: ")
Y = input("Ingrese el segundo numero: ")

result = (x+Y)
print("resultado de (x+y) ANTES de castear:", result)

# convirtiendo String a int con 'int()'
xCast = int(x)
yCast = int(Y)
resultCast = (xCast + yCast)

print("resultado de (x+y) DESPUES de castear:", resultCast)

