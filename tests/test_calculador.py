"""
Pruebas unitarias para el módulo calculador de CONJUNVION.
"""

import unittest
from conjunvion.calculador import ConjuntoCalculador


class TestConjuntoCalculador(unittest.TestCase):
    """Pruebas para la clase ConjuntoCalculador."""

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.calc = ConjuntoCalculador()
        self.universo = {1, 2, 3, 4, 5, 6}
        self.calc_con_universo = ConjuntoCalculador(self.universo)

    def test_union_basica(self):
        """Prueba de unión básica."""
        A = {1, 2, 3}
        B = {3, 4, 5}
        resultado = self.calc.union(A, B)
        self.assertEqual(resultado, {1, 2, 3, 4, 5})

    def test_union_vacia(self):
        """Prueba de unión con conjunto vacío."""
        A = {1, 2, 3}
        B = set()
        resultado = self.calc.union(A, B)
        self.assertEqual(resultado, A)

    def test_interseccion_basica(self):
        """Prueba de intersección básica."""
        A = {1, 2, 3}
        B = {2, 3, 4}
        resultado = self.calc.interseccion(A, B)
        self.assertEqual(resultado, {2, 3})

    def test_interseccion_vacia(self):
        """Prueba de intersección sin elementos comunes."""
        A = {1, 2, 3}
        B = {4, 5, 6}
        resultado = self.calc.interseccion(A, B)
        self.assertEqual(resultado, set())

    def test_diferencia_basica(self):
        """Prueba de diferencia básica."""
        A = {1, 2, 3}
        B = {2, 3, 4}
        resultado = self.calc.diferencia(A, B)
        self.assertEqual(resultado, {1})

    def test_diferencia_simetrica_basica(self):
        """Prueba de diferencia simétrica básica."""
        A = {1, 2, 3}
        B = {2, 3, 4}
        resultado = self.calc.diferencia_simetrica(A, B)
        self.assertEqual(resultado, {1, 4})

    def test_complemento_basico(self):
        """Prueba de complemento básico."""
        A = {1, 2, 3}
        universo = {1, 2, 3, 4, 5}
        resultado = self.calc.complemento(A, universo)
        self.assertEqual(resultado, {4, 5})

    def test_complemento_con_universo_definido(self):
        """Prueba de complemento con universo pre-configurado."""
        A = {1, 2, 3}
        resultado = self.calc_con_universo.complemento(A)
        self.assertEqual(resultado, {4, 5, 6})

    def test_complemento_sin_universo_error(self):
        """Prueba que complemento lanza error sin universo."""
        A = {1, 2, 3}
        with self.assertRaises(ValueError):
            self.calc.complemento(A)

    def test_producto_cartesiano(self):
        """Prueba de producto cartesiano."""
        A = {1, 2}
        B = {3, 4}
        resultado = self.calc.producto_cartesiano(A, B)
        esperado = {(1, 3), (1, 4), (2, 3), (2, 4)}
        self.assertEqual(resultado, esperado)

    def test_potencia_basica(self):
        """Prueba de conjunto potencia."""
        A = {1, 2}
        resultado = self.calc.potencia(A)
        # P({1,2}) tiene 2^2 = 4 elementos
        self.assertEqual(len(resultado), 4)
        # Debe contener el conjunto vacío
        self.assertIn(frozenset(), resultado)
        # Debe contener el conjunto completo
        self.assertIn(frozenset({1, 2}), resultado)

    def test_potencia_conjunto_vacio(self):
        """Prueba de potencia de conjunto vacío."""
        A = set()
        resultado = self.calc.potencia(A)
        # P(∅) = {∅}
        self.assertEqual(len(resultado), 1)
        self.assertIn(frozenset(), resultado)

    def test_cardinalidad(self):
        """Prueba de cardinalidad."""
        A = {1, 2, 3}
        resultado = self.calc.cardinalidad(A)
        self.assertEqual(resultado, 3)

    def test_cardinalidad_vacia(self):
        """Prueba de cardinalidad de conjunto vacío."""
        A = set()
        resultado = self.calc.cardinalidad(A)
        self.assertEqual(resultado, 0)

    def test_es_subconjunto_verdadero(self):
        """Prueba de subconjunto - caso verdadero."""
        A = {1, 2}
        B = {1, 2, 3}
        self.assertTrue(self.calc.es_subconjunto(A, B))

    def test_es_subconjunto_falso(self):
        """Prueba de subconjunto - caso falso."""
        A = {1, 2, 4}
        B = {1, 2, 3}
        self.assertFalse(self.calc.es_subconjunto(A, B))

    def test_es_subconjunto_igual(self):
        """Prueba de subconjunto - conjuntos iguales."""
        A = {1, 2, 3}
        B = {1, 2, 3}
        self.assertTrue(self.calc.es_subconjunto(A, B))

    def test_es_subconjunto_propio_verdadero(self):
        """Prueba de subconjunto propio - caso verdadero."""
        A = {1, 2}
        B = {1, 2, 3}
        self.assertTrue(self.calc.es_subconjunto_propio(A, B))

    def test_es_subconjunto_propio_falso_igual(self):
        """Prueba de subconjunto propio - conjuntos iguales."""
        A = {1, 2, 3}
        B = {1, 2, 3}
        self.assertFalse(self.calc.es_subconjunto_propio(A, B))

    def test_son_iguales_verdadero(self):
        """Prueba de igualdad - caso verdadero."""
        A = {1, 2, 3}
        B = {3, 2, 1}
        self.assertTrue(self.calc.son_iguales(A, B))

    def test_son_iguales_falso(self):
        """Prueba de igualdad - caso falso."""
        A = {1, 2, 3}
        B = {1, 2, 4}
        self.assertFalse(self.calc.son_iguales(A, B))

    def test_son_disjuntos_verdadero(self):
        """Prueba de disjuntos - caso verdadero."""
        A = {1, 2, 3}
        B = {4, 5, 6}
        self.assertTrue(self.calc.son_disjuntos(A, B))

    def test_son_disjuntos_falso(self):
        """Prueba de disjuntos - caso falso."""
        A = {1, 2, 3}
        B = {3, 4, 5}
        self.assertFalse(self.calc.son_disjuntos(A, B))

    def test_pertenece_verdadero(self):
        """Prueba de pertenencia - caso verdadero."""
        A = {1, 2, 3}
        self.assertTrue(self.calc.pertenece(1, A))

    def test_pertenece_falso(self):
        """Prueba de pertenencia - caso falso."""
        A = {1, 2, 3}
        self.assertFalse(self.calc.pertenece(4, A))


if __name__ == "__main__":
    unittest.main()
