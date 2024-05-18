#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3).

"""def redondear():
    numero=float(input("Escriba un número decimal: "))
    if numero-(int(numero))>=0.50:
        print(f"El entero es: {int(numero)+1}")
    else:
        print(f"El entero es: {int(numero)}")

redondear()

def redondear(numero):
    if numero-(int(numero))>=0.50:
        print(f"El entero es: {int(numero)+1}")
    else:
        print(f"El entero es: {int(numero)}")
        
redondear()"""
    
#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

"""def suma():
    lista=[]
    suma=0
    from packs import redondear

    for i in range (3):
        dec=float(input("Ingrese un número decimal: "))
        lista.append(dec)
    print(lista)

    for elemento in lista:
        suma += elemento
    print(suma)
    
    redondear(print(suma))
    
suma()   #No verificado"""

#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema.

"""import datetime

print(datetime.datetime.now())"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

"""from packs import random

print(random.randrange(2,11,2))"""

#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica.

"""import random

opciones=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde",
"Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no",
"Mis fuentes me dicen que no"]

Duda=input("Pregunta: ")
#Opción 1
print(opciones[random.randint(0,7)])
#Opción 2
print(random.choice(opciones))"""

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)

"""import time

INCOMPLETO"""

#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.

"""import random

papeles=["Andrea","Ramón","Celeste","Carlos","Josefina","Pía"]
print(random.choice(papeles))"""

#8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
#nacimiento y sea capaz de devolver la cantidad de días desde su
#nacimiento hasta hoy.

"""def calcular_dias():

    from packs import datetime
   
calcular_dias()"""

#9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario.
