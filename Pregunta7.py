#Pregunta 7
from datetime import date, time, datetime
class Mi_Tiempo():
    def __str__(self):
        return f'{self.horas}:{self.minutos}:{self.segundos}'

    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

hora1= str(Mi_Tiempo(12,15,20))
print(hora1)
hora1_object= datetime.strptime(hora1, '%H:%M:%S')
print(hora1_object)

hora2 = str(Mi_Tiempo(16,15,20))
print(hora2)

hora2_object= datetime.strptime(hora2, '%H:%M:%S')
print(hora1_object)

print('la diferencia en horas es %s'%(hora2_object.hour-hora1_object.hour))



