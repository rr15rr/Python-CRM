#Funcion de entrada y salida de datos (Menu de opciones)
def menu():
    print("""---Rafon Rentals---
          
Bienvenido al portal digital de Rafon Rentals!

1) Realizar una transaccion
2) Costos
3) Salir
""")
    
    opciones = int(input("Elije una opcion: "))

    try:    #Usamos try para manejo de errores
        if opciones == 3:   #Condiciones con if para el menu de opciones 
            print("\nGracias por usar el portal digital de Rafon Rentals, Saludos!\n")

        elif opciones == 1:
            transaccion()   #Pasamos a la funcion "Transaccion" para que el usuario pueda realizar transacciones
    
        elif opciones > 3:
            print("\nError, elije una opcion valida\n")
            menu()
        
        elif opciones == 2:
            costos()    #Pasamos a la funcion "costos" para que el usuario pueda saber costos por modelo

        else: 
            print("\nError, elije una opcion valida\n")
            menu()

    except (ValueError, TypeError):     #Usamos Except para los numeros negativos y los char o string
        print("\nError, elije una opcion valida\n")
        menu()


#Funcion "transaccion" para realizar las transacciones
def transaccion():
    print("\n-----Transacciones Rafon Rentals-----\n")

    try:
        licencia = float(input("Indica tu numero de licencia: "))
        renta = float(input("Indica la cantidad de dias de renta: "))
        edad = float(input("Indica tu edad: "))
        modelo = float(input("Indica el modelo del automovil: "))
    except ValueError:
        print("\nError: Debes ingresar números válidos.")
        transaccion()
        return

    #Manejo de errores
    if renta < 3:
        print("\n---Error, Debes rentar una unidad por lo menos 3 dias---")
        transaccion()
    
    elif renta > 90:
        print("\n---Error, no puedes rentar un vehiculo por mas de 3 meses---")
        transaccion()
              
    elif modelo > 2021:
        print("\n---Error, por temas de la actividad no manejamos modelos despues del 2021---")
        transaccion()

    elif modelo < 2017:
        print("\n---Error, por temas de la actividad no manejamos modelos antes del 2017---")
        transaccion()
    
    elif edad < 15:
        print("\n---Error, debes ser mayor de edad para rentar un vehiculo o tener almenos 15 años con autorizacion de un tutor---")
        transaccion()

    elif edad > 80:
        print("\n---Error, lamentablemente no rentamos vehiculos a adultos mayores a 80 años---")
        transaccion()


    elif edad >= 15 and edad < 18:

        permiso = input("Cuenta con la autorizacion de un tutor? (si/no): ")

        if permiso == "no":
            print("\n---Error, debes tener el permiso de un tutor para rentar un vehiculo---")
            transaccion()

        elif permiso == "si":
            print("-------------------------------------------")
            print("\nEstimado cliente con numero de licencia: ")

            if modelo == 2017:
                subtotal = renta * 550.00
        
            elif modelo == 2018:
                subtotal = renta * 590.00

            elif modelo == 2019:
                subtotal = renta * 650.00

            elif modelo == 2020:
                subtotal = renta * 700.00

            elif modelo == 2021:
                subtotal = renta * 750.00

            print("Subtotal: $" + str(subtotal) + "mxn" )

            seguro = subtotal * 0.8
            total = subtotal + seguro 

            print("Seguro de menor de edad: $" + str(seguro) + "mxn")
            print("Total a pagar: $" + str(total) + "mxn")


    else: 
        print("-------------------------------------------")
        print("\nEstimado cliente con numero de licencia: ")

        if modelo == 2017:
            subtotal = renta * 550.00
        
        elif modelo == 2018:
            subtotal = renta * 590.00

        elif modelo == 2019:
            subtotal = renta * 650.00

        elif modelo == 2020:
            subtotal = renta * 700.00

        elif modelo == 2021:
            subtotal = renta * 750.00

        print("Subtotal: $" + str(subtotal) + "mxn" )

        seguro = subtotal * 0.8
        total = subtotal + seguro 

        print("Total a pagar: $" + str(total) + "mxn")
            


    


#Funcion "costos" para darle al usuario una lista de costos por modelo
def costos():
    costos = ["2017 renta diaria de $550.00", "2018 renta diaria de $590.00", "2019 renta diaria de $650.00", "2020 renta diaria de $700.00", "2021 renta diaria de $750.00"]


    print("\nLista de costos: \n")

    #Ciclo For para imprimir la lista de costos
    for i in costos:
        print(i)

    print("")
    



menu()  #Se llama a la funcion "menu" para comenzar el programa