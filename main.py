# Lógica de las opciones del menú

while not Salir: 


 opcion = input("Elija una opción : \n")
 if opcion == "1":
     while True:
         try:
             deposito = float(input("Ingrese el monto a depositar:\n"))
         except ValueError:
            print("Monto inválido. Ingrese un monto válido.")
            continue    
         
         if deposito <=0:
            print ("Monto inválido. Ingrese un monto valido")
            continue

     
         saldo += deposito
         movimientos.append(("Deposito", deposito)) 
         print(f"Deposito realizado. Nuevo saldo: {saldo:.2f}\n")
         break

    
     print ("1. Volver al menú    2. Salir\n")
     sub= input("Seleccione una opción:\n ")

     if sub == "2":
         print("Hasta luego!")
         Salir = True 

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
       
     
         saldo -= retiro 
         movimientos.append(("Retiro", retiro))
         print (f"Retiro realizado. Nuevo saldo: {saldo:.2f}")
         break
     
     
     print ("1. Volver al menú  2. Salir\n")
     sub= input("Seleccione una opción:\n")

     if sub =="2":
        print ("Hasta luego!")
        Salir= True

 elif opcion == "3":
    
    if not movimientos:
        print("\nNo se han realizado movimientos.\n")
    else:   
        print("\n---Movimientos realizados:---") 
        for mov in movimientos:
            if mov [0] == "Retiro":
              print(f"{mov[0]}: -{mov[1]:.2f}")
            else:
              print(f"{mov[0]}: +{mov[1]:.2f}") 
       
    print ("\n1. Volver al menú  2. Salir\n")
    sub= input("Seleccione una opción:\n")

    if sub == "2":
       print("Hasta luego!")
       Salir = True
    
    else:
       
 elif opcion == "4":
   print(f"Su saldo actual es: {saldo:.2f}\n")
   print ("1. Volver al menú  2. Salir\n")
   sub= input("Seleccione una opción:\n")

   if sub == "2":
    print ("Hasta luego!")
    Salir= True


 else:
  print("Opción no válida. Por favor, seleccione una opción del menú.\n")    