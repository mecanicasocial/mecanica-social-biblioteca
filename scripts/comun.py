"""Utilidades compartidas: lectura de fichas con metadatos simples."""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CURSOS_ESCUELA = [
    "01-democracia-ciudadania", "02-historia-politica-chile", "03-estado-instituciones", "04-constitucion-derechos",
    "05-politicas-publicas", "06-presupuesto-publico", "07-liderazgo-social", "08-comunicacion-publica",
    "09-pensamiento-critico", "10-participacion-ciudadana", "11-diseno-proyectos", "12-tecnologia-ia",
    "13-etica-servicio-publico", "14-innovacion-social", "15-incidencia-gestion", "16-proyecto-final",
]
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
