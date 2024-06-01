from tkinter import Tk, Label, Button, Entry

#Funciones

"""def Seguimos():
    text2.delete(0, "end")
    text3.delete(0, "end")
    text4.delete(0, "end")
    text6.delete(0, "end")
    text7.delete(0, "end")
    text8.delete(0, "end")
    text9.delete(0, "end")
    
def Salir():
    break

def Juego():
    from random import randint

    eleccion = ["piedra", "papel", "tijera"]

    def main():
        compu = eleccion[randint(0,2)]

        print("Juguemos a piedra, papel o tijera")
        jugador = input("Elegí: ").lower()
        print(f"La compu eligió: {compu}")

        if jugador == compu:
            print("Empate")
        elif jugador == "piedra" and compu == "papel":
            print("La compu ganó")
        elif jugador == "piedra" and compu == "tijera":
            print("Ganaste")
        elif jugador == "tijera" and compu == "papel":
            print("Ganaste")
        elif jugador == "tijera" and compu == "piedra":
            print("La compu ganó")
        elif jugador == "papel" and compu == "tijera":
            print("La compu ganó")
        elif jugador == "papel" and compu == "piedra":
            print("Ganaste")
        elif jugador != "papel" or jugador != "tijera" or jugador != "piedra":
            print("Elige una opción válida por favor")
        
        main ()

    main()"""

#Ventana
Ventana = Tk()
Ventana.title("Juego de Piedra, Papel, Tijera")
Ventana.geometry("400x400")
Ventana.config(bg="pink")

#Jugador 1
label0 = Label(Ventana, text="Jugador 1",fg="blue",bg="yellow")
label0.place(x=30,y=10,width=100,height=30)
txt0 = Entry(Ventana, bg="white")
txt0.place(x=160,y=10,width=100,height=30)

label1 = Label(Ventana, text="Marca con X tu elección",fg="yellow",bg="purple")
label1.place(x=30,y=60,width=200,height=30)

label2 = Label(Ventana, text="Piedra",bg="gray")
label2.place(x=30,y=120,width=100, height=30)
txt2 = Entry(Ventana, bg="white")
txt2.place(x=65,y=150,width=30,height=30)

label3 = Label(Ventana, text="Papel",bg="white")
label3.place(x=150,y=120,width=100, height=30)
txt3 = Entry(Ventana, bg="white")
txt3.place(x=180,y=150,width=30,height=30)

label4 = Label(Ventana, text="Tijera",bg="#69f30e")
label4.place(x=270,y=120,width=100, height=30)
txt4 = Entry(Ventana, bg="white")
txt4.place(x=310,y=150,width=30,height=30)

#Jugador 2
label5 = Label(Ventana, text="Jugador 2",fg="red",bg="white")
label5.place(x=30,y=200,width=100,height=30)
txt0 = Entry(Ventana, bg="white")
txt0.place(x=160,y=200,width=100,height=30)

label6 = Label(Ventana, text="Piedra",bg="gray")
label6.place(x=30,y=250,width=100, height=30)
txt6 = Entry(Ventana, bg="white")
txt6.place(x=65,y=280,width=30,height=30)

label7 = Label(Ventana, text="Papel",bg="white")
label7.place(x=150,y=250,width=100, height=30)
txt7 = Entry(Ventana, bg="white")
txt7.place(x=180,y=280,width=30,height=30)

label8 = Label(Ventana, text="Tijera",bg="#69f30e")
label8.place(x=270,y=250,width=100, height=30)
txt8 = Entry(Ventana, bg="white")
txt8.place(x=310,y=280,width=30,height=30)

#Resultado
label9 = Label(Ventana, text="Ganador",bg="orange")
label9.place(x=30,y=340,width=100,height=30)
txt9 = Entry(Ventana, bg="white")
txt9.place(x=160,y=340,width=100,height=30)

button1 = Button(Ventana, text="¿Seguimos?",command=Button)
button1.place(x=310,y=330,width=80,height=20)

button2 = Button(Ventana, text="Salir",command=Button)
button2.place(x=310,y=360,width=80,height=20)

Ventana.mainloop()
