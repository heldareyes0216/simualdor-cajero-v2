#  TECHBANK RIWI DIGITAL - Simulador Bancario

Este proyecto es una aplicación de consola desarrollada en **Python** que simula las operaciones básicas de un cajero automático (ATM). El sistema permite gestionar sesiones de usuario, depósitos, retiros y consulta de historial de movimientos con una interfaz visual fluida.

---

## 🚀 Características Principales

* **Autenticación de Seguridad:** Sistema de login con 3 intentos máximos antes del bloqueo de cuenta.
* **Gestión de Saldo:** Control en tiempo real de ingresos y egresos con validación de fondos.
* **Historial de Movimientos:** Registro dinámico de todas las transacciones realizadas durante la sesión.
* **Interfaz Dinámica:** Incluye barras de carga visuales y limpieza de consola (`ASCII`) para una mejor experiencia de usuario.
* **Validación de Datos:** Manejo de excepciones para evitar entradas no numéricas o montos negativos.

---

## 🏗️ Arquitectura del Flujo

La lógica del programa se divide en tres etapas fundamentales:

1.  **Carga e Inicialización:** Configuración de variables globales (`saldo`, `intentos`, `movimientos`).
2.  **Validación de Credenciales:** Verificación de identidad mediante un bucle de control.
3.  **Bucle de Operaciones:** Un menú interactivo que procesa la lógica de negocio.



---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Módulos del Sistema:**
    * `os`: Gestión de limpieza de pantalla.
    * `sys` & `time`: Creación de la barra de progreso animada.
    * `datetime`: Sellado de tiempo real para los comprobantes.

---

## 📖 Guía de Uso

### 🔑 Credenciales por Defecto
| Usuario | Clave |
| :--- | :--- |
| `1234` | `2711` |

### 🕹️ Opciones del Menú
| Opción | Acción | Descripción |
| :--- | :--- | :--- |
| **1** | **Depositar** | Incrementa el saldo y genera un comprobante de depósito. |
| **2** | **Retirar** | Permite retirar dinero si el saldo es suficiente. |
| **3** | **Movimientos** | Despliega una lista numerada con el historial de la sesión. |
| **4** | **Saldo** | Muestra el balance actual formateado a dos decimales. |
| **5** | **Salir** | Finaliza la sesión de forma segura. |

---

## 👨‍🏫 Notas de Mejora (Feedback Senior)

Como parte de un proceso de aprendizaje progresivo, se identifican los siguientes puntos para optimizar en futuras versiones:

* **Refactorización:** Mover la lógica de la "Barra de carga" y los "Comprobantes" a funciones independientes (`def`) para mejorar la legibilidad.
* **Corrección de String:** En el depósito, el historial registra la palabra "retiro" por error; se debe ajustar a "deposito".
* **Persistencia:** Implementar manejo de archivos (`JSON` o `TXT`) para que el saldo no se reinicie al cerrar el programa.

---

> **Desarrollado como ejercicio de lógica de programación y manejo de flujos en Python.**