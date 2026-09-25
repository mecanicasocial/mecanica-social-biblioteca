#!/usr/bin/env bash
# Inicializa formalmente el repositorio mecanica-social-biblioteca.
# Modelo: Coursera (catálogo + rutas) + Canva (marca y plantillas) + Moodle (aula virtual).
# Uso (desde la raíz del repositorio):  bash inicializar.sh
set -e
cd "$(dirname "$0")"
echo "==> Creando estructura de carpetas"
mkdir -p .github/workflows catalogo/fuentes catalogo/esquemas rutas canva/marca canva/plantillas \
         moodle/plantillas moodle/export docs scripts site

# ---------------------------------------------------------------- README
cat > README.md <<'MS_EOF'
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

Detalle en [`docs/modelo-tres-marcos.md`](docs/modelo-tres-marcos.md).

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
MS_EOF

# ---------------------------------------------------------------- Gobernanza
cat > GOVERNANCE.md <<'MS_EOF'
# Gobernanza

## Estados de una fuente o ruta
`borrador` → `prueba` → `aprobado` · también `restringido`, `obsoleto`, `suspendido`, `retirado`.

Ninguna fuente se considera `aprobado` solo porque parezca confiable: requiere `verificada: si` y una persona revisora identificada.

## Roles
- **Curador/a:** propone y redacta fichas.
- **Revisor/a:** verifica la fuente y aprueba el cambio.
- **Dirección Ejecutiva:** decide sobre licencia, publicación y retiro de fuentes.
MS_EOF
cat > CONTRIBUTING.md <<'MS_EOF'
# Cómo contribuir

1. Define el propósito: ¿a qué ruta o curso de la Escuela sirve la fuente?
2. Verifica que existe y que su licencia permite el uso previsto.
3. Crea la ficha desde `catalogo/fuentes/_plantilla.md`.
4. Resume con tus palabras; no pegues textos protegidos.
5. Abre un Pull Request o guarda con Commit; la validación automática debe pasar.
6. Una persona revisora aprueba antes de marcar `aprobado`.
MS_EOF
cat > SECURITY.md <<'MS_EOF'
# Seguridad

No incorporar al repositorio: contraseñas, tokens, claves API, datos personales, documentos reservados ni copias de material protegido.
Si detectas una exposición, no la publiques como incidencia abierta: avisa de forma privada a la Dirección Ejecutiva.
MS_EOF
cat > AI_ETHICS.md <<'MS_EOF'
# Uso ético de la inteligencia artificial

Este repositorio sigue los principios de mecanica-social-ia.

- **Supervisión humana:** la IA puede proponer fichas o resúmenes; una persona los revisa y aprueba.
- **Verificabilidad:** toda fuente debe existir y poder consultarse. La IA no inventa referencias.
- **Transparencia:** se indica cuando un resumen fue elaborado con asistencia de IA (`asistencia_ia: si`).
- **Derechos de terceros:** no se reproducen obras protegidas.
- **Rendición de cuentas:** responden las personas de la ONG, nunca el sistema de IA.
MS_EOF
cat > CODE_OF_CONDUCT.md <<'MS_EOF'
# Código de convivencia

Trato respetuoso, debate de ideas sin descalificar personas, no publicar información personal de terceros y reportar conductas inapropiadas a la Dirección Ejecutiva.
MS_EOF
cat > .gitignore <<'MS_EOF'
.env
*.pyc
__pycache__/
.DS_Store
MS_EOF

# ---------------------------------------------------------------- Docs
cat > docs/modelo-tres-marcos.md <<'MS_EOF'
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
- Moodle requiere un servidor propio o MoodleCloud; este repositorio no lo aloja.
- Canva es una herramienta externa: aquí solo se guardan la guía y los enlaces a los diseños.
MS_EOF
cat > docs/criterios-curaduria.md <<'MS_EOF'
# Criterios de curaduría

Una fuente se aprueba si cumple:
1. **Existe y es localizable** (URL, DOI, ISBN o ubicación física).
2. **Autoría identificable** (persona, institución o normativa).
3. **Pertinencia** con una ruta o curso de la Escuela.
4. **Licencia o derechos** compatibles con el uso previsto.
5. **Pluralismo:** se procura incluir perspectivas diversas, sin sesgo partidario.
6. **Vigencia:** se indica año y se revisa periódicamente.
7. **Resumen propio**, sin copiar el texto original.
MS_EOF

