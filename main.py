

#Inicio del sistema

import time
import sys
import os

USUARIO_CORRECTO = "1234"
CLAVE_CORRETA = "2711"
intentos = 3
saldo = 1000
retiro = 0
deposito = 0
movimientos = []
salir = False
from datetime import datetime
ahora = datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y, %H:%M:%S")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while not salir:
    
    for i in range(101):
        barra = "█" * (i//2) #LLENARIA LA BARRA
        espacios = " " * (50 - len(barra)) #ESPACIO VACÍO   

        sys.stdout.write(f"\rCargando: |{barra}{espacios}| {i}%")
        sys.stdout.flush()
        time.sleep(0.02)
        limpiar_pantalla()
    
    break

while intentos >0:
  
    print("      ""\033[35m\033[1mTECHBANK RIWI DIGITAL\033[0m")
    print("        ""-- \033[33mBIENVENIDO\033[0m --""\n")
    print("    ""=== INICIO DE SESIÓN===""\n")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRETA:
        print("\n ✅ \033[32mAcceso concedido\033[0m""\n")

        input("\nPresione ENTER para continuar...")
        limpiar_pantalla()
    
        for i in range(101):
            barra = "█" * (i//2) #LLENARIA LA BARRA
            espacios = " " * (50 - len(barra)) #ESPACIO VACÍO   

            sys.stdout.write(f"\rCargando: |{barra}{espacios}| {i}%")
            sys.stdout.flush()
            time.sleep(0.01)
        break
    
 
    else:
        intentos -= 1
        print(f"❌ \033[31mDatos incorrectos.\033[0m Intentos restantes: {intentos}\n")

        if intentos == 0:   
            print("🚫 \033[31mCuenta Bloqueada\033[0m")
            exit()

limpiar_pantalla()

#MENU
while not salir:
 
    print("       ""\033[35m=== MENÚ===\033[0m")
    print("-seleccione una operacion\n")
    print("1. Depositar       2. Retirar")
    print("3. Movimientos     4. Saldo")
    print("5. Salir\n")
 
    opcion = input("\nSeleccione una opcion: ")
    limpiar_pantalla()


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
                print("\033[31m❌ Monto inválido. Ingrese un monto valido\033[0m")
                continue

     
            saldo += deposito
            movimientos.append(f"deposito: +${deposito}")

            print("\n   ""\033[35m====== COMPROBANTE ======\033[0m")
            print("Fecha y hora:", fecha_formateada)
            print("Tipo: Deposito")
            print(f"Monto: ${deposito}")
            print(f"Saldo actual: ${saldo}")
            print("Estado:\033[32m ✅ APROBADO\033[0m\n")
         
            while True:

                print ("\033[36m1. Realizar otro deposito\033[0m\n")
                print ("\033[33m2. Volver al menú     \033[31m3. Salir\033[0m\n")
                sub= input("Seleccione una opción:\n ")

                if sub == "1":
                    break
            
                elif sub == "2":
                    break

                elif sub == "3":
                    print("\033[33m👋 ¡Hasta luego!\033[0m")
                    salir = True
                    break

                else:
                    print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")

            if salir or sub == "2":
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
                print("\033[31m❌ Monto inválido. Ingrese un monto válido.\033[0m")
                continue

            elif retiro > saldo:
                print("\033[31m❌ Fondos insuficientes.\033[0m")
                continue
       
     
            saldo -= retiro 
            movimientos.append(f"retiro: -${retiro}")

            print("\n   ""====== COMPROBANTE ======")
            print("Fecha y hora:", fecha_formateada)
            print("Tipo: retiro")
            print(f"Monto: ${retiro}")
            print(f"saldo actual: ${saldo}")
            print("Estado: \033[32m ✅ APROBADO\033[0m")

            while True:
                print ("\033[36m1. Realizar otro deposito\033[0m\n")
                print ("\033[33m2. Volver al menú     \033[31m3. Salir\033[0m\n")   
                sub= input("Seleccione una opción:\n")

                if sub =="1":
                    break

                elif sub == "2":
                    break

                elif sub == "3":
                    print("\033[33m👋 ¡Hasta luego!\033[0m")
                    salir = True
                    break

                else:
                    print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")
            
            if salir or sub == "2":
                break    

#---------------------------
# Opcion 3: Ver movimientos
#---------------------------

    elif opcion == "3":
        if len(movimientos) == 0:
            print("\033[31m❌ No hay movimientos realizados.\033[0m\n")

        else:   
            print("\033[35m===== Movimientos realizados =====\033[0m\n")

            for i, movimiento in enumerate(movimientos, start=1):
                print(f"{i}. {movimiento}") 

            

            while True:    
                print ("\033[33m1. Volver al menú     \033[31m2. Salir\033[0m\n") 
                sub= input("Seleccione una opción:\n")

                if sub == "1":
                    break
                
                elif sub == "2":
                    print("\033[33m👋 ¡Hasta luego!\033[0m")
                    salir = True
                    break

                else:
                    print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")

#---------------------------
# Opcion 4: Ver saldo
# ---------------------------  
    
    elif opcion == "4":
        print(f"\nSu saldo actual es: {saldo:.2f}")
        print ("\033[33m1. Volver al menú     \033[31m2. Salir\033[0m\n") 
        sub= input("Seleccione una opción:\n")

        if sub == "2":
            print("\033[33m👋 ¡Hasta luego!\033[0m")
            salir= True

#---------------------------
# Opcion 5: Salir
#---------------------------

    elif opcion == "5":
        print("\033[33m👋 ¡Hasta luego!\033[0m")
        salir = True    
        break  

#---------------------------
# Opcion no valida
#---------------------------

    else:
        print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")    

