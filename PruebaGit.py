print("Hola Mundo")   #debo guardar la versión que quiero subir

#git init =iniciaste un repositorio local en la carpeta donde estás parado.

#alumnos={"Amir":{"DNI":43242324","FN":"03/03/2003","Nota":"6"}}
                 
#primero van los def y después 

"""while True:
    try: 
        x=int(input("ingrese un número"))
        break

    except ValueError:
        print("Debe ingresar un número")"""


#Clase de cómo manejar errores y excepciones (esto debe estar en los proyectos finales)

try: 
    x=int(input("ingrese un número "))          #un código robusto maneja todos los errores
    x=x/0

except ValueError:
    print("Debe ingresar un número ")

except TypeError:
    print("Algo falló")

except Exception as e:
    print(e)

print("hola mundo")
    



