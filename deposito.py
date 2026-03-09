from comprobante import comprobante
import saldo

def deposito(movimientos):
    while True:
        try:
            deposito = float(input("Ingrese el monto a depositar:\n"))
        except ValueError:
            print("Monto inválido. Ingrese un monto válido.")
            continue

        if deposito <=0:
            print("\033[31m❌ Monto inválido. Ingrese un monto valido\033[0m")
            continue


        saldo.value += deposito
        movimientos.append(f"deposito: +${deposito}")
        
        comprobante("deposito", deposito, saldo.value)

        while True:

            print ("\033[36m1. Realizar otro deposito\033[0m\n")
            print ("\033[33m2. Volver al menú\033[0m\n")
            print ("\033[31m3. Salir\033[0m\n")
            sub= input("Seleccione una opción:\n")

            if sub == "1":
                break

            elif sub == "2":
                return False

            elif sub == "3":
                print("\033[33m👋 ¡Hasta luego!\033[0m")
                return True
               
            else:
                print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")                  