def barra ():
    import sys
    import time

    for i in range(101):
        barra = "█" * (i//2) #LLENARIA LA BARRA
        espacios = " "* (50 - len(barra)) #ESPACIO VACÍO

        sys.stdout.write(f"\rCargando: |{barra}{espacios}| {i}%")
        sys.stdout.flush()
        time.sleep(0.02)
    
    print()
    print()   
      