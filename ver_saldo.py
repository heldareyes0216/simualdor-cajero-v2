def ver_saldo(saldo):
    print(f"\nSu saldo actual es: {saldo.value:.2f}")

    while True:
        print ("\033[33m1. Volver al menú     \033[31m2. Salir\033[0m\n")
        sub= input("Seleccione una opción:\n")

        if sub == "2":
            print("\033[33m👋 ¡Hasta luego!\033[0m")
            return True
        
        elif sub == "1":
            return False
        
        else:
            print("\033[31m❌ Opción no válida. Por favor, seleccione una opción del menú.\033[0m\n")
