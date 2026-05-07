# CONJUNVION

Una herramienta poderosa para calcular y manipular operaciones con conjuntos matemáticos.

## Características

- ✨ **Operaciones básicas**: Unión, Intersección, Diferencia, Diferencia Simétrica
- 🔄 **Operaciones avanzadas**: Complemento, Producto Cartesiano, Potencia de Conjuntos
- 📊 **Análisis**: Cardinalidad, Subconjuntos, Igualdad de conjuntos
- 🎯 **Interfaz intuitiva**: CLI fácil de usar
- 📈 **Visualización**: Representación clara de resultados

## Instalación

```bash
git clone https://github.com/saamdanilo-hub/CONJUNVION.git
cd CONJUNVION
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

### Como script CLI

```bash
python main.py
```

### Como módulo Python

```python
from conjunvion import ConjuntoCalculador

calc = ConjuntoCalculador()
A = {1, 2, 3}
B = {2, 3, 4}

union = calc.union(A, B)
print(f"A ∪ B = {union}")

interseccion = calc.interseccion(A, B)
print(f"A ∩ B = {interseccion}")
```

## Operaciones Disponibles

| Operación | Símbolo | Descripción |
|-----------|---------|-------------|
| Unión | ∪ | Elementos que están en A o en B |
| Intersección | ∩ | Elementos que están en A y en B |
| Diferencia | − | Elementos en A pero no en B |
| Diferencia Simétrica | Δ | Elementos en A o B pero no en ambos |
| Complemento | ᶜ | Elementos del universo que no están en A |
| Producto Cartesiano | × | Todos los pares ordenados (a, b) |
| Potencia | P(A) | Todos los subconjuntos de A |

## Estructura del Proyecto

```
CONJUNVION/
├── main.py                 # Punto de entrada principal
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── conjunvion/
│   ├── __init__.py
│   ├── calculador.py      # Lógica principal de cálculos
│   ├── validador.py       # Validación de entrada
│   └── utils.py           # Funciones utilitarias
└── tests/
    ├── __init__.py
    └── test_calculador.py # Pruebas unitarias
```

## Ejemplos

```python
from conjunvion import ConjuntoCalculador

calc = ConjuntoCalculador()

# Crear conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
universo = {1, 2, 3, 4, 5, 6, 7, 8}

# Operaciones
print(calc.union(A, B))              # {1, 2, 3, 4, 5, 6}
print(calc.interseccion(A, B))       # {3, 4}
print(calc.diferencia(A, B))         # {1, 2}
print(calc.diferencia_simetrica(A, B))  # {1, 2, 5, 6}
print(calc.complemento(A, universo)) # {5, 6, 7, 8}
print(calc.cardinalidad(A))          # 4
print(calc.es_subconjunto(A, B))     # False
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## Autor

**Saám Danilo** - [saamdanilo-hub](https://github.com/saamdanilo-hub)

## Soporte

Para reportar problemas o sugerencias, abre un [issue](https://github.com/saamdanilo-hub/CONJUNVION/issues).
