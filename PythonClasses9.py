#Ejercicio 9
#
class Rectangulo:
    def perimetro(self,):
        self.largo = 1
        self.ancho = 1
        self.calcularPerimetro = (self.largo * 2) + (self.ancho * 2)

    def area(self):
        self.largo = 1
        self.ancho = 1
        self.calcularArea = self.largo * self.ancho

    @property
    def ingresar_datos(self):
        self.ingresarLargo = int(input('Ingrese el largo: '))
        self.ingresarAncho = int(input('Ingresar el ancho: '))
        print(f'El valor de largo es {self.ingresarLargo} y el ancho {self.ingresarAncho}')
        return {self.ingresarLargo, self.ingresarAncho}

    @ingresar_datos.setter
    def validar_largo(self, largo):
        largo1, largo2 = largo
        #self.ancho = ancho

        if 0.0 <= largo1 <= 20.0 and 0.0 <= largo2 <= 20.0:
                print('Bien')

        else:
            print('mal')

    def es_cuadrado(self, largo1, largo2):
        self.largo = largo1
        self.ancho = largo2
        # self.ancho = ancho

        if self.largo == self.ancho:
            print('Cuadrado')
            return True

        else:
            print('Rectangulo')
            return False





llamandoClase = Rectangulo()
llamandoClase.ingresar_datos
llamandoClase.validar_largo = (-1, -3)
llamandoClase.es_cuadrado(3,3)


