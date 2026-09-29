"""
Versión anterior: solo validaba las fuentes que YA habían llegado al catálogo público.
Si una ficha tenía un error que la excluía antes de llegar ahí (ej. 'estado: aprobada' en
vez de 'aprobado', un typo de género), el validador nunca la veía — desaparecía del sitio
en silencio, sin ✓ ni ❌. Así pasó con fuente-0004 el 26 de septiembre de 2026.

Esta versión corrige eso en dos frentes:
1. Valida CADA ficha en catalogo/fuentes/ y rutas/ contra el schema, exista o no en el
   catálogo publicado — así un valor de 'estado' o 'licencia' inválido se detecta siempre,
   no solo cuando la ficha ya está aprobada.
2. Compara qué fichas fuente existen contra cuáles llegaron al catálogo público, y avisa
   (⚠, sin bloquear el build) por cada una que quedó fuera, explicando el motivo — para que
   un curador vea explícitamente "esta ficha no se publicó, y esta es la razón" en vez de
   que simplemente no aparezca en el sitio sin explicación.

No usa la librería jsonschema (para no depender de un pip install nuevo); implementa a mano
el subconjunto de JSON Schema que este proyecto realmente usa.
"""

import json
import os
import re
import sys

from _comunes import parse_frontmatter

RUTA_SCHEMA = "catalogo/esquemas/catalogo.schema.json"
RUTA_CATALOGO = "site/catalogo.json"
CARPETA_FUENTES = "catalogo/fuentes"
CARPETA_RUTAS = "rutas"

errores = []
advertencias = []


def error(msg):
    errores.append(msg)


def advertencia(msg):
    advertencias.append(msg)


def validar_objeto(obj, definicion, etiqueta, exigir_obligatorios=True):
    """Valida tipos, enums y patrones de los campos presentes en `obj`.
    exigir_obligatorios=False se usa para fichas que aún no están aprobadas (pueden
    legítimamente faltarles campos que solo se completan al aprobar) — pero incluso así,
    cualquier campo que SÍ esté presente se valida igual, y la condición 'si aprobado,
    exige fechas de revisión' se aplica siempre, sea o no una ficha ya publicada."""
    if exigir_obligatorios:
        for campo in definicion.get("required", []):
            if campo not in obj:
                error(f"{etiqueta}: falta el campo obligatorio '{campo}'")

    for campo, spec in definicion.get("properties", {}).items():
        if campo not in obj:
            continue
        valor = obj[campo]
        tipo_esperado = spec.get("type")

        if tipo_esperado == "string" and not isinstance(valor, str):
            error(f"{etiqueta}: '{campo}' debería ser texto, llegó como {type(valor).__name__} ({valor!r})")
            continue
        if tipo_esperado == "integer" and not isinstance(valor, int):
            error(f"{etiqueta}: '{campo}' debería ser un número entero, llegó como {type(valor).__name__} ({valor!r})")
            continue
        if tipo_esperado == "array" and not isinstance(valor, list):
            error(
                f"{etiqueta}: '{campo}' debería ser una lista, llegó como {type(valor).__name__} "
                f"({valor!r}). Revisa scripts/_comunes.py."
            )
            continue

        if "enum" in spec and valor not in spec["enum"]:
            error(f"{etiqueta}: '{campo}'={valor!r} no es un valor permitido. Válidos: {spec['enum']}")

        if "pattern" in spec and isinstance(valor, str) and not re.match(spec["pattern"], valor):
            error(f"{etiqueta}: '{campo}'={valor!r} no cumple el formato esperado ({spec['pattern']})")

    # Esta condición corre SIEMPRE, publicada o no: si dice estado=aprobado, exige fechas.
    for condicion in definicion.get("allOf", []):
        condiciones_si = condicion.get("if", {}).get("properties", {})
        cumple = all(obj.get(campo) == cond.get("const") for campo, cond in condiciones_si.items())
        if cumple:
            for campo in condicion.get("then", {}).get("required", []):
                if campo not in obj:
                    error(f"{etiqueta}: al estar 'aprobado' debe tener el campo '{campo}'")


def cargar_fichas(carpeta):
    fichas = []
    if not os.path.isdir(carpeta):
        return fichas
    for nombre in sorted(os.listdir(carpeta)):
        if nombre.endswith(".md") and not nombre.startswith("_"):
            datos = parse_frontmatter(os.path.join(carpeta, nombre))
            if datos:
                fichas.append((nombre, datos))
    return fichas


def motivo_no_publicada(ficha, enum_estado):
    if ficha.get("estado") not in enum_estado:
        return f"'estado'={ficha.get('estado')!r} no es un valor válido — revisa si es un error de tipeo"
    if ficha.get("estado") != "aprobado":
        return f"estado es '{ficha.get('estado')}', no 'aprobado' (correcto si aún es borrador)"
    if ficha.get("tipo") == "documento-interno":
        return "tipo es 'documento-interno' (correcto, así se diseñó: nunca se publica)"
    return "motivo no identificado — revisar manualmente"


