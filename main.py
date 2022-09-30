
class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre 
        self.apellido=apellido
        self.dni=dni 

class Personaservice:
    def __init__(self):
        self.personas=[]
    def add(self,a): 
        self.personas.append(a)
    def delete(self,a):
        self.personas.remove(a)
    #para actualizar voy a tener dos parametros de entrada
    #a es el objeto a remplazar, b son los nuevos valores    
    def update(self,a,b):
        for i in range(len(self.personas)):
            if b.dni == self.personas[i].dni:
                self.personas[i] = b
    #ingresa dni, sale objeto persona si es que existe
    def findByDocumento(self,a):
        for i in range(len(self.personas)):
            if a == self.personas[i].dni:
                return self.personas[i]
            else:
                return None
    #metodo que devuelve toda la lista             
    def findAll(self):
        return self.personas
    #carga los elementos del block a la lista
    def loadfile(self):    
        file = open('C:/Users/USUARIO/Documents/personaservice',"r")
        for line in file:
            self.personas.append(Persona(line.split(",",3)[0],line.split(",",3)[1],line.split(",",3)[2])) 
        file.close()
     #escribe los elementos del block en la lista
    def writefile(self):
        file = open('C:/Users/USUARIO/Documents/personaservice.txt',"w")
        for i in range(len(self.personas)):
            file.write("{},{},{}, \n".format(self.personas[i].nombre, self.personas[i].apellido, self.personas[i].dni))
        file.close()



