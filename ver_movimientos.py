def ver_movimientos(movimientos):

    if len (movimientos) == 0:
        print("\033[31m❌ No se han realizado movimientos aún.\033[0m\n")
            
    else:
        print("\033[35m===== Movimientos realizados =====\033[0m\n")

        for i, mov in enumerate(movimientos, start=1):
            print(f"{i}. {mov}")

    while True:
        print ("\033[33m1. Volver al menú \033[31m2. Salir\033[0m\n")
        sub = input("Seleccione una opción:\n")

        if sub == "1":
            return False

        elif sub == "2":
            print("\033[33m👋 ¡Hasta luego!\033[0m")
            return True

        else:
            print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")        