def validar_coherencia_rutas(fichas_fuente, fichas_ruta):
    """Las rutas que declara una fuente deben ser exactamente las rutas que contienen sus
    modulos (cursos). Antes nada lo comprobaba, y las fichas podían quedar declarando una
    ruta que no correspondía (por ejemplo, confundir el curso '03' con la 'ruta-03')."""
    modulos_por_ruta = {r.get("id"): set(r.get("modulos", [])) for _, r in fichas_ruta}
    modulos_en_alguna_ruta = set()
    for ms in modulos_por_ruta.values():
        modulos_en_alguna_ruta |= ms

    for nombre, f in fichas_fuente:
        etiqueta = f"{CARPETA_FUENTES}/{nombre}"
        modulos = f.get("modulos", [])
        declaradas = f.get("rutas", [])
        if not isinstance(modulos, list) or not isinstance(declaradas, list):
            continue  # el tipo incorrecto ya lo reporta validar_objeto

        for m in modulos:
            if m not in modulos_en_alguna_ruta:
                advertencia(f"{etiqueta}: el módulo '{m}' no pertenece a ninguna ruta en rutas/")

        esperadas = sorted(r for r, ms in modulos_por_ruta.items() if ms & set(modulos))
        if sorted(declaradas) != esperadas:
            error(
                f"{etiqueta}: 'rutas' declara {sorted(declaradas)} pero, según sus 'modulos' "
                f"{modulos}, debería ser {esperadas}"
            )


def main():
    try:
        schema = json.load(open(RUTA_SCHEMA, encoding="utf-8"))
    except FileNotFoundError:
        print(f"❌ No se encuentra {RUTA_SCHEMA}")
        sys.exit(1)

    def_fuente = schema["definitions"]["fuente"]
    def_ruta = schema["definitions"]["ruta"]

    # Paso nuevo: validar cada ficha fuente y ruta individual, esté publicada o no.
    fichas_fuente = cargar_fichas(CARPETA_FUENTES)
    fichas_ruta = cargar_fichas(CARPETA_RUTAS)

    for nombre, ficha in fichas_fuente:
        validar_objeto(ficha, def_fuente, f"{CARPETA_FUENTES}/{nombre}", exigir_obligatorios=False)

    for nombre, ficha in fichas_ruta:
        validar_objeto(ficha, def_ruta, f"{CARPETA_RUTAS}/{nombre}", exigir_obligatorios=False)

    validar_coherencia_rutas(fichas_fuente, fichas_ruta)

    try:
        catalogo = json.load(open(RUTA_CATALOGO, encoding="utf-8"))
    except FileNotFoundError:
        print(f"❌ No se encuentra {RUTA_CATALOGO}. Corre construir_indice.py antes de validar.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ {RUTA_CATALOGO} no es JSON válido: {e}")
        sys.exit(1)

    for campo in schema.get("required", []):
        if campo not in catalogo:
            error(f"catálogo: falta el campo obligatorio de nivel superior '{campo}'")

    ids_fuentes_publicadas = {f.get("id") for f in catalogo.get("fuentes", [])}
    for f in catalogo.get("fuentes", []):
        etiqueta = f"fuente {f.get('id', '<sin id>')} (publicada)"
        validar_objeto(f, def_fuente, etiqueta, exigir_obligatorios=True)
        if f.get("tipo") == "documento-interno" or f.get("estado") != "aprobado":
            error(f"{etiqueta}: es documento-interno o no está aprobada — NO debería estar en el catálogo público")

    ids_rutas_publicadas = {r.get("id") for r in catalogo.get("rutas", [])}
    for r in catalogo.get("rutas", []):
        etiqueta = f"ruta {r.get('id', '<sin id>')} (publicada)"
        validar_objeto(r, def_ruta, etiqueta, exigir_obligatorios=True)
        if r.get("estado") != "aprobado":
            error(f"{etiqueta}: no está aprobada — NO debería estar en el catálogo público")

    # Paso nuevo: avisar por cada ficha fuente/ruta que existe pero no llegó al catálogo.
    enum_estado_fuente = def_fuente["properties"]["estado"]["enum"]
    enum_estado_ruta = def_ruta["properties"]["estado"]["enum"]

    for nombre, ficha in fichas_fuente:
        if ficha.get("id") not in ids_fuentes_publicadas:
            advertencia(f"{CARPETA_FUENTES}/{nombre} (id={ficha.get('id')!r}): {motivo_no_publicada(ficha, enum_estado_fuente)}")

    for nombre, ficha in fichas_ruta:
        if ficha.get("id") not in ids_rutas_publicadas:
            advertencia(f"{CARPETA_RUTAS}/{nombre} (id={ficha.get('id')!r}): {motivo_no_publicada(ficha, enum_estado_ruta)}")

    if errores:
        print(f"❌ Validación fallida: {len(errores)} problema(s) encontrado(s)\n")
        for e in errores:
            print(f"  - {e}")
        sys.exit(1)

    print(
        f"✓ {RUTA_CATALOGO} cumple catalogo.schema.json: "
        f"{len(catalogo.get('fuentes', []))} fuente(s) y {len(catalogo.get('rutas', []))} ruta(s), "
        f"todas aprobadas y públicas."
    )

    if advertencias:
        print(f"\n⚠ {len(advertencias)} ficha(s) fuera del catálogo público (revisa si es intencional):")
        for a in advertencias:
            print(f"  - {a}")


if __name__ == "__main__":
    main()
