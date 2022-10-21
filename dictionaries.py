#Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values


#Ejemplos de diccionarios 
product = {
    "name" : "book",
    "cantidad" : 3,
    "precio" : 4.99
}

person = {
    "first_name" : "andres",
    "last_name" : "felipe"
}


#Como ver los tipos de datos en un diccionario
print(type(product))

#Comon ver los metodos de un diccionario
print(dir(person))



#METODOS EN UN DICCIONARIO


#Como imprimir solo las claves dentro de un diccionario
print(person.keys())

#Como obtener solo los items 
print(person.items())

#Como eliminar un diccionario
del product
print(person)

#Como limpiar los elementos de un diccionarios\
person.clear()
print(person)

#Podemos agrupar los diccionarios dentro de una lista
products = [
    {"name" : "book", "price" : 23.90},
    {"name" : "laptop", "price" : 1000}
]