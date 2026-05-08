"""
Módulo calculador de CONJUNVION.
Contiene la clase ConjuntoCalculador con todas las operaciones matemáticas de conjuntos.
"""

from itertools import combinations, product
from typing import Set, Tuple, FrozenSet


class ConjuntoCalculador:
    """Clase para realizar operaciones matemáticas con conjuntos."""

    def __init__(self, universo: Set = None):
        """
        Inicializa el calculador.

        Args:
            universo: Conjunto universo opcional para operaciones de complemento.
        """
        self.universo = universo

    def union(self, A: Set, B: Set) -> Set:
        """
        Calcula la unión de dos conjuntos (A ∪ B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            La unión de A y B
        """
        return A | B

    def interseccion(self, A: Set, B: Set) -> Set:
        """
        Calcula la intersección de dos conjuntos (A ∩ B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            La intersección de A y B
        """
        return A & B

    def diferencia(self, A: Set, B: Set) -> Set:
        """
        Calcula la diferencia de dos conjuntos (A - B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            Los elementos en A pero no en B
        """
        return A - B

    def diferencia_simetrica(self, A: Set, B: Set) -> Set:
        """
        Calcula la diferencia simétrica de dos conjuntos (A Δ B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            Los elementos en A o B pero no en ambos
        """
        return A ^ B

    def complemento(self, A: Set, universo: Set = None) -> Set:
        """
        Calcula el complemento de un conjunto (A^c).

        Args:
            A: Conjunto
            universo: Conjunto universo. Si no se proporciona, usa el del objeto.

        Returns:
            El complemento de A respecto al universo

        Raises:
            ValueError: Si no hay universo definido
        """
        univ = universo or self.universo
        if univ is None:
            raise ValueError("Debe definirse un universo para calcular el complemento")
        return univ - A

    def producto_cartesiano(self, A: Set, B: Set) -> Set[Tuple]:
        """
        Calcula el producto cartesiano de dos conjuntos (A × B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            El producto cartesiano como conjunto de tuplas
        """
        return set(product(A, B))

    def potencia(self, A: Set) -> Set[FrozenSet]:
        """
        Calcula el conjunto potencia de un conjunto (P(A)).

        Args:
            A: Conjunto

        Returns:
            El conjunto potencia como conjunto de frozensets
        """
        A_lista = list(A)
        potencia = set()

        for r in range(len(A_lista) + 1):
            for combo in combinations(A_lista, r):
                potencia.add(frozenset(combo))

        return potencia

    def cardinalidad(self, A: Set) -> int:
        """
        Calcula la cardinalidad de un conjunto (|A|).

        Args:
            A: Conjunto

        Returns:
            El número de elementos en el conjunto
        """
        return len(A)

    def es_subconjunto(self, A: Set, B: Set) -> bool:
        """
        Verifica si A es subconjunto de B (A ⊆ B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            True si A ⊆ B, False en caso contrario
        """
        return A <= B

    def es_subconjunto_propio(self, A: Set, B: Set) -> bool:
        """
        Verifica si A es subconjunto propio de B (A ⊂ B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            True si A ⊂ B, False en caso contrario
        """
        return A < B

    def son_iguales(self, A: Set, B: Set) -> bool:
        """
        Verifica si dos conjuntos son iguales (A = B).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            True si A = B, False en caso contrario
        """
        return A == B

    def son_disjuntos(self, A: Set, B: Set) -> bool:
        """
        Verifica si dos conjuntos son disjuntos (A ∩ B = ∅).

        Args:
            A: Primer conjunto
            B: Segundo conjunto

        Returns:
            True si los conjuntos son disjuntos, False en caso contrario
        """
        return len(A & B) == 0

    def pertenece(self, elemento, A: Set) -> bool:
        """
        Verifica si un elemento pertenece a un conjunto.

        Args:
            elemento: Elemento a verificar
            A: Conjunto

        Returns:
            True si el elemento está en A, False en caso contrario
        """
        return elemento in A
