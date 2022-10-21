#Un set es una colección que no posee órden, y por tanto, tampoco números de índex. Esto quiere decir que no podemos decidir el orden en el cual aparecerán sus elementos.

from turtle import color


colors = {'red', 'green', 'blue'}
print(type(colors))

#Como comprobar si los datos existen dentro de un set
print('red' in colors)

#Como agregar datos a un set
colors.add('violet')
print(colors)

#Como remover elementos de un set
colors.remove('red')
print(colors)

#Como vaciar un set
colors.clear()
print(colors)

#Como eliminar un set
del colors