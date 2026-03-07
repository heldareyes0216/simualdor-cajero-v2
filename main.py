

#Importaciones

import time
import sys
import os
from comprobante import comprobante
from clean import limpiar_pantalla
from barra import barra
from deposito import deposito
from retiro import retiro
import saldo


#Inicio del sistema

USUARIO_CORRECTO = "1234"
CLAVE_CORRETA = "2711"
intentos = 4
retiro = 0
movimientos = []
salir = False
from datetime import datetime
ahora = datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y, %H:%M:%S")





barra()
limpiar_pantalla()
    

while intentos > 0:

  
    print("      ""\033[35m\033[1mTECHBANK RIWI DIGITAL\033[0m")
    print("        ""-- \033[33mBIENVENIDO\033[0m --""\n")
    print("    ""=== INICIA SESIÓN ===""\n")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRETA:
        print("\n ✅ \033[32mAcceso concedido\033[0m""\n")

        input("\nPresione ENTER para continuar...")
        
        limpiar_pantalla()
        barra()
        limpiar_pantalla()

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

        deposito(movimientos)

#---------------------------
# Opcion 2: Retirar dinero
#---------------------------

    elif opcion == "2":
        retiro(movimientos)    

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
        print(f"\nSu saldo actual es: {saldo.value:.2f}")
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

