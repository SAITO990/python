myStr =  "Hello World"

#Concatenacion de strings
print("Mi primer " + myStr + " en python")
print(f"Mi primer {myStr}")
print("Mi primer {0}".format(myStr))

#dir no permite ver una lista de atributos del objeto que se llama
print (dir(myStr))

#Upper convierte el texto en mayuscula
print(myStr.upper())

#lower convierte el texto en minuscula
print(myStr.lower())

#Swapcase cambia el texto a minuscula o mayuscula dependiendo de como se habia escrito antes
print(myStr.swapcase())

#Capitalize convierte la primera letra en mayuscula y el resto del texto queda en minuscula
print(myStr.capitalize())

#El método replace() reemplaza una frase específica con otra frase específica
print(myStr.replace('Hello' , 'bye'))

#El método count() devuelve el número de elementos con el valor especificado.
print(myStr.count('l'))

#El método startswith() devuelve True si la cadena comienza con el valor especificado; de lo contrario, False.
print(myStr.startswith('Hello'))

#El método Endswith() devuelve True si la cadena termina con el valor especificado; de lo contrario, False.
print(myStr.endswith('world'))

#El método split() divide una cadena en una lista, Puede especificar el separador, el separador predeterminado es cualquier espacio en blanco.
print(myStr.split())

#El método find() encuentra la primera aparición del valor especificado.
print(myStr.find('H'))

#La función Python len() devuelve la longitud de la cadena.
print(len(myStr))

#El método index() devuelve el índice del elemento especificado en la lista.
print(myStr.index('e'))

#El método isnumeric() devuelve True si todos los caracteres son numéricos (0-9), de lo contrario, False.
print(myStr.isnumeric())

#El método isalpha() devuelve True si todos los caracteres son letras del alfabeto (a-z).
print(myStr.isalpha())