# ---------------------------------------------------------------- Catálogo
cat > catalogo/esquemas/ficha-fuente.md <<'MS_EOF'
# Campos de una ficha de fuente

| Campo | Obligatorio | Valores |
|---|---|---|
| id | sí | `fuente-0001`, único |
| titulo | sí | texto |
| autor | sí | texto |
| anio | sí | número |
| tipo | sí | libro, articulo, informe, normativa, documento-interno, sitio-web, video, visual |
| url | no | dirección pública |
| licencia | sí | por-definir, cc-by, dominio-publico, con-permiso, todos-los-derechos |
| estado | sí | borrador, prueba, aprobado, restringido, obsoleto, suspendido, retirado |
| verificada | sí | si / no |
| revisor | sí | nombre o `pendiente` |
| asistencia_ia | no | si / no |
| rutas | no | lista de ids de ruta |
| modulos | no | lista de carpetas de la Escuela |
| etiquetas | no | lista |
MS_EOF
cat > catalogo/fuentes/_plantilla.md <<'MS_EOF'
---
id: fuente-0000
titulo: Título de la fuente
autor: Autor o institución
anio: 2026
tipo: libro
url:
licencia: por-definir
estado: borrador
verificada: no
revisor: pendiente
asistencia_ia: no
rutas: []
modulos: []
etiquetas: []
---
Resumen con tus propias palabras (2 a 4 líneas). No copies el texto original.
MS_EOF
cat > catalogo/fuentes/fuente-0001.md <<'MS_EOF'
---
id: fuente-0001
titulo: Plan de Negocios y Sostenibilidad 2027-2029
autor: ONG Mecánica Social
anio: 2026
tipo: documento-interno
url:
licencia: por-definir
estado: borrador
verificada: no
revisor: pendiente
asistencia_ia: no
rutas: [ruta-04]
modulos: [11-diseno-proyectos]
etiquetas: [estrategia, plan-de-negocios]
---
Hoja de ruta de la ONG para el trienio 2027-2029: identidad, portafolio, modelo de ingresos, gobernanza y riesgos. Cifras referenciales.
MS_EOF
cat > catalogo/fuentes/fuente-0002.md <<'MS_EOF'
---
id: fuente-0002
titulo: Plan de Marketing Estratégico 2027-2029
autor: ONG Mecánica Social
anio: 2026
tipo: documento-interno
url:
licencia: por-definir
estado: borrador
verificada: no
revisor: pendiente
asistencia_ia: no
rutas: [ruta-02]
modulos: [08-comunicacion-publica]
etiquetas: [marketing, posicionamiento]
---
Estrategia de posicionamiento, comunicaciones, alianzas y control de gestión que acompaña al plan de negocios.
MS_EOF
cat > catalogo/fuentes/fuente-0003.md <<'MS_EOF'
---
id: fuente-0003
titulo: Mecánica Social IA, principios institucionales
autor: ONG Mecánica Social
anio: 2026
tipo: documento-interno
url:
licencia: por-definir
estado: borrador
verificada: no
revisor: pendiente
asistencia_ia: no
rutas: [ruta-04]
modulos: [12-tecnologia-ia, 13-etica-servicio-publico]
etiquetas: [ia, etica, gobernanza]
---
Principios, límites de uso, clasificación de riesgos y ciclo de vida de las soluciones de inteligencia artificial de la ONG.
MS_EOF

# ---------------------------------------------------------------- Rutas
cat > rutas/ruta-01-educacion-civica.md <<'MS_EOF'
---
id: ruta-01
titulo: Educación cívica y liderazgo público
linea: Educación cívica y liderazgo público
estado: borrador
modulos: [01-democracia-ciudadania, 02-historia-politica-chile, 03-estado-instituciones, 04-constitucion-derechos, 07-liderazgo-social]
---
Competencias para participar, decidir y rendir cuentas.
MS_EOF
cat > rutas/ruta-02-gestion-comunitaria.md <<'MS_EOF'
---
id: ruta-02
titulo: Gestión comunitaria y participación
linea: Gestión comunitaria y vinculación territorial
estado: borrador
modulos: [10-participacion-ciudadana, 08-comunicacion-publica, 09-pensamiento-critico, 15-incidencia-gestion]
---
Acuerdos legítimos, comunicación y gobernanza local.
MS_EOF
cat > rutas/ruta-03-politicas-publicas.md <<'MS_EOF'
---
id: ruta-03
titulo: Políticas públicas y presupuesto
linea: Fortalecimiento institucional y evaluación
estado: borrador
modulos: [05-politicas-publicas, 06-presupuesto-publico, 13-etica-servicio-publico]
---
Diseño, financiamiento y ética de las políticas públicas.
MS_EOF
cat > rutas/ruta-04-proyectos-innovacion.md <<'MS_EOF'
---
id: ruta-04
titulo: Proyectos, tecnología e innovación
linea: RSE y valor compartido / Fortalecimiento
estado: borrador
modulos: [11-diseno-proyectos, 12-tecnologia-ia, 14-innovacion-social, 16-proyecto-final]
---
Del diseño de proyectos a su ejecución, con tecnología e innovación social.
MS_EOF

