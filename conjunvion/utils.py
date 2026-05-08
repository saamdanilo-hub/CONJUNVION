"""
Módulo de utilidades de CONJUNVION.
Contiene funciones auxiliares para la interfaz de usuario.
"""

import os
import sys
from typing import Dict, Optional


class Utilidades:
    """Clase con utilidades para la interfaz de usuario."""

    @staticmethod
    def limpiar_pantalla() -> None:
        """Limpia la pantalla de la terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def imprimir_titulo(titulo: str) -> None:
        """
        Imprime un título formateado.

        Args:
            titulo: Texto del título
        """
        print("\n" + "=" * 60)
        print(f"  {titulo.center(56)}")
        print("=" * 60 + "\n")

    @staticmethod
    def imprimir_resultado(nombre: str, resultado: str) -> None:
        """
        Imprime un resultado formateado.

        Args:
            nombre: Nombre del resultado
            resultado: Texto del resultado
        """
        print("\n" + "-" * 60)
        print(f"📊 {nombre}")
        print("-" * 60)
        print(f"  {resultado}")
        print("-" * 60 + "\n")

    @staticmethod
    def imprimir_error(mensaje: str) -> None:
        """
        Imprime un mensaje de error.

        Args:
            mensaje: Texto del error
        """
        print(f"\n❌ Error: {mensaje}\n")

    @staticmethod
    def imprimir_advertencia(mensaje: str) -> None:
        """
        Imprime un mensaje de advertencia.

        Args:
            mensaje: Texto de la advertencia
        """
        print(f"\n⚠️  Advertencia: {mensaje}\n")

    @staticmethod
    def imprimir_exito(mensaje: str) -> None:
        """
        Imprime un mensaje de éxito.

        Args:
            mensaje: Texto del mensaje
        """
        print(f"\n✅ {mensaje}\n")

    @staticmethod
    def mostrar_menu(opciones: Dict[str, str], titulo: str = "MENÚ") -> str:
        """
        Muestra un menú y obtiene la selección del usuario.

        Args:
            opciones: Diccionario con opciones {clave: descripción}
            titulo: Título del menú

        Returns:
            La opción seleccionada por el usuario
        """
        print(f"\n{'=' * 60}")
        print(f"  {titulo.center(56)}")
        print(f"{'=' * 60}\n")

        for clave, descripcion in opciones.items():
            print(f"  [{clave}] {descripcion}")

        print()
        while True:
            seleccion = input("  Selecciona una opción: ").strip()
            if seleccion in opciones:
                return seleccion
            print("  ❌ Opción no válida. Intenta de nuevo.")

    @staticmethod
    def obtener_entrada(prompt: str) -> Optional[str]:
        """
        Obtiene entrada del usuario con manejo de excepciones.

        Args:
            prompt: Texto del mensaje

        Returns:
            La entrada del usuario o None si cancela
        """
        try:
            entrada = input(f"\n  {prompt}\n  > ").strip()
            if entrada.lower() == 'cancelar':
                return None
            return entrada
        except KeyboardInterrupt:
            return None

    @staticmethod
    def obtener_confirmacion(prompt: str) -> bool:
        """
        Obtiene una confirmación sí/no del usuario.

        Args:
            prompt: Texto del mensaje

        Returns:
            True si el usuario responde afirmativamente
        """
        while True:
            respuesta = input(f"\n  {prompt} (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            print("  ❌ Respuesta no válida. Por favor, ingresa 's' o 'n'.")
