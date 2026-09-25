# Mecánica Social Biblioteca

> Fuentes, bibliografía y conocimiento al servicio de la colaboración.

Repositorio institucional de la ONG Mecánica Social que organiza las fuentes de conocimiento del ecosistema:
cada fuente se cataloga, se verifica por una persona, se agrupa en **rutas de aprendizaje** y se vincula con
los cursos de la Escuela y con el aula virtual Moodle.

## Tres marcos, una biblioteca

| Marco | Qué aporta | Dónde vive en este repo |
|---|---|---|
| **Coursera** | Catálogo, rutas (especializaciones), progreso del aprendiz | `catalogo/`, `rutas/`, `site/` |
| **Canva** | Marca, plantillas y método de diseño de materiales | `canva/` |
| **Moodle** | Aula virtual y exportaciones para cursos | `moodle/`, `scripts/exportar_moodle.py` |

Detalle en [`docs/modelo-tres-marcos.md`](docs/modelo-tres-marcos.md). Todo el ecosistema usa software gratuito: [`docs/software-gratuito.md`](docs/software-gratuito.md).

La Escuela tiene **16 cursos**; las 4 rutas los agrupan sin repetir ni omitir ninguno (lo verifica la validación automática).

## Ecosistema

| Repositorio | Rol |
|---|---|
| mecanica-social-institucional | Página principal, estrategia y gestión |
| mecanica-social-escuela | Programas, recursos y evidencias formativas |
| mecanica-social-ia | Sistema institucional de inteligencia artificial |
| **mecanica-social-biblioteca** | Fuentes, bibliografía y conocimiento (este repositorio) |

## Estructura

```
catalogo/fuentes/    una ficha .md por fuente (metadatos + resumen propio)
catalogo/esquemas/   reglas de los metadatos
rutas/               rutas de aprendizaje (agrupan cursos de la Escuela)
canva/               marca, plantillas y guía de diseño
moodle/              guía, plantillas y exportaciones para Moodle
docs/                metodología, curaduría y derechos
scripts/             validación, índice y exportación (Python)
site/                sitio web del catálogo (GitHub Pages)
```

## Cómo agregar una fuente

1. Copia `catalogo/fuentes/_plantilla.md` con un nombre nuevo (por ejemplo `fuente-0004.md`).
2. Completa los metadatos y escribe el resumen **con tus palabras**.
3. Guarda con **Commit changes**. GitHub valida la ficha automáticamente y actualiza el sitio.

## Reglas de oro

- No se inventan fuentes, citas ni estadísticas.
- No se copian textos protegidos: se resume, se cita brevemente y se enlaza.
- Toda fuente pasa por revisión humana antes de quedar `aprobado`.
- Licencia del repositorio: pendiente de definición institucional.
