from numpy import cos,sin,pi
from math import tan
Operacion= input('operacion ')
gravedad= 9.81

def Peso_Masa():
    Peso= float(input('¿Cual es el peso?'))
    Masa= Peso/gravedad

def Volumen_poligono():
    Forma = input('¿Es un Prisma, Piramide, Cono, Cilindro?')
    if(Forma == 'Prisma'):
        Base = float(input('inserta el valor de la base ')) 
        Altura= float(input('inserta el valor de la altura '))
        Volumen_poligono = (Base*Altura)
    if(Forma == 'Piramide'):
        Base = float(input('inserta el valor de la base ')) 
        Altura= float(input('inserta el valor de la altura '))
        Volumen_piramide = Base*Altura/3
    if(Forma == 'Cono'):
        pregunta1= input('¿Tienes Radio o Diametro?')
        if(pregunta1 == 'Radio'):
            print('usaremos radio')
            Radio=float(input('inserta el Radio'))
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi/3*Radio**2*Altura
        
        elif(pregunta1 == 'Diametro'):
            print('usaremos diametro')
            Diametro=float(input('inserta el Diametro'))
            Diametro = Diametro/2
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi/3*Diametro**2*Altura

    if(Forma == 'Cilindro'):
        pregunta1= input('¿Tienes Radio o Diametro?')
        if(pregunta1 == 'Radio'):
            print('usaremos radio')
            Radio=float(input('inserta el Radio'))
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi*Radio**2*Altura
        
        elif(pregunta1 == 'Diametro'):
            print('usaremos diametro')
            Diametro=float(input('inserta el Diametro'))
            Diametro = Diametro/2
            Altura=float(input('inserta la altura'))
            Volumen_poligono = pi*Diametro**2*Altura

def calculadora_Densidad():
    print('esto podemos calcular')
    print('Densidad, Masa, Volumen')
    cal_valor = input('¿cual quieres calcular?')
    
    if(cal_valor == 'Densidad'):
        print('¿conoces el volumen o lo tienes que calcular?')
        respuesta= input('Si o No')
        if( respuesta == 'Si'):
            magnitud1 = float(input('inserta la masa'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'No'):
            respuesta2= input('¿tienes Area o Medidas?: ')
            if(respuesta2 == 'Area'):
                Volumen_poligono()
                print(Volumen_poligono + 'usalo en la ecuacion')
                magnitud1 = float(input('inserta la masa'))
                magnitud2 = float(input('inserta la Volumen'))

            if(respuesta2 == 'Medidas'):
                print('perdon estamos trabajando en ello')

    elif(cal_valor == 'Masa'):
        print('¿conoces el volumen o lo tienes que calcular?')
        respuesta= input('Si o No')
        if( respuesta == 'Si'):
            magnitud1 = float(input('inserta la masa'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'No'):
            respuesta2= input('¿tienes Area o Medidas?: ')
            if(respuesta2 == 'Area'):
                Volumen_poligono()
                print(Volumen_poligono + 'usalo en la ecuacion')
                magnitud1 = float(input('inserta la Densidad'))
                magnitud2 = float(input('inserta la Volumen'))
                print(magnitud1*magnitud2)
            if(respuesta2 == 'Medidas'):
                print('perdon estamos trabajando en ello')
   
    elif(cal_valor == 'Volumen'):
        print('¿conoces la Masa o el Peso?')
        respuesta= input('Masa o Peso')
        if(respuesta == 'Masa'):
            magnitud1 = float(input('inserta la Densidad'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
        if(respuesta == 'Peso'):
            Peso_Masa()
            print(Peso_Masa +'usa la Masa para calcular el Volumen')
            magnitud1 = float(input('inserta la Densidad'))
            magnitud2 = float(input('inserta la Volumen'))
            print(magnitud1/magnitud2)
            


def Longitud():

    print('esto es lo que podemos convertir')

    tipo_conversion1=input('¿que quieres converitir?')
    medida1=float(input('inserta la longitud que quieres convertir'))
    
    if(tipo_conversion1=='centimetros a pulgadas' or tipo_conversion1=='cm a in'):
        print(str(medida1*2.5)+' in')
    
    elif(tipo_conversion1 == 'pulgadas a centimetros' or tipo_conversion1=='in a cm'):
        print(str(medida1/2.5)+' cm')
    
    elif(tipo_conversion1 == 'metros a pies' or tipo_conversion1=='m a ft'):
        print(str(medida1*3.281) + ' ft')
    
    elif(tipo_conversion1 == 'pie a metros'or tipo_conversion1=='ft a m'):
        print(str(medida1/.3048) + ' m')
    
    elif(tipo_conversion1 == 'kilometros a millas' or tipo_conversion1=='Km a milles'):
        print(str(medida1*1.609) + 'milles')
    
    elif(tipo_conversion1 == 'metros a millas' or tipo_conversion1=='m a milles'):
        print(str(medida1*1609.344) + 'milles')

def Tiempo():
    print('esto es lo que podemos convertir')
    print('segundo a hora, hora a segundo, segundos en un dia, segundos en un año')
    tipo_conversion1=input('¿Que quieres convertir?')
    valor1= float(input('Cuanto '))
    if(tipo_conversion1 == 'segundo a hora' or tipo_conversion1=='S a H'):
        return(valor1*60)
    if(tipo_conversion1 == 'hora a segundo' or tipo_conversion1=='H a S'):
        return(valor1/60)
    if(tipo_conversion1 == 'segundos en un dia'):
        return(valor1*3600)
    if(tipo_conversion1 == 'segundos en un año'):
        return(valor1*3600*365)
        



while True:
    if(Operacion== 'Calcular densidad'):
        calculadora_Densidad()

    if(Operacion== 'Conversion de unidades'):
        print('Esto es lo que podemos convertir')
        print('Volumen','Area','Tiempo','Peso','Masa','Longitud','Velocidad','Fuerza','Potencia','Densidad', 'Energia','Presion')
        tipo_conversion= input('tipo de unidad ')

        if(tipo_conversion=='Longitud'):
            Longitud()

        elif(tipo_conversion=='Tiempo'):
            Tiempo()
        
        elif(tipo_conversion=='Area'):
            Area()
            