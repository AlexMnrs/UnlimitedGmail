"""
.SYNOPSIS
    Generador de alias de Gmail mediante la inserción de puntos.

.DESCRIPTION
    Este script solicita un nombre de usuario de Gmail y genera todas las variaciones 
    posibles insertando puntos entre los caracteres. Según las políticas de Gmail, 
    los puntos no alteran la dirección de correo, permitiendo crear múltiples alias 
    que redirigen a la misma bandeja de entrada.

.NOTES
    Script Name: main.py
    Author:      Alex Monrás
    Created:     2026-01-22
    Version:     1.0.0
    
.EXAMPLE
    Entrada: test
    Salida: 
        test@gmail.com
        t.est@gmail.com
        te.st@gmail.com
        ...
"""

import os
import sys
import time

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_usuario() -> str:
    """
    Solicita y valida el nombre de usuario.
    
    Returns:
        str: El nombre de usuario validado sin dominio.
    """
    while True:
        try:
            entrada = input(" [+] Introduce tu usuario de Gmail (la parte antes del @): ").strip()
            
            if not entrada:
                continue
                
            if "@" in entrada:
                limpiar_pantalla()
                print(" [!] Error: Por favor, introduce SOLO el usuario, sin el '@gmail.com'")
                time.sleep(2)
                limpiar_pantalla()
                continue
            
            # Validación básica de caracteres permitidos en Gmail (letras, números y puntos)
            # Aunque quitamos los puntos para la generación, es bueno avisar si hay caracteres raros
            # Para simplificar, aceptamos lo que sea pero quitamos los puntos existentes
            return entrada.replace(".", "")
            
        except KeyboardInterrupt:
            print("\n [!] Operación cancelada por el usuario.")
            sys.exit(0)

def generar_alias(usuario: str):
    """
    Genera todas las combinaciones posibles de puntos para el usuario dado.
    Utiliza un enfoque iterativo basado en bitmasks para eficiencia.
    
    Args:
        usuario (str): Nombre de usuario base.
        
    Yields:
        str: Alias generado.
    """
    n = len(usuario)
    if n <= 1:
        yield usuario
        return

    # Hay n-1 espacios posibles donde poner punto.
    # Iteramos desde 0 hasta 2^(n-1) - 1
    total_combinaciones = 1 << (n - 1)
    
    for i in range(total_combinaciones):
        resultado = ""
        for j in range(n):
            resultado += usuario[j]
            # Si no es el último caracter y el bit correspondiente está activo, añadir punto
            # El bit j controla el espacio después del caracter j
            if j < n - 1 and (i & (1 << j)):
                resultado += "."
        yield resultado

def main():
    """Función principal de ejecución."""
    try:
        limpiar_pantalla()
        print(" ==========================================")
        print("       GENERADOR DE ALIAS DE GMAIL")
        print(" ==========================================\n")
        
        usuario = obtener_usuario()
        nombre_archivo = "gmail_aliases.txt"
        
        print(f"\n [*] Generando alias para '{usuario}'...")
        start_time = time.time()
        
        contador = 0
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            for alias in generar_alias(usuario):
                email = f"{alias}@gmail.com"
                f.write(email + "\n")
                # Imprimir en pantalla puede ser lento para muchos resultados,
                # mostramos progreso cada cierto tiempo o simplemente los resultados.
                # Dado el script original, mostramos los resultados.
                print(f" [>] Generado: {email}")
                contador += 1
        
        elapsed_time = time.time() - start_time
        
        print("\n ==========================================")
        print(f" [v] Proceso finalizado con éxito.")
        print(f" [+] Total generados: {contador}")
        print(f" [+] Tiempo transcurrido: {elapsed_time:.2f} segundos")
        print(f" [+] Guardado en: {os.path.abspath(nombre_archivo)}")
        print(" ==========================================")
        
        # Pausa antes de salir para que el usuario pueda leer en caso de doble clic
        input("\n Presiona Enter para salir...")

    except Exception as e:
        print(f"\n [X] Ocurrió un error inesperado: {e}")
        input(" Presiona Enter para salir...")

if __name__ == "__main__":
    main()
