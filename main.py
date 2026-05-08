"""
Script principal de CONJUNVION.
Interfaz interactiva en línea de comandos para cálculos de conjuntos con visualización de gráficos.
"""

import os
import sys

from conjunvion import (
    ConjuntoCalculador,
    VisualizadorConjuntos,
    ValidadorEntrada,
    Utilidades,
)


class InterfazCONJUNVION:
    """Interfaz principal de la aplicación CONJUNVION."""

    def __init__(self):
        """Inicializa la interfaz."""
        self.calculador = None
        self.visualizador = VisualizadorConjuntos()
        self.validador = ValidadorEntrada()
        self.utils = Utilidades()
        self.universo = None

    def mostrar_bienvenida(self) -> None:
        """Muestra el mensaje de bienvenida."""
        self.utils.imprimir_titulo("BIENVENIDO A CONJUNVION")
        print("La herramienta completa para cálculos de conjuntos matemáticos")
        print("✓ Operaciones de conjuntos")
        print("✓ Análisis matemático")
        print("✓ Visualización con gráficos (Venn, Cartesiano, etc.)")
        print("\nEscribe 'ayuda' en cualquier momento para ver los comandos disponibles\n")

    def configurar_universo(self) -> None:
        """Permite al usuario configurar un universo opcional."""
        print("\n¿Deseas trabajar con un universo definido?")
        print("(Esto permite usar la operación de complemento)\n")

        if self.utils.obtener_confirmacion("¿Definir universo?"):
            entrada = self.utils.obtener_entrada(
                "Ingresa los elementos del universo (ej: 1 2 3 4 5)"
            )
            if entrada:
                try:
                    self.universo = self.validador.parsear_conjunto(entrada)
                    self.calculador = ConjuntoCalculador(self.universo)
                    print(f"\n✅ Universo definido: {self.validador.formatear_conjunto(self.universo)}\n")
                except ValueError as e:
                    self.utils.imprimir_error(str(e))
        else:
            self.calculador = ConjuntoCalculador()

    def menu_operaciones_basicas(self) -> None:
        """Menú de operaciones básicas."""
        while True:
            opciones = {
                '1': 'Unión (A ∪ B)',
                '2': 'Intersección (A ∩ B)',
                '3': 'Diferencia (A - B)',
                '4': 'Diferencia Simétrica (A Δ B)',
                '5': 'Volver al menú principal',
            }

            seleccion = self.utils.mostrar_menu(opciones, "OPERACIONES BÁSICAS")

            if seleccion == '1':
                self.operar_dos_conjuntos('union', 'Unión')
            elif seleccion == '2':
                self.operar_dos_conjuntos('interseccion', 'Intersección')
            elif seleccion == '3':
                self.operar_dos_conjuntos('diferencia', 'Diferencia')
            elif seleccion == '4':
                self.operar_dos_conjuntos('diferencia_simetrica', 'Diferencia Simétrica')
            elif seleccion == '5':
                break

    def menu_operaciones_avanzadas(self) -> None:
        """Menú de operaciones avanzadas."""
        while True:
            opciones = {
                '1': 'Complemento (A^c)',
                '2': 'Producto Cartesiano (A × B)',
                '3': 'Conjunto Potencia (P(A))',
                '4': 'Volver al menú principal',
            }

            seleccion = self.utils.mostrar_menu(opciones, "OPERACIONES AVANZADAS")

            if seleccion == '1':
                self.operar_complemento()
            elif seleccion == '2':
                self.operar_producto_cartesiano()
            elif seleccion == '3':
                self.operar_potencia()
            elif seleccion == '4':
                break

    def menu_analisis(self) -> None:
        """Menú de análisis de conjuntos."""
        while True:
            opciones = {
                '1': 'Cardinalidad',
                '2': 'Verificar subconjunto',
                '3': 'Verificar igualdad',
                '4': 'Verificar disjuntos',
                '5': 'Verificar pertenencia',
                '6': 'Volver al menú principal',
            }

            seleccion = self.utils.mostrar_menu(opciones, "ANÁLISIS DE CONJUNTOS")

            if seleccion == '1':
                self.analizar_cardinalidad()
            elif seleccion == '2':
                self.analizar_subconjunto()
            elif seleccion == '3':
                self.analizar_igualdad()
            elif seleccion == '4':
                self.analizar_disjuntos()
            elif seleccion == '5':
                self.analizar_pertenencia()
            elif seleccion == '6':
                break

    def operar_dos_conjuntos(self, operacion: str, nombre_op: str) -> None:
        """Operación con dos conjuntos."""
        entrada_a = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3)")
        if entrada_a is None:
            return

        entrada_b = self.utils.obtener_entrada("Ingresa el conjunto B (ej: 3 4 5)")
        if entrada_b is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_a)
            B = self.validador.parsear_conjunto(entrada_b)

            operador = getattr(self.calculador, operacion)
            resultado = operador(A, B)

            resultado_str = self.validador.formatear_conjunto(resultado)
            self.utils.imprimir_resultado(
                nombre_op,
                f"{self.validador.formatear_conjunto(A)} {nombre_op.lower()} {self.validador.formatear_conjunto(B)} = {resultado_str}"
            )

            self.mostrar_grafico_resultado(A, B, resultado, nombre_op)

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def operar_complemento(self) -> None:
        """Operación de complemento."""
        if self.universo is None:
            self.utils.imprimir_error("Debes definir un universo para usar complemento")
            return

        entrada = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3)")
        if entrada is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada)
            resultado = self.calculador.complemento(A)

            resultado_str = self.validador.formatear_conjunto(resultado)
            self.utils.imprimir_resultado(
                "Complemento",
                f"A^c = {resultado_str}"
            )

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def operar_producto_cartesiano(self) -> None:
        """Operación de producto cartesiano."""
        entrada_a = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2)")
        if entrada_a is None:
            return

        entrada_b = self.utils.obtener_entrada("Ingresa el conjunto B (ej: 3 4)")
        if entrada_b is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_a)
            B = self.validador.parsear_conjunto(entrada_b)

            resultado = self.calculador.producto_cartesiano(A, B)
            resultado_str = self.validador.formatear_tuplas(resultado)

            self.utils.imprimir_resultado(
                "Producto Cartesiano",
                f"A × B = {resultado_str}"
            )

            if self.utils.obtener_confirmacion("¿Ver gráfico del producto cartesiano?"):
                ruta_grafico = None
                if self.utils.obtener_confirmacion("¿Guardar gráfico?"):
                    dir_graficos = self.visualizador.crear_directorio_graficos()
                    ruta_grafico = os.path.join(dir_graficos, "producto_cartesiano.png")

                self.visualizador.grafico_producto_cartesiano(A, B, guardar=ruta_grafico)

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def operar_potencia(self) -> None:
        """Operación de conjunto potencia."""
        entrada = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3)")
        if entrada is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada)

            if len(A) > 10:
                self.utils.imprimir_advertencia(
                    f"Conjunto muy grande (cardinalidad {len(A)}).\n"
                    "P(A) tendrá 2^{len(A)} = {2**len(A)} elementos"
                )
                return

            resultado = self.calculador.potencia(A)
            cardinalidad = len(resultado)

            self.utils.imprimir_resultado(
                "Conjunto Potencia",
                f"|P(A)| = 2^{len(A)} = {cardinalidad} elementos"
            )

            if len(A) <= 3:
                elementos = sorted([sorted(list(x)) for x in resultado])
                print("  Elementos de P(A):")
                for elem in elementos:
                    print(f"    {set(elem) if elem else '∅'}")

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def analizar_cardinalidad(self) -> None:
        """Analiza la cardinalidad de un conjunto."""
        entrada = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3 4)")
        if entrada is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada)
            cardinalidad = self.calculador.cardinalidad(A)

            self.utils.imprimir_resultado(
                "Cardinalidad",
                f"|A| = {cardinalidad}"
            )

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def analizar_subconjunto(self) -> None:
        """Verifica si un conjunto es subconjunto de otro."""
        entrada_a = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2)")
        if entrada_a is None:
            return

        entrada_b = self.utils.obtener_entrada("Ingresa el conjunto B (ej: 1 2 3)")
        if entrada_b is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_a)
            B = self.validador.parsear_conjunto(entrada_b)

            es_sub = self.calculador.es_subconjunto(A, B)
            es_sub_propio = self.calculador.es_subconjunto_propio(A, B)

            resultado = f"A ⊆ B: {es_sub}"
            if es_sub_propio:
                resultado += f"\nA ⊂ B (subconjunto propio): Verdadero"

            self.utils.imprimir_resultado("Análisis de Subconjunto", resultado)

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def analizar_igualdad(self) -> None:
        """Verifica si dos conjuntos son iguales."""
        entrada_a = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3)")
        if entrada_a is None:
            return

        entrada_b = self.utils.obtener_entrada("Ingresa el conjunto B (ej: 3 2 1)")
        if entrada_b is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_a)
            B = self.validador.parsear_conjunto(entrada_b)

            son_iguales = self.calculador.son_iguales(A, B)

            self.utils.imprimir_resultado(
                "Igualdad",
                f"A = B: {'Verdadero' if son_iguales else 'Falso'}"
            )

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def analizar_disjuntos(self) -> None:
        """Verifica si dos conjuntos son disjuntos."""
        entrada_a = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2)")
        if entrada_a is None:
            return

        entrada_b = self.utils.obtener_entrada("Ingresa el conjunto B (ej: 3 4)")
        if entrada_b is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_a)
            B = self.validador.parsear_conjunto(entrada_b)

            disjuntos = self.calculador.son_disjuntos(A, B)

            self.utils.imprimir_resultado(
                "Conjuntos Disjuntos",
                f"A ∩ B = ∅: {'Verdadero' if disjuntos else 'Falso'}"
            )

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def analizar_pertenencia(self) -> None:
        """Verifica si un elemento pertenece a un conjunto."""
        entrada_conj = self.utils.obtener_entrada("Ingresa el conjunto A (ej: 1 2 3 4)")
        if entrada_conj is None:
            return

        entrada_elem = self.utils.obtener_entrada("Ingresa el elemento a verificar (ej: 2)")
        if entrada_elem is None:
            return

        try:
            A = self.validador.parsear_conjunto(entrada_conj)
            elemento = self.validador.validar_elemento(entrada_elem)

            pertenece = self.calculador.pertenece(elemento, A)

            simbolo = "∈" if pertenece else "∉"
            self.utils.imprimir_resultado(
                "Pertenencia",
                f"{elemento} {simbolo} A"
            )

        except ValueError as e:
            self.utils.imprimir_error(str(e))

    def mostrar_grafico_resultado(self, A, B, resultado, nombre_op):
        """Muestra opciones para visualizar resultados."""
        if self.utils.obtener_confirmacion("¿Ver diagrama de Venn?"):
            ruta_grafico = None
            if self.utils.obtener_confirmacion("¿Guardar gráfico?"):
                dir_graficos = self.visualizador.crear_directorio_graficos()
                ruta_grafico = os.path.join(dir_graficos, f"venn_{nombre_op.lower()}.png")

            self.visualizador.diagrama_venn_2(
                A, B,
                titulo=f"Diagrama de Venn - {nombre_op}",
                guardar=ruta_grafico
            )

    def menu_principal(self) -> None:
        """Menú principal de la aplicación."""
        while True:
            opciones = {
                '1': 'Operaciones Básicas',
                '2': 'Operaciones Avanzadas',
                '3': 'Análisis de Conjuntos',
                '4': 'Configurar Universo',
                '5': 'Salir',
            }

            seleccion = self.utils.mostrar_menu(opciones, "MENÚ PRINCIPAL CONJUNVION")

            if seleccion == '1':
                self.menu_operaciones_basicas()
            elif seleccion == '2':
                self.menu_operaciones_avanzadas()
            elif seleccion == '3':
                self.menu_analisis()
            elif seleccion == '4':
                self.configurar_universo()
            elif seleccion == '5':
                self.utils.imprimir_exito("¡Gracias por usar CONJUNVION!")
                sys.exit(0)

    def ejecutar(self) -> None:
        """Ejecuta la aplicación."""
        try:
            self.utils.limpiar_pantalla()
            self.mostrar_bienvenida()
            self.configurar_universo()
            self.menu_principal()
        except KeyboardInterrupt:
            print("\n\n❌ Aplicación interrumpida por el usuario")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            sys.exit(1)


def main():
    """Función principal."""
    interfaz = InterfazCONJUNVION()
    interfaz.ejecutar()


if __name__ == "__main__":
    main()
