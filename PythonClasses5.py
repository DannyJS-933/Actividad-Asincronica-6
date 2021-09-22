#Implementar clases para el cubo, cilindro y un cono, ademas obtener los volumenes.
import math
import time
from fractions import Fraction

class Cubo:
    def volumen_cubo(self):
        self.lado = int(input('Ingrese un valor: '))
        self.resultado = self.lado ** 3
        print(f'El volumen del cubo es: {self.resultado} ')

    def area_cubo(self):
        self.area = int(input('Ingrese un valor: '))
        self.resultadoArea = 6 * self.area ** 2
        print(f'El area del cubo es: {self.resultadoArea}')

class Prisma:
    def volumen_prisma(self):
        self.largo = int(input('Ingrese la medida del largo: '))
        self.ancho = int(input('Ingrese la medida del ancho: '))
        self.altura = int(input('Ingrese la medida de la altura: '))
        self.resultadoPrisma = self.largo * self.ancho * self.altura
        print(f'El volumen del prisma es {self.resultadoPrisma}')

    def area_prisma(self):
        self.areaLaterla = int(input('Ingrese el area lateral: '))
        self.areaBase = int(input('Ingrese el area de la base: '))
        self.resultadoPrismaArea = self.areaLaterla * self.areaBase * 2
        print(f'El area del prisma es {self.resultadoPrismaArea}')

class Cilindro:

    def volumen_cilindro(self):
        self.altura = int(input('Ingrese el valor de la altura: '))
        self.radio = int(input('Ingrese el valor del radio: '))
        self.resultadoCilindro = math.pi * self.altura * (self.radio ** 2)
        print(f'El volumen del cilindro es: {self.resultadoCilindro}')

    def area_cilindro(self):
        self.alturaCilindro = int(input('Ingrese la altura del cilindro: '))
        self.radioCilindro = int(input('Ingrese el radio del cilindro: '))
        self.resultadoAreaCilindro = 2 * math.pi * self.radioCilindro * self.alturaCilindro + 2 * math.pi * (self.radioCilindro ** 2)
        print(f'El area del cilindro es {self.resultadoAreaCilindro}')

class Piramide:
    def volumen_piramide(self):
        self.base = int(input('Ingrese el valor de la base: '))
        self.altura = int(input('Ingrese el valor de la altura: '))
        self.fraction = Fraction(1, 3)
        self.resultado = self.fraction * self.base * self.altura
        print(f'El volumen de la piramide es {self.resultado}')

    def area_piramide(self):
        self.baseTriangulo = int(input('Ingrese la medida de la base de uno de los triangulos: '))
        self.alturaTriangulo = int(input('Ingrese la medida de la altura de uno de los triangulos: '))
        self.resultadoAreaTriangulo = (self.baseTriangulo * self.alturaTriangulo) / 2
        print(f'Primero calculamos el area de uno de los triangulos, seria {self.baseTriangulo} * {self.alturaTriangulo} y el resultado es {self.resultadoAreaTriangulo}')
        time.sleep(3)
        self.resultadoFinal = self.resultadoAreaTriangulo * 4
        print(f'El area total de la piramide es {self.resultadoFinal}')

class Cono:
    def volumen_cono(self):
        self.fraction = Fraction(1, 3)
        self.radio = int(input('Ingrese el radio: '))
        self.altura = int(input('Ingrese la altura: '))
        self.resultado = self.fraction * math.pi * (self.radio) ** 2 * self.altura
        print(f'El volumen del cono es {self.resultado}')

    def area_cono(self):
        self.radioCono = int(input('Ingrese el radio: '))
        self.alturaCono = int(input('Ingrese la altura: '))
        self.resultadoAreaCono = math.pi * self.radioCono * self.alturaCono + math.pi * (self.radioCono ** 2)
        print(f'El area del cono es {self.resultadoAreaCono}')




Cubo().volumen_cubo()
Cubo().area_cubo()
Prisma().volumen_prisma()
Prisma().area_prisma()
Cilindro().volumen_cilindro()
Cilindro().area_cilindro()
Piramide().volumen_piramide()
Piramide().area_piramide()
Cono().volumen_cono()
Cono().area_cono()