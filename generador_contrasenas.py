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

    longitud = int(input("Ingresar longitud de contraseña: "))

# validacion de longitud minima

    if longitud >= 8:
        print("Longitud válida.")

# crear caracteres para la contraseña

        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

# generar la contraseña aleatoria

        contrasena = ""
        for i in range(longitud):
            contrasena += random.choice(caracteres) 

# mostrar la contraseña generada
        print("Contraseña generada:")
        print(contrasena)
        
    else:
        print("La longitud mínima de la contraseña debe ser de 8 caracteres.")


#Inicio del programa
generate_contrasena()
        