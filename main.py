#Inicio del sistema

import time
import sys
import os

USUARIO_CORRECTO = "1"
CLAVE_CORRETA = "1"
intentos = 3
saldo = 1000
retiro = 0
deposito = 0
movimientos = {}
salir = False

def limpiar_pantalla():
 os.system('cls' if os.name == 'nt' else 'clear')
 salir = False

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
  
 print("      ""TECHBANK RIWI DIGITAL")
 print("        ""-- BIENVENIDO --""\n")
 print("    ""=== INICIO DE SESIÓN===""\n")

 usuario = input("Usuario: ")
 clave = input("Clave: ")

 if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRETA:
  print("\n ✅ \033[32mAcceso concedido\033[0m""\n")
  
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
print("    ""=== MENÚ===")
print("-seleccione una operacion""\n")
print("1. Depositar        2. Retirar")
print("3. Saldo            4. Movimiento")

