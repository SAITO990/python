#Ciclo For
foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'graves']

for food in foods:
    print(food)


#Validaciones dentro de un bucle
for food in foods:
    if food == 'cheese':
        print("Tienes que comprar esto")
    print(food)


#Como detener un bucle
for food in foods:
    if food == 'cheese':
            break
    print(food)


#Ejemplo de bucles con un rango
for number in range(1,20):
    print(number)


#Ejemplo de bucles con un string
for letter in "Hello":
    print(letter)


#Ciclo While
count =  0

while count <= 10:
    print(count)
    count = count + 1