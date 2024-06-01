"""1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido, fecha de nacimiento, DNI,
 Nombre de Tutor, registro de todas las notas, cantidad de faltas, cantidad de amonestaciones recibidas.

Recomendación: Para llevar un registro de estos dato se puede utilizar un diccionario estructurado de la 
siguiente manera:
{“Alumnos” : [alumno1,alumno2,alumno3 ]}
Donde cada alumno es otro diccionario estructurado de la
siguiente forma:
{“Nombre”: nombre de alumno,
“Apellido” : apellido de alumno,
“DNI” : DNI de alumno
“Fecha de nacimiento”, fecha de nacimiento de alumno,
“Tutor” : nombre y apellido de tutor,
“Notas” : todas las notas del alumno,
“Faltas” : cantidad de faltas,
“amonestaciones” : cantidad de amonestaciones}

En esta estructura:
Datos = {“Alumnos” : [alumno1,alumno2,alumno3 ]}
Para acceder por ejemplo al numero de DNI del tercer alumno podríamos hacer algo así:
Datos[“Alumnos”][2][“DNI”]
Este es un ejemplo de estructura, se puede cambiar completamente o hacer algunos cambios sobre el para mejorar
 el orden (si lo consideran necesario)
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos
RECOMEDACIONN GENERAL:
El programa es extenso, hacer por partes."""

#El diccionario se crea con el ingreso de datos del usuario.
alumnos={}
opcion=""

while opcion != "5":  #salir
    if opcion == "1":  #agregar
        lib=input("Escribe el número de libreta: ")
        apellido=input("Escribe el apellido: ")
        nombre=input("Escribe el nombre: ")
        dni=input("Escribe el DNI: ")
        born=input("Escribe la fecha de nacimiento: ")
        tutor=input("Escriba el tutor: ")
        faltas=input("Escribe la cantidad de faltas: ")
        sancion=input("Escribe la cantidad de amonestaciones: ")
        alumno={"Apellido":apellido,"Nombre":nombre,"DNI":dni,"Fecha Nacimiento":born,"Tutor":tutor,"Faltas":faltas,"Amonestaciones":sancion}
        alumnos[lib]=alumno

    if opcion == "2":  #mostrar
        lib=input("Escribe la libreta del alumno: ")
        if lib in alumnos:
            print("Libreta:",lib)
            for clave, valor in alumnos[lib].items():
                print(clave.title()+":",valor)
        else:
            print("No existe ese número de libreta")

    if opcion == "3":  #modificar
        lib=input("Escribe la libreta del alumno: ")
        if lib in alumnos:
            clave=input("Escriba dato a modificar: ")
            valor=input("Escriba la modificación: ")
            alumnos[clave]=valor
        else:
            print("No existe ese número de libreta")

    if opcion == "4":  #eliminar
        lib=input("Escribe la libreta del alumno: ")
        if lib in alumnos:
            del alumnos[lib]
        else:
            print("No existe ese número de libreta")

    opcion=input("Escribe una opción 1.Agregar 2.Mostrar 3.Modificar 4.Eliminar 5.Salir :  ")
