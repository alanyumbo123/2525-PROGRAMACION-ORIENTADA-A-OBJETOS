# Dashboard de Programación Orientada a Objetos
# Adaptado por: Alan Yumbo
# Uso personal para organizar mis tareas y proyectos de POO
# Este archivo fue modificado respecto al proyecto original

import os
import subprocess
from datetime import datetime

# ---------------- DATOS DEL ESTUDIANTE ----------------
ESTUDIANTE = "Alan Yumbo"
MATERIA = "Programación Orientada a Objetos"

# Contador simple de ejecuciones del dashboard
contador_ejecuciones = 0


def mostrar_codigo(ruta_script):
    """
    Muestra el código fuente de un script seleccionado
    """
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script seleccionado desde el dashboard
    """
    try:
        subprocess.run(["python", ruta_script])
    except Exception as e:
        print(f"❌ Error al ejecutar el script: {e}")


def mostrar_menu():
    """
    Menú principal del dashboard
    """
    global contador_ejecuciones
    contador_ejecuciones += 1

    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Unidad 3'  # CAMBIO: unidad agregada por el estudiante
    }

    while True:
        print("\n===================================")
        print(" DASHBOARD DE PROGRAMACIÓN POO ")
        print("===================================")
        print(f"Estudiante: {ESTUDIANTE}")
        print(f"Materia: {MATERIA}")
        print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"Veces ejecutado: {contador_ejecuciones}")
        print("-----------------------------------")

        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            print("👋 Saliendo del dashboard...")
            break
        elif opcion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[opcion]))
        else:
            print("❌ Opción no válida.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las carpetas internas de cada unidad
    """
    if not os.path.exists(ruta_unidad):
        print("⚠️ Esta unidad aún no tiene carpetas.")
        return

    carpetas = [c.name for c in os.scandir(ruta_unidad) if c.is_dir()]

    while True:
        print("\n--- Submenú ---")
        for i, carpeta in enumerate(carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break
        try:
            index = int(opcion) - 1
            if 0 <= index < len(carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, carpetas[index]))
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


def mostrar_scripts(ruta_carpeta):
    """
    Lista los scripts .py y permite verlos o ejecutarlos
    """
    scripts = [s.name for s in os.scandir(ruta_carpeta) if s.name.endswith(".py")]

    while True:
        print("\n--- Scripts disponibles ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Volver")

        opcion = input("Seleccione un script: ")

        if opcion == '0':
            break
        try:
            index = int(opcion) - 1
            if 0 <= index < len(scripts):
                ruta_script = os.path.join(ruta_carpeta, scripts[index])
                mostrar_codigo(ruta_script)
                ejecutar = input("¿Desea ejecutar el script? (s/n): ").lower()
                if ejecutar == 's':
                    ejecutar_codigo(ruta_script)
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()


