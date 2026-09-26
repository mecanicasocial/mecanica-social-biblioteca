"""
Módulo compartido entre construir_indice.py y exportar_moodle.py.

Existe por una razón concreta: el 25-26 de septiembre de 2026, construir_indice.py y
exportar_moodle.py tenían cada uno su propia copia de la regla "qué fuente es publicable".
Una de las dos copias se perdió al reescribir el script, y 3 fuentes internas en borrador
se filtraron al catálogo público sin que nadie lo notara. Para que eso no pueda repetirse,
la regla vive en un solo lugar: es_fuente_publicable(), abajo. Ningún script debe volver a
implementar su propia versión de este filtro.
"""

import re

CAMPOS_LISTA = {"rutas", "modulos", "etiquetas"}


def _quitar_comillas(valor):
    valor = valor.strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in ('"', "'"):
        return valor[1:-1]
    return valor


def _convertir_valor(clave, valor_crudo):
    valor = valor_crudo.strip()
    if clave in CAMPOS_LISTA:
        interior = valor
        if interior.startswith("[") and interior.endswith("]"):
            interior = interior[1:-1]
        interior = interior.strip()
        if not interior:
            return []
        return [_quitar_comillas(item.strip()) for item in interior.split(",") if item.strip()]
    valor = _quitar_comillas(valor)
    if clave == "anio":
        try:
            return int(valor)
        except ValueError:
            return valor
    return valor


def parse_frontmatter(ruta_archivo):
    """Lee un .md con frontmatter y devuelve un dict, o None si no tiene frontmatter válido.
    Entiende: texto plano, texto entre comillas, listas simples tipo [a, b, c], y enteros
    en el campo 'anio'. No es un parser YAML completo (no entiende listas anidadas ni
    bloques multilínea), pero cubre todo lo que usan las fichas reales de este proyecto."""
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    if not contenido.startswith("---"):
        return None
    partes = contenido.split("---", 2)
    if len(partes) < 3:
        return None

    bloque_frontmatter, cuerpo = partes[1], partes[2].strip()
    datos = {}
    for linea in bloque_frontmatter.strip().split("\n"):
        linea = linea.rstrip()
        if not linea or linea.lstrip().startswith("#") or ":" not in linea:
            continue
        clave, _, valor_crudo = linea.partition(":")
        clave = clave.strip()
        datos[clave] = _convertir_valor(clave, valor_crudo)

    datos["resumen"] = cuerpo
    return datos


def es_fuente_publicable(ficha):
    """Única función que decide si una fuente sale al catálogo público."""
    return ficha.get("estado") == "aprobado" and ficha.get("tipo") != "documento-interno"


def es_ruta_publicable(ficha):
    """Única función que decide si una ruta sale al catálogo público."""
    return ficha.get("estado") == "aprobado"