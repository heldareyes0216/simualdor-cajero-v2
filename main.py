#lógica de retiro

elif option == 2:
try:
    monto = float(input("Ingrese monto a retirar: "))
    if monto <= 0:
        print("Monto invalido.")
    elif monto > saldo:
        print("Fonods insuficientes.")
    else:
        saldo -= monto
        movimientos.append(f"Retiro: -${monto}")
        print("\n==== COMPROBANTRE ====")
        print("Tipo: retiro")
        print(f"Monto: ${monto}")
        print(f"Saldo anterior: ${saldo_anterior}")
        print(f"saldo actual: ${saldo}")
        print("Estado: APROBADO")
        print("==========================")
except ValueError:
    print("Ingrese un número válido.")        

#lógica de depósito

elif option == 3:
try:
    monto = float(input("Ingrese monto a depositar: "))
    if monto <= 0:
        print("Monto invalido.")
    else:
        saldo_anterior = saldo
        saldo += monto 

        movimientos.append(f"Deposito: +${monto}")

        print("\n====== COMPROBANTE ======")
        print("Tipo: Depósito")
        print(f"Monto: ${monto}")
        print(f"Saldo anterior: ${saldo_anterior}")
        print(f"Saldo actual: ${saldo}")
        print("Estado: APROBADO")
        print("=========================")
except ValueError:
    print("Ingrese un número valido.")        


#        
    





        


                  
     






