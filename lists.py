from cgi import print_form
from turtle import color


demo_list = [1, "Hello", 1.4, True, [1,2,3]]
colors = ['red', 'green', 'blue']

#Creacion de listas usando un constructor
numbers_list = list((1,2,3,4))
print(type(numbers_list))

#Creacion de lista por medio de un rango
r  = list(range(1, 100))
print(r)

#Podemos obtener informacion de los tipos de datos
print(type(colors))
print(dir(colors))

#Longitus de una lista
print(len(demo_list))
print(len(colors))

#Obtencion de datos especificos en una lista
print(colors[1])
print(colors[-3])

#Verificacion de elementos dentro de una lista
print('green' in colors)#Esto nos puede devolver dos posibles valores True o False

#Como reemplazar valores en una lista
color[1] = 'yellow'
print(colors)



#METODOS DENTRO DE UNA LISTA


#Agregar valores a una lista con append, sin embargo debemos de tener en cuenta que solo recibe un valor
#asi que para enviar varios valores podemos convertir la lista en una tupla
colors.append(('violet', 'yellow'))
colors.extend(['white', 'pink', 'black'])
print(colors)

#Insertar valores en una posicion especifica
colors.insert(1, 'violet')
colors.insert(-1, 'orange')
colors.insert(len(colors), 'Aliceblue')
print(colors)

#Remover elementos de una lista, sin embargo pop solo elimina el ultimo elemento a no ser que le pasemos un indice [1]
colors.pop()
print(colors)

#Remover elementos especificos con remove
colors.remove('orange')
print(colors)

#Remover todos los elementos de una lista 
colors.clear()
print(colors)

#Ordenar elementos con sort
colors.sort()
colors.sort(reverse=True)

#Como obtener indices de una lista
colors.index('red')
colors.index('blue')

#Como obtener la cantidad de veces que un elemento se repite en una lista
colors.count('yellow')

