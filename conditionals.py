age =  20

if age < 30:
    print("El usuario es menor a 30 años")



x = 30

if x == 30: 
    print("x es igual a 30")



y = 10

if y < 20:
    print("x es menor que 20")
else:
    print("x es mayor que 20")



color = "blue"

if color == 'red':
    print("el color es rojo")
else:
    print("Es cualquier otro color menos rojo")



colors = "aliceblue"

if colors == "red":
    print("El color es rojo")
elif colors == "blue":
    print("El color es azul")
else:
    print("El color no coincide")



#Ejemplos con if

name = "Andres"
lastname = "Felipe"

if name == "Andres":
    if lastname == "Felipe":
        print("Bienvenido Andres Felipe")
    else:
        print("El nombre no coincide con Andres Felipe")
else:
    print("El nombre no coincide con Andres")  



x = 5
y = 7

if x > 2 and x <= 10:
    print("X es mayor que 2 y menor o igual que 10")
if x > 2 or x <=20:
    print("X es mayor que dos o menor o igual que 20")
if (not(x == y)):
    print("X no es igual a y")
