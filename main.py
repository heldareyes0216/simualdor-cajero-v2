# Lógica de las opciones del menú

#---------------------------
# Opcion 1: Depositar dinero
#---------------------------

if opcion == "1":
    while True:
        try:
            deposito = float(input("Ingrese el monto a depositar:\n"))
        except ValueError:
            print("Monto inválido. Ingrese un monto válido.")
            continue    
         
        if deposito <=0:
            print("Monto inválido. Ingrese un monto valido")
            continue

     
        saldo += deposito
        movimientos.append(("Deposito", deposito)) 
        print(f"\nDeposito realizado. Nuevo saldo: {saldo:.2f}")
         
        while True:

            print ("\n1. Realizar otro deposito")
            print ("2. Volver al menú")
            print ("3. Salir\n")
            sub= input("Seleccione una opción:\n ")

            if sub == "1":
               break
            
            elif sub == "2":
                break

            elif sub == "3":
                print("Hasta luego!")
                Salir = True
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.\n")

        if Salir or sub == "2":
            break

#---------------------------
# Opcion 2: Retirar dinero
#---------------------------

elif opcion == "2":
    while True:
        try:
            retiro = float(input("Ingrese el monto a retirar: \n"))
        except ValueError:
            print("Monto invalido. Ingrese un monto válido.")
            continue
             
        if retiro <= 0:
            print("Monto inválido. Ingrese un monto válido.")
            continue

        elif retiro > saldo:
            print("Fondos insuficientes.")
            continue
       
     
        saldo -= retiro 
        movimientos.append(("Retiro", retiro))
        print(f"\nRetiro realizado. Nuevo saldo: {saldo:.2f}")

        while True:
            print ("\n1. Realizar otro retiro")
            print ("2. Volver al menú")
            print ("3. Salir\n")   
            sub= input("Seleccione una opción:\n")

            if sub =="1":
                break
            elif sub == "2":
                break

            elif sub == "3":
                print("Hasta luego!")
                Salir = True
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.\n")
            
        if Salir or sub == "2":
            break    

#---------------------------
# Opcion 3: Ver movimientos
#---------------------------

elif opcion == "3":
    
    if not movimientos:
        print("\nNo se han realizado movimientos.\n")

    else:   
        print("\n---Movimientos realizados:---") 
        for mov in movimientos:
            if mov [0] == "Retiro":
                print(f"\n{mov[0]}: -{mov[1]:.2f}")

            else:
                print(f"\n{mov[0]}: +{mov[1]:.2f}") 

        while True:    
            print ("\n1. Volver al menú")
            print ("2. Salir\n")
            sub= input("Seleccione una opción:\n")

            if sub == "1":
                break
        
            elif sub == "2":
                print("Hasta luego!")
                Salir = True
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.\n")

#---------------------------
# Opcion 4: Ver saldo
# ---------------------------  
    
elif opcion == "4":
    print(f"\nSu saldo actual es: {saldo:.2f}")
    print ("\n1. Volver al menú")
    print ("2. Salir\n")
    sub= input("Seleccione una opción:\n")

    if sub == "2":
        print("Hasta luego!")
        Salir= True

#---------------------------
# Opcion 5: Salir
#---------------------------

elif opcion == "5":
    print("Hasta luego!")
    Salir = True      

#---------------------------
# Opcion no valida
#---------------------------

else:
    print("Opción no válida. Por favor, seleccione una opción del menú.\n")    