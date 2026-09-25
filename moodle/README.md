# Moodle

Moodle es el aula virtual; la biblioteca es su fuente de contenidos.

> **Costo:** el software Moodle es gratuito, pero el servidor no. MoodleCloud no tiene plan gratuito permanente. Hasta contar con un servidor sin costo (por ejemplo de una universidad aliada), la biblioteca y la Escuela en GitHub Pages cumplen el rol de aula. Ver `docs/software-gratuito.md`.

## Estructura recomendada de un curso en Moodle
- Un curso por **ruta** de aprendizaje (`rutas/`).
- Una **sección** por módulo de la Escuela.
- En cada sección: recurso "URL" hacia las fuentes, una actividad y un cuestionario.

## Importar el glosario de fuentes
1. Ejecuta el flujo de publicación (o `python scripts/exportar_moodle.py`) para generar `moodle/export/glosario-fuentes.xml`.
2. En Moodle: curso → Glosario → Importar entradas → sube el XML.
Formato experimental: pruébalo primero en un curso de práctica.

## Banco de preguntas
`moodle/plantillas/banco-ejemplo.gift` usa el formato GIFT (Banco de preguntas → Importar → GIFT).