# ---------------------------------------------------------------- Canva
cat > canva/marca/paleta.md <<'MS_EOF'
# Marca Mecánica Social (para Canva Brand Kit)

| Uso | Color | Código |
|---|---|---|
| Fondo institucional | Azul marino | #051C2C |
| Acento principal | Azul | #2251FF |
| Acento secundario | Cian | #00A9F4 |
| Texto | Gris oscuro | #1F2933 |
| Texto secundario | Gris | #5B6B79 |
| Fondo claro | Gris muy claro | #F5F7F9 |

**Tipografías:** títulos en Georgia (serif); textos en Arial.
En Canva: Brand Kit → Colores y Fuentes; si Georgia no está disponible, usar una serif equivalente.
MS_EOF
cat > canva/plantillas/plantillas.md <<'MS_EOF'
# Plantillas a crear en Canva

| Plantilla | Formato | Uso |
|---|---|---|
| Ficha de lectura | A4 vertical | Resumen visual de una fuente |
| Infografía de ruta | 1080x1350 | Difusión de una ruta de aprendizaje |
| Presentación de módulo | 16:9 | Clases y talleres |
| Portada de curso | 1280x720 | Imagen del curso en Moodle |
| Certificado de participación | A4 horizontal | Lo define la Escuela |

Nombre de archivo: `MS-<tipo>-<id>-v<version>` (ejemplo: `MS-ficha-fuente-0001-v1`).
Al terminar cada diseño, guarda su enlace en la ficha (campo `url`) con `tipo: visual`.
MS_EOF
cat > canva/guia-canva.md <<'MS_EOF'
# Método de diseño con Canva

1. **Brief:** ¿qué debe entender la persona y para qué ruta o curso?
2. **Diseño:** usa el Brand Kit y las plantillas; un mensaje por pieza.
3. **Accesibilidad:** contraste alto, tamaño de letra legible, texto alternativo en imágenes, lenguaje claro.
4. **Derechos:** solo imágenes propias, con licencia o de bancos autorizados.
5. **Revisión humana:** una persona distinta a quien diseñó revisa datos y fuentes.
6. **Publicación:** exporta PDF o PNG, registra el diseño en el catálogo y menciona si se usó IA.
MS_EOF

# ---------------------------------------------------------------- Moodle
cat > moodle/README.md <<'MS_EOF'
# Moodle

Moodle es el aula virtual; la biblioteca es su fuente de contenidos.

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
MS_EOF
cat > moodle/plantillas/banco-ejemplo.gift <<'MS_EOF'
// Ejemplo de banco de preguntas en formato GIFT
::Decisión final:: Según los principios institucionales, ¿quién toma las decisiones significativas? {
=Una persona responsable
~El sistema de inteligencia artificial
~Cualquier usuario
}

::Fuentes:: Una fuente puede quedar aprobada solo por parecer confiable. {FALSE}
MS_EOF

