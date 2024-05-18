def redondear(numero):
    if numero-(int(numero))>=0.50:
        print(f"El entero es: {int(numero)+1}")
    else:
        print(f"El entero es: {int(numero)}")