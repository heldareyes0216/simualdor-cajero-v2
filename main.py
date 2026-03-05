# Variables iniciales necesarias
saldo = 1000.0
movimientos = []
deposito = 0
Salir = False

while not Salir: 

 opcion = input("Elija una opción : \n")
 if opcion == "1":
   while True:
    deposito = float(input("Ingrese el monto a depositar:\n"))
    if deposito < 0:
        print ("Monto inválido. Ingrese un monto valido")

    elif deposito > 0:
     saldo += deposito
     movimientos.append(("Desposito", deposito)) 
     print(f"Deposito realizado. Nuevo saldo: {saldo}\n")
     break

    
   print ("1. Volver al menú    2. Salir\n")
   sub= input("Seleccione una opción:\n ")

   if sub == "2":
     print("Hasta luego!")
     Salir = True 

 elif opcion == "2":
   while True:
    retiro = float(input("Ingrese el monto a retirar: \n"))
    if retiro < 0:
       print("Monto inválido. Ingrese un monto válido.")

    elif retiro > saldo:
       print("Fondos insuficientes.")
       break
     
    else:
       saldo -= retiro 
       movimientos.append(("Retiro", retiro))
       print (f"Retiro realizado. Nuevo saldo: {saldo}")
       break
     
   print ("1. Volver al menú  2. Salir\n")
   sub= input("Seleccione una opción:\n")

   if sub =="2":
    print ("Hasta luego!")
    Salir= True

 elif opcion == "3":
   while True:
    print("Movimientos realizados:")
    for mov in movimientos:
      print(f"{mov[0]}: {mov[1]})")
