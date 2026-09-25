# Modelo: Coursera + Canva + Moodle

## Coursera → catálogo y rutas
| Concepto Coursera | En la biblioteca |
|---|---|
| Catálogo de cursos | Catálogo de fuentes (`catalogo/fuentes/`) |
| Especialización | Ruta de aprendizaje (`rutas/`), agrupa cursos de la Escuela |
| Curso, módulos, lecturas | Cursos y módulos de mecanica-social-escuela + fuentes vinculadas |
| Progreso del aprendiz | Casillas de avance en el sitio (guardadas en el navegador de cada persona) |
| Certificado | Fuera de alcance de este repositorio; lo define la Escuela |

## Canva → método visual
Marca única (paleta y tipografías), plantillas reutilizables y flujo: brief → diseño → revisión humana → publicación. Ver `canva/`.

## Moodle → aula virtual
Moodle entrega los cursos; la biblioteca es la **fuente de contenidos**. `scripts/exportar_moodle.py` genera archivos importables (glosario XML y listado CSV). Ver `moodle/README.md`.

## Límites (honestidad técnica)
- GitHub Pages es un sitio estático: no hay cuentas de usuario, certificados ni seguimiento centralizado.
- Moodle es software gratuito, pero requiere un servidor; este repositorio no lo aloja. Ver `docs/software-gratuito.md`.
- Canva es una herramienta externa y su Brand Kit es de pago: aquí solo se guardan la guía y los enlaces. Alternativa libre: Penpot.
