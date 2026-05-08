"""
Módulo validador de CONJUNVION.
Contiene funciones para validar y parsear entrada del usuario.
"""

from typing import Set, Tuple


class ValidadorEntrada:
    """Clase para validar y parsear entrada del usuario."""

    @staticmethod
    def parsear_conjunto(entrada: str) -> Set:
        """
        Parsea una cadena de entrada a un conjunto.

        Args:
            entrada: Cadena con elementos separados por espacios (ej: "1 2 3")

        Returns:
            Conjunto con los elementos parseados

        Raises:
            ValueError: Si la entrada no es válida
        """
        if not entrada or not entrada.strip():
            return set()

        try:
            elementos = entrada.strip().split()
            conjunto = set()

            for elem in elementos:
                try:
                    # Intentar convertir a número
                    if '.' in elem:
                        conjunto.add(float(elem))
                    else:
                        conjunto.add(int(elem))
                except ValueError:
                    # Si no es número, agregarlo como string
                    conjunto.add(elem)

            return conjunto
        except Exception as e:
            raise ValueError(f"Error al parsear el conjunto: {str(e)}")

    @staticmethod
    def validar_elemento(entrada: str):
        """
        Valida y parsea un elemento individual.

        Args:
            entrada: Cadena con el elemento

        Returns:
            El elemento parseado

        Raises:
            ValueError: Si la entrada no es válida
        """
        entrada = entrada.strip()
        if not entrada:
            raise ValueError("El elemento no puede estar vacío")

        try:
            if '.' in entrada:
                return float(entrada)
            else:
                return int(entrada)
        except ValueError:
            return entrada

    @staticmethod
    def formatear_conjunto(conj: Set) -> str:
        """
        Formatea un conjunto para mostrarlo.

        Args:
            conj: Conjunto a formatear

        Returns:
            Cadena formateada del conjunto
        """
        if not conj:
            return "∅"

        elementos = sorted(list(conj), key=lambda x: (isinstance(x, str), x))
        return "{" + ", ".join(str(e) for e in elementos) + "}"

    @staticmethod
    def formatear_tuplas(tuplas: Set[Tuple]) -> str:
        """
        Formatea un conjunto de tuplas.

        Args:
            tuplas: Conjunto de tuplas

        Returns:
            Cadena formateada
        """
        if not tuplas:
            return "∅"

        tuplas_sorted = sorted(list(tuplas))
        return "{" + ", ".join(f"({a}, {b})" for a, b in tuplas_sorted) + "}"
