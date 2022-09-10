import pickle

class Vehiculo:

    def __init__(self, name, price, doors):
        self.name = name
        self.price = price
        self.doors = doors


    def getNombre(self):
        print( f'El auto es un {self.name}')

    def getPrice(self):
        print(f'El auto cuesta {self.price}')



a1 = Vehiculo('Dodge Charger', '25.000', 4)
a1.getNombre()
a1.getPrice()



f = open('clase.bin', 'wb') #Este comando crea un archivo binario
pickle.dump(a1, f)              #Este comando guarda la clase en el archivo
f.close

f = open('clase.bin', 'rb') #Este comando lee el archivo binario
a = pickle.load(f)              #Este comando carga lo que hay dentro del archivo
f.close()

a.getPrice()




