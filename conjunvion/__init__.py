"""
CONJUNVION - Herramienta para cálculos de conjuntos matemáticos.

Módulos disponibles:
- calculador: Operaciones matemáticas de conjuntos
- validador: Validación y parseo de entrada
- utils: Utilidades de interfaz
- visualizador: Generación de gráficos
"""

from .calculador import ConjuntoCalculador
from .validador import ValidadorEntrada
from .utils import Utilidades
from .visualizador import VisualizadorConjuntos

__version__ = "1.0.0"
__author__ = "Saám Danilo"
__all__ = [
    "ConjuntoCalculador",
    "ValidadorEntrada",
    "Utilidades",
    "VisualizadorConjuntos",
]
