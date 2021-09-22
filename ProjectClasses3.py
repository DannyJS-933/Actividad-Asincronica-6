#Implementra un clase para los siguientes conceptos:
#mesa, persona, revista, camisa

class Mesa:
    def __init__(self, precio, ubicacion):
        self.precioMesa = precio
        self.ubicacionMesa = ubicacion


    @property
    def forma(self):
        print(f'Esta mesa se ubica en {self.ubicacionMesa} y tiene un precio de {self.precioMesa}')
        return self.precioMesa

    @forma.setter
    def valores(self, medida):
        self.medidaMesa = medida
        print (f'La mesa tiene una medida de {self.medidaMesa}')



mesa = Mesa('$259', 'Meeting Room')
mesa.forma
mesa.valores = '183 x 76'

#--------------Clase para Persona----------------

class Persona:
    def __init__(self, edad, genero, profesion):
        self.edadPersona = edad
        self.generoPersona = genero
        self.profesionPersona = profesion

    @property
    def propiedades_persona(self):
        print(f'La persona tiene una edad de {self.edadPersona}, su genero es {self.generoPersona} y su profesion es {self.profesionPersona}')

    @propiedades_persona.setter

    def nuevas_propiedades(self, nombre):
        self.nombrePersona = nombre
        return self.nombrePersona

#Aqui utilizamos solo el atributo nombrePersona para extraer el dato que necesitamos
persona = Persona('30', 'Femenino', 'Developer')
persona.propiedades_persona
persona.nombrePersona= 'Julia'
print(persona.nombrePersona)

#--------------Clase para revista------------------

class Revista:
    def __init__(self, tema, editorial, fecha):
        self.revistaTema = tema
        self.revistaEditorial = editorial
        self.fechaRevista = fecha

    @property

    def propiedades_revista(self):
        print(f'El tema de la revista es {self.revistaTema}, la editorial es * {self.revistaEditorial} * y su fecha de creacion es {self.fechaRevista}')

    @propiedades_revista.setter

    def nuevas_propiedades(self, precio):
        self.precioRevista = precio
        print(f'El precio de la revista es {self.precioRevista}')


revista = Revista('Programacion', 'Documento oficial de Python', '2020')
revista.propiedades_revista
revista.nuevas_propiedades= '1500'

#------------------Clase para la camisa-----------------------

class Camisa:
    def __init__(self, talla, color, estilo):
        self.tallaCamisa = talla
        self.colorCamisa = color
        self.estiloCamisa = estilo

    @property

    def propiedades_camisa(self):
        print(f'La talla de la camisa es {self.tallaCamisa}, el color de la camisa es {self.colorCamisa} y su estilo es {self.estiloCamisa}')

    @propiedades_camisa.setter

    def nuevas_propiedades(self, precio):
        self.precioCamisa = precio
        print(f'El precio de la camisa es {self.precioCamisa}')

camisa = Camisa('L', 'Negro', 'Polo' )
camisa.propiedades_camisa
camisa.nuevas_propiedades = '10000 colones'




