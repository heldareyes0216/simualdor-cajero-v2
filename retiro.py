from comprobante import comprobante
import saldo
salir = False

def retiro(movimientos):
    
    global salir
    while True:
        try:
            retiro = float(input("Ingrese el monto a retirar:\n"))
        except ValueError: 
            print("Monto inválido. Ingrese un monto válido.")
            continue

        if retiro <= 0:
            print("\033[31m❌ Monto inválido. Ingrese un monto válido.\033[0m")
            continue

        elif retiro > saldo.value:
            print("\033[31m❌ Fondos insuficientes.\033[0m")
            continue

        saldo.value -= retiro
        movimientos.append(f"retiro: -${retiro}")

        comprobante("retiro", retiro, saldo.value)

        while True:
            print ("\033[36m1. Realizar otro deposito\033[0m\n")
            print ("\033[33m2. Volver al menú\033[0m\n")
            print ("\033[31m3. Salir\033[0m\n")
            sub= input("Seleccione una opción:\n")

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