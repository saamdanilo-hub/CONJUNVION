"""
Módulo visualizador de CONJUNVION.
Contiene funciones para generar gráficos de las operaciones de conjuntos.
"""

import os
from typing import Set, Optional, Tuple
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn2, venn3
import numpy as np


class VisualizadorConjuntos:
    """Clase para visualizar conjuntos mediante gráficos."""

    def __init__(self):
        """Inicializa el visualizador."""
        plt.style.use('seaborn-v0_8-darkgrid')

    @staticmethod
    def crear_directorio_graficos(nombre_dir: str = "graficos") -> str:
        """
        Crea un directorio para guardar gráficos si no existe.

        Args:
            nombre_dir: Nombre del directorio

        Returns:
            Ruta del directorio
        """
        if not os.path.exists(nombre_dir):
            os.makedirs(nombre_dir)
        return nombre_dir

    @staticmethod
    def diagrama_venn_2(
        A: Set,
        B: Set,
        titulo: str = "Diagrama de Venn",
        guardar: Optional[str] = None
    ) -> None:
        """
        Genera un diagrama de Venn para 2 conjuntos.

        Args:
            A: Primer conjunto
            B: Segundo conjunto
            titulo: Título del diagrama
            guardar: Ruta para guardar el gráfico (None para solo mostrar)
        """
        fig, ax = plt.subplots(figsize=(10, 8))

        # Convertir sets a listas etiquetadas
        A_set = set(A)
        B_set = set(B)

        venn2([A_set, B_set], set_labels=('A', 'B'), ax=ax)
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)

        # Agregar leyenda con cardinalidades
        card_a = len(A_set)
        card_b = len(B_set)
        card_interseccion = len(A_set & B_set)

        leyenda_texto = f"|A| = {card_a}\n|B| = {card_b}\n|A ∩ B| = {card_interseccion}"
        ax.text(0.98, 0.02, leyenda_texto, transform=ax.transAxes,
                fontsize=11, verticalalignment='bottom', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Gráfico guardado en: {guardar}")

        plt.show()
        plt.close()

    @staticmethod
    def diagrama_venn_3(
        A: Set,
        B: Set,
        C: Set,
        titulo: str = "Diagrama de Venn (3 conjuntos)",
        guardar: Optional[str] = None
    ) -> None:
        """
        Genera un diagrama de Venn para 3 conjuntos.

        Args:
            A: Primer conjunto
            B: Segundo conjunto
            C: Tercer conjunto
            titulo: Título del diagrama
            guardar: Ruta para guardar el gráfico
        """
        fig, ax = plt.subplots(figsize=(10, 8))

        A_set = set(A)
        B_set = set(B)
        C_set = set(C)

        venn3([A_set, B_set, C_set], set_labels=('A', 'B', 'C'), ax=ax)
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)

        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Gráfico guardado en: {guardar}")

        plt.show()
        plt.close()

    @staticmethod
    def grafico_producto_cartesiano(
        A: Set,
        B: Set,
        guardar: Optional[str] = None
    ) -> None:
        """
        Genera un gráfico del producto cartesiano.

        Args:
            A: Primer conjunto
            B: Segundo conjunto
            guardar: Ruta para guardar el gráfico
        """
        fig, ax = plt.subplots(figsize=(10, 8))

        # Convertir a listas numéricas si es posible
        try:
            A_list = sorted([float(x) for x in A])
            B_list = sorted([float(x) for x in B])
        except (ValueError, TypeError):
            A_list = sorted(list(A), key=str)
            B_list = sorted(list(B), key=str)

        # Plotear puntos
        for a in A_list:
            for b in B_list:
                ax.plot(a, b, 'o', markersize=12, color='#2E86AB')
                ax.annotate(f'({a}, {b})', xy=(a, b), xytext=(5, 5),
                           textcoords='offset points', fontsize=9)

        ax.set_xlabel('A', fontsize=12, fontweight='bold')
        ax.set_ylabel('B', fontsize=12, fontweight='bold')
        ax.set_title('Producto Cartesiano A × B', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Gráfico guardado en: {guardar}")

        plt.show()
        plt.close()

    @staticmethod
    def grafico_barras_cardinalidad(
        conjuntos: dict,
        titulo: str = "Cardinalidad de Conjuntos",
        guardar: Optional[str] = None
    ) -> None:
        """
        Genera un gráfico de barras para comparar cardinalidades.

        Args:
            conjuntos: Diccionario {nombre: conjunto}
            titulo: Título del gráfico
            guardar: Ruta para guardar el gráfico
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        nombres = list(conjuntos.keys())
        cardinalidades = [len(conjuntos[nombre]) for nombre in nombres]

        colores = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
        colores_usados = colores[:len(nombres)]

        barras = ax.bar(nombres, cardinalidades, color=colores_usados, alpha=0.7, edgecolor='black')

        # Agregar valores en las barras
        for barra in barras:
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                   f'{int(altura)}', ha='center', va='bottom', fontweight='bold')

        ax.set_ylabel('Cardinalidad', fontsize=12, fontweight='bold')
        ax.set_title(titulo, fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Gráfico guardado en: {guardar}")

        plt.show()
        plt.close()

    @staticmethod
    def tabla_elementos(
        conj: Set,
        titulo: str = "Elementos del Conjunto",
        guardar: Optional[str] = None
    ) -> None:
        """
        Crea una tabla visual de elementos.

        Args:
            conj: Conjunto a visualizar
            titulo: Título de la tabla
            guardar: Ruta para guardar el gráfico
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')

        elementos = sorted(list(conj), key=str)
        tabla_data = [[str(elem)] for elem in elementos]
        tabla_labels = ['Elemento']

        tabla = ax.table(cellText=tabla_data, colLabels=tabla_labels,
                        cellLoc='center', loc='center',
                        colWidths=[0.4])

        tabla.auto_set_font_size(False)
        tabla.set_fontsize(10)
        tabla.scale(1, 2)

        # Colorear header
        for i in range(len(tabla_labels)):
            tabla[(0, i)].set_facecolor('#2E86AB')
            tabla[(0, i)].set_text_props(weight='bold', color='white')

        ax.set_title(f"{titulo} (|A| = {len(conj)})", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Tabla guardada en: {guardar}")

        plt.show()
        plt.close()
