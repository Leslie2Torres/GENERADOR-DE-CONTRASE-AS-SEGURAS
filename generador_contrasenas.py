# =========================================================
# PROYECTO: Generador de Contraseñas Seguras
# Estudiante: Leslie Stefania Torres Chavez
# Paso 1: Avance Inicial del Desarrollo
# =========================================================

# 1. Configuración de librerías para la aleatoriedad y caracteres

import random
import string

# 2. Función principal del sistema

def generate_contrasena():
    print("=== GENERADOR DE CONTRASEÑAS SEGURAS ===")

# Avance inicial: Lectura de datos según el diagrama de flujo

    longitud = int(input("\nIngresar longitud de contraseña: "))

# validacion de longitud minima

    if longitud >= 8:
        print("Longitud válida.")
    else:
        print("La longitud mínima de la contraseña debe ser de 8 caracteres.")

# Inicio del programa
generate_contrasena()
        