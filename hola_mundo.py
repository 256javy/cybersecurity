# 1. Imprime "Hola, mundo"

print( "Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Javier"

print( "Hola,", nombre ) # con una coma

print( "Hola, " + nombre ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 256

print( "Hola", numero, "!" ) # con una coma

print( "Hola " + str(numero) + "!" ) # con un + -- corregido con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "pizza"

comida2 = "papas fritas"

print( "Me encanta comer {} y {}".format(comida1, comida2)) # con .format()

print( f"Me encanta comer {comida1} y {comida2}") # con una cadena f

# BONUS NINJA: Busca otros métodos de cadena y utilízalos en el archivo. ¡Existen muchísimas opciones para esto!
# algunas de https://docs.python.org/3/library/stdtypes.html#string-methods :

# imprimir en mayúsculas

print( "Me encanta comer {} y {}".upper().format(comida1.upper(), comida2.upper())) # con .upper()

# reemplaza "Me encata" por "A quien no le gusta"

print( "Me encanta comer {} y {}".replace("Me encanta", "A quien no le gusta").format(comida1, comida2)) # con .replace()

# capitalize

print( "Me encanta comer {} y {}".capitalize().format(comida1.capitalize(), comida2.capitalize())) # con .capitalize()

# isprintable

print( "Me encanta comer".isprintable() ) # con .isprintable()

# title

print( "Me encanta comer {} y {}".format(comida1, comida2).title() ) # con .title()

