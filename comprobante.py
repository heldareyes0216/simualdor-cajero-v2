from datetime import datetime


def comprobante(tipo, monto, saldo):
    fecha = datetime.now().strftime ("%d/%m/%Y %H:%M:%S")

    print("\n   ""\033[35m====== COMPROBANTE ======\033[0m")
    print("Fecha y hora:", fecha)
    print("Tipo: ", tipo)
    print(f"Monto: ${monto}")
    print(f"Saldo actual: ${saldo}")
    print("Estado:\033[32m ✅ APROBADO\033[0m\n")