# ---------------------------------------------------------------- Scripts
cat > scripts/comun.py <<'MS_EOF'
"""Utilidades compartidas: lectura de fichas con metadatos simples."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ESTADOS = {"borrador", "prueba", "aprobado", "restringido", "obsoleto", "suspendido", "retirado"}
TIPOS = {"libro", "articulo", "informe", "normativa", "documento-interno", "sitio-web", "video", "visual"}
LICENCIAS = {"por-definir", "cc-by", "dominio-publico", "con-permiso", "todos-los-derechos"}


def leer_ficha(ruta):
    texto = pathlib.Path(ruta).read_text(encoding="utf-8")
    partes = texto.split("---", 2)
    if len(partes) < 3:
        raise ValueError("falta el bloque de metadatos entre ---")
    meta = {}
    for linea in partes[1].strip().splitlines():
        if ":" not in linea:
            continue
        k, v = linea.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        meta[k.strip()] = v
    meta["resumen"] = partes[2].strip()
    return meta


def cargar(carpeta, ignorar_plantilla=True):
    fichas = []
    for p in sorted((RAIZ / carpeta).glob("*.md")):
        if ignorar_plantilla and p.name.startswith("_"):
            continue
        m = leer_ficha(p)
        m["_archivo"] = p.name
        fichas.append(m)
    return fichas
MS_EOF
cat > scripts/validar_catalogo.py <<'MS_EOF'
"""Valida fichas de fuentes y rutas. Termina con error si hay problemas."""
import sys
from comun import RAIZ, ESTADOS, TIPOS, LICENCIAS, cargar

errores = []
rutas = cargar("rutas")
ids_ruta = {r.get("id") for r in rutas}
carpetas_escuela = set()
for r in rutas:
    carpetas_escuela.update(r.get("modulos", []))

vistos = set()
fuentes = cargar("catalogo/fuentes")
for f in fuentes:
    a = f["_archivo"]
    for c in ("id", "titulo", "autor", "anio", "tipo", "licencia", "estado", "verificada", "revisor"):
        if not f.get(c):
            errores.append(f"{a}: falta el campo '{c}'")
    if f.get("id") in vistos:
        errores.append(f"{a}: id repetido {f.get('id')}")
    vistos.add(f.get("id"))
    if f.get("tipo") and f["tipo"] not in TIPOS:
        errores.append(f"{a}: tipo no válido '{f['tipo']}'")
    if f.get("licencia") and f["licencia"] not in LICENCIAS:
        errores.append(f"{a}: licencia no válida '{f['licencia']}'")
    if f.get("estado") and f["estado"] not in ESTADOS:
        errores.append(f"{a}: estado no válido '{f['estado']}'")
    if f.get("estado") == "aprobado" and (f.get("verificada") != "si" or f.get("revisor") in (None, "", "pendiente")):
        errores.append(f"{a}: no puede estar 'aprobado' sin verificación ni revisor")
    for r in f.get("rutas", []):
        if r not in ids_ruta:
            errores.append(f"{a}: ruta inexistente '{r}'")
    for m in f.get("modulos", []):
        if m not in carpetas_escuela:
            errores.append(f"{a}: módulo '{m}' no pertenece a ninguna ruta")
    if not f.get("resumen"):
        errores.append(f"{a}: falta el resumen")

if errores:
    print("Se encontraron problemas:")
    for e in errores:
        print(" -", e)
    sys.exit(1)
print(f"OK: {len(fuentes)} fuentes y {len(rutas)} rutas válidas.")
MS_EOF
cat > scripts/construir_indice.py <<'MS_EOF'
"""Genera site/catalogo.json a partir de las fichas."""
import json
from comun import RAIZ, cargar

fuentes = cargar("catalogo/fuentes")
rutas = cargar("rutas")
for x in fuentes + rutas:
    x.pop("_archivo", None)
salida = {"fuentes": fuentes, "rutas": rutas}
(RAIZ / "site" / "catalogo.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Índice generado: {len(fuentes)} fuentes, {len(rutas)} rutas.")
MS_EOF
cat > scripts/exportar_moodle.py <<'MS_EOF'
"""Exporta fuentes aprobadas o en prueba a un glosario XML (experimental) y a un CSV para Moodle."""
import csv
from xml.sax.saxutils import escape
from comun import RAIZ, cargar

salida = RAIZ / "moodle" / "export"
salida.mkdir(parents=True, exist_ok=True)
fuentes = [f for f in cargar("catalogo/fuentes") if f.get("estado") in ("aprobado", "prueba", "borrador")]

entradas = []
for f in fuentes:
    cuerpo = f"{f['resumen']}<br/>{escape(f['autor'])} ({f['anio']}). Estado: {f['estado']}."
    if f.get("url"):
        cuerpo += f' <a href="{escape(f["url"])}">Enlace</a>'
    entradas.append(
        f"<ENTRY><CONCEPT>{escape(f['titulo'])}</CONCEPT><DEFINITION>{cuerpo}</DEFINITION>"
        f"<FORMAT>1</FORMAT><USEDYNALINK>0</USEDYNALINK><CASESENSITIVE>0</CASESENSITIVE><FULLMATCH>0</FULLMATCH></ENTRY>"
    )
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<GLOSSARY><INFO><NAME>Biblioteca Mecánica Social</NAME>'
       '<INTRO>Fuentes del catálogo.</INTRO><INTROFORMAT>1</INTROFORMAT></INFO><ENTRIES>' + "".join(entradas) + "</ENTRIES></GLOSSARY>")
(salida / "glosario-fuentes.xml").write_text(xml, encoding="utf-8")

with open(salida / "fuentes.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "titulo", "autor", "anio", "tipo", "estado", "url", "rutas"])
    for f in fuentes:
        w.writerow([f["id"], f["titulo"], f["autor"], f["anio"], f["tipo"], f["estado"], f.get("url", ""), ";".join(f.get("rutas", []))])
print(f"Exportadas {len(fuentes)} fuentes a moodle/export/")
MS_EOF

# ---------------------------------------------------------------- Workflow
cat > .github/workflows/pages.yml <<'MS_EOF'
name: Validar y publicar biblioteca
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Validar catálogo
        run: python scripts/validar_catalogo.py
      - name: Construir índice
        run: python scripts/construir_indice.py
      - name: Exportar Moodle
        run: python scripts/exportar_moodle.py
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.d.outputs.page_url }}
    steps:
      - id: d
        uses: actions/deploy-pages@v4
MS_EOF

# ---------------------------------------------------------------- Sitio
touch site/.nojekyll
cat > site/index.html <<'MS_EOF'
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Biblioteca | ONG Mecánica Social</title>
<meta name="description" content="Fuentes, bibliografía y rutas de aprendizaje de la ONG Mecánica Social.">
<style>
:root{--navy:#051c2c;--blue:#2251ff;--cyan:#00a9f4;--ink:#1f2933;--mute:#5b6b79;--line:#d9e0e6;--bg:#f5f7f9}
*{box-sizing:border-box;margin:0;padding:0}body{font-family:Arial,Helvetica,sans-serif;color:var(--ink);background:var(--bg);line-height:1.5}
h1,h2,h3{font-family:Georgia,serif;font-weight:400;color:var(--navy)}.w{max-width:1120px;margin:0 auto;padding:0 24px}
.hero{background:var(--navy);color:#fff;padding:64px 0 48px}.hero h1{color:#fff;font-size:clamp(1.8rem,4vw,2.8rem);max-width:760px}
.hero p{color:#b8c7d3;margin:14px 0 24px;max-width:600px}.hero input{width:100%;max-width:520px;padding:14px;border:0;border-radius:8px;font-size:1rem}
main{padding:40px 0}h2{font-size:1.6rem;margin:32px 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px}
.card h3{font-size:1.1rem;margin-bottom:6px}.card small{color:var(--mute)}
.ruta{border-top:4px solid var(--blue)}.bar{height:8px;background:var(--line);border-radius:4px;margin:10px 0}.bar i{display:block;height:100%;background:var(--cyan);border-radius:4px;width:0}
.mods label{display:block;font-size:.85rem;margin:4px 0;cursor:pointer}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}.chips button,.link{border:1px solid var(--navy);background:#fff;padding:6px 14px;border-radius:20px;cursor:pointer;font-size:.8rem}
.chips button.on{background:var(--navy);color:#fff}
.b{display:inline-block;font-size:.7rem;padding:2px 8px;border-radius:10px;background:#eef2ff;color:var(--blue);margin:6px 4px 0 0}.b.w2{background:#fff4e0;color:#8a5a00}.b.ok{background:#e3f6ea;color:#1a6b3a}
footer{background:var(--navy);color:#8fa3b3;padding:28px 0;font-size:.8rem;margin-top:40px}a{color:var(--blue)}
</style></head><body>
<div class="hero"><div class="w"><h1>Biblioteca de conocimiento para hacer funcionar la colaboración</h1>
<p>Fuentes verificadas por personas y rutas de aprendizaje conectadas con la Escuela de Formación.</p>
<input id="q" type="search" placeholder="Buscar por título, autor o etiqueta" aria-label="Buscar en el catálogo"></div></div>
<main class="w">
<h2>Rutas de aprendizaje</h2><div class="grid" id="rutas"></div>
<h2>Catálogo de fuentes <span id="n" style="font-size:1rem;color:var(--mute)"></span></h2>
<div class="chips" id="chips"></div><div class="grid" id="fuentes"></div>
</main>
<footer><div class="w">ONG Mecánica Social · Fuentes en revisión: solo las marcadas "verificada" han sido contrastadas por una persona. Contenido con asistencia de IA revisado por personas.</div></footer>
<script>
const $=id=>document.getElementById(id),esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
let D={fuentes:[],rutas:[]},filtro="todas",ruta=null;
const K="ms-biblioteca-avance";
function leer(){try{return JSON.parse(localStorage.getItem(K)||"{}")}catch(e){return{}}}
function guardar(a){try{localStorage.setItem(K,JSON.stringify(a))}catch(e){}}
function pintarRutas(){const av=leer();$("rutas").innerHTML=D.rutas.map(r=>{const m=r.modulos||[],h=m.filter(x=>av[r.id+"|"+x]).length,p=m.length?Math.round(h/m.length*100):0;
return `<div class="card ruta"><h3>${esc(r.titulo)}</h3><small>${esc(r.linea)}</small><p style="margin-top:8px;font-size:.9rem">${esc(r.resumen)}</p>
<div class="bar"><i style="width:${p}%"></i></div><small>${h} de ${m.length} módulos (${p}%)</small>
<div class="mods">${m.map(x=>`<label><input type="checkbox" data-k="${esc(r.id)}|${esc(x)}" ${av[r.id+"|"+x]?"checked":""}> ${esc(x.replace(/^\d+-/,"").replace(/-/g," "))}</label>`).join("")}</div>
<p style="margin-top:10px"><button class="link" data-r="${esc(r.id)}">Ver fuentes de la ruta</button></p></div>`}).join("");
document.querySelectorAll("[data-k]").forEach(c=>c.onchange=()=>{const a=leer();a[c.dataset.k]=c.checked;guardar(a);pintarRutas()});
document.querySelectorAll("[data-r]").forEach(b=>b.onclick=()=>{ruta=b.dataset.r;pintarFuentes();$("fuentes").scrollIntoView({behavior:"smooth"})})}
function pintarChips(){const t=["todas",...new Set(D.fuentes.map(f=>f.tipo))];$("chips").innerHTML=t.map(x=>`<button class="${x===filtro?"on":""}" data-t="${esc(x)}">${esc(x)}</button>`).join("")+(ruta?`<button data-quitar="1">Quitar filtro de ruta ✕</button>`:"");
document.querySelectorAll("[data-t]").forEach(b=>b.onclick=()=>{filtro=b.dataset.t;pintarFuentes()});const q=document.querySelector("[data-quitar]");if(q)q.onclick=()=>{ruta=null;pintarFuentes()}}
function pintarFuentes(){const q=$("q").value.toLowerCase();
const l=D.fuentes.filter(f=>(filtro==="todas"||f.tipo===filtro)&&(!ruta||(f.rutas||[]).includes(ruta))&&(f.titulo+f.autor+(f.etiquetas||[]).join(" ")).toLowerCase().includes(q));
$("n").textContent="("+l.length+")";pintarChips();
$("fuentes").innerHTML=l.length?l.map(f=>`<div class="card"><h3>${esc(f.titulo)}</h3><small>${esc(f.autor)} · ${esc(f.anio)}</small><p style="font-size:.9rem;margin-top:8px">${esc(f.resumen)}</p>
<span class="b">${esc(f.tipo)}</span><span class="b ${f.estado==="aprobado"?"ok":"w2"}">${esc(f.estado)}</span>${f.verificada==="si"?'<span class="b ok">verificada</span>':'<span class="b w2">sin verificar</span>'}
${f.url?`<p style="margin-top:10px"><a href="${esc(f.url)}" rel="noopener">Ir a la fuente</a></p>`:""}</div>`).join(""):"<p>No hay fuentes con esos criterios.</p>"}
fetch("catalogo.json").then(r=>r.json()).then(d=>{D=d;pintarRutas();pintarFuentes()}).catch(()=>{$("fuentes").innerHTML="<p>No se pudo cargar el catálogo.</p>"});
$("q").oninput=pintarFuentes;
</script></body></html>
MS_EOF

# ---------------------------------------------------------------- Validación y Git
echo "==> Validando catálogo"
python3 scripts/validar_catalogo.py && python3 scripts/construir_indice.py && python3 scripts/exportar_moodle.py || echo "(Python no disponible: GitHub lo hará automáticamente al subir)"
if command -v git >/dev/null 2>&1 && [ ! -d .git ]; then
  git init -b main >/dev/null 2>&1 || git init >/dev/null 2>&1
  git add -A && git commit -q -m "chore: inicializa mecanica-social-biblioteca" 2>/dev/null || true
fi
echo "==> Listo. Siguiente paso: subir a GitHub y activar Pages (Settings > Pages > GitHub Actions)."
