import unittest

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
            if a.dni == self.personas[i].dni:
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
    #carga los elementos del bloc a la lista
    def loadfile(self):    
        file = open('C:/Users/USUARIO/Documents/personaservice',"r")
        for line in file:
            self.personas.append(Persona(line.split(",",3)[0],line.split(",",3)[1],line.split(",",3)[2])) 
        file.close()
     #escribe los elementos del bloc en la lista
    def writefile(self):
        file = open('C:/Users/USUARIO/Documents/personaservice.txt',"w")
        for i in range(len(self.personas)):
            file.write("{},{},{}, \n".format(self.personas[i].nombre, self.personas[i].apellido, self.personas[i].dni))
        file.close()


class TestApp(unittest.TestCase):
    
    def test_add(self):
        repo1=Personaservice()
        persona1=Persona("pepe","honguito",123)
        repo1.add(persona1)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona1] })
        
    def test_delete(self):
        repo1=Personaservice()
        persona1=Persona("fulano","mengano",864)
        repo1.add(persona1)
        repo1.delete(persona1)
        self.assertDictEqual(repo1.__dict__,{'personas': [] })

    def test_update(self):
        repo1=Personaservice()
        persona1=Persona("cualquier","cosa",000)
        persona2=Persona("alberto","cortez",85)
        repo1.add(persona1)
        repo1.update(persona1,persona2)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona2] })

    def test_findbydocumento_sucess(self):
        repo1=Personaservice()
        persona1=Persona("huang","lee", 32467)
        repo1.add(persona1)
        self.assertEqual(persona1,repo1.findByDocumento(32467))

    def test_findbydocumento_failed(self):
        repo1=Personaservice()
        persona1=Persona("huang","lee", 32467)
        repo1.add(persona1)
        self.assertEqual(None,repo1.findByDocumento(00000))

    def test_findAll(self):
        repo1=Personaservice()
        persona1=Persona("frederik","weber", 8976)
        persona2=Persona("kate","denson", 5681)
        repo1.add(persona1)
        repo1.add(persona2)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona1,persona2] })

if __name__ == '__main__':
    unittest.main()