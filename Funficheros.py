
      #Funciones de un fichero#
# r : Lectura
#a : Append(Agregar al final)
#w : Escritura(Crear un nuevo fichero)
#x : Create

#t : Texto
#b :  Binary

# +

# f.readline() Lee una sola linea
#f.readlines() Lee todo el fichero como si fuera una lista 
# f.read()  Lee todo el fichero a menos que le pasemos un parámetro
""" 
f = open('hol.txt', 'r')  #De esta manera se lee un fichero
datos = f.read()
f.close()
print(datos)
"""
f = open('wachin.txt', 'w')  #De esta manera se crea un fichero nuevo
f.write('que hay wey')
f.close()

f = open('wachin.txt', 'a') #De esta manera se agrega lo que queramos al final del fichero
f.write('\nChapa mal clavada, vuela')
f.close()




    





