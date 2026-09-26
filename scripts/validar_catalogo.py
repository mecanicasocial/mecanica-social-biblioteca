"""
Antes, este script solo revisaba que existieran ciertos nombres de campo, sin comprobar
tipos, enums ni patrones — e imprimía "APROBADO" incluso cuando el catálogo publicado
tenía fuentes en borrador. Esta versión sí lee catalogo.schema.json y aplica sus reglas:
required, type, enum, pattern, y la condición "si aprobado, exige fechas de revisión".
No usa la librería jsonschema (para no depender de un pip install nuevo); implementa
a mano el subconjunto de JSON Schema que este proyecto realmente usa.
"""

import json
import re
import sys

RUTA_SCHEMA = "catalogo/esquemas/catalogo.schema.json"
RUTA_CATALOGO = "site/catalogo.json"

errores = []


def error(msg):
    errores.append(msg)


def validar_objeto(obj, definicion, etiqueta):
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
                f"({valor!r}). Si ves algo como '[ruta-04]' entre comillas, el parser de "
                f"construir_indice.py no está interpretando la lista — revisa scripts/_comunes.py."
            )
            continue

        if "enum" in spec and valor not in spec["enum"]:
            error(f"{etiqueta}: '{campo}'={valor!r} no es un valor permitido. Válidos: {spec['enum']}")

        if "pattern" in spec and isinstance(valor, str) and not re.match(spec["pattern"], valor):
            error(f"{etiqueta}: '{campo}'={valor!r} no cumple el formato esperado ({spec['pattern']})")

    for condicion in definicion.get("allOf", []):
        condiciones_si = condicion.get("if", {}).get("properties", {})
        cumple = all(obj.get(campo) == cond.get("const") for campo, cond in condiciones_si.items())
        if cumple:
            for campo in condicion.get("then", {}).get("required", []):
                if campo not in obj:
                    error(f"{etiqueta}: al estar 'aprobado' debe tener el campo '{campo}'")


def main():
    try:
        schema = json.load(open(RUTA_SCHEMA, encoding="utf-8"))
    except FileNotFoundError:
        print(f"❌ No se encuentra {RUTA_SCHEMA}")
        sys.exit(1)

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

    def_fuente = schema["definitions"]["fuente"]
    def_ruta = schema["definitions"]["ruta"]

    for f in catalogo.get("fuentes", []):
        etiqueta = f"fuente {f.get('id', '<sin id>')}"
        validar_objeto(f, def_fuente, etiqueta)
        # Segunda comprobación, redundante a propósito: aunque el schema no lo exprese como
        # regla de negocio, revalidamos aquí la barrera de seguridad como defensa adicional.
        if f.get("tipo") == "documento-interno" or f.get("estado") != "aprobado":
            error(f"{etiqueta}: es documento-interno o no está aprobada — NO debería estar en el catálogo público")

    for r in catalogo.get("rutas", []):
        etiqueta = f"ruta {r.get('id', '<sin id>')}"
        validar_objeto(r, def_ruta, etiqueta)
        if r.get("estado") != "aprobado":
            error(f"{etiqueta}: no está aprobada — NO debería estar en el catálogo público")

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


if __name__ == "__main__":
    main()