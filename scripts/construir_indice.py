import os
import json
import datetime

from _comunes import parse_frontmatter, es_fuente_publicable, es_ruta_publicable


def cargar_fichas(carpeta):
    fichas = []
    if not os.path.isdir(carpeta):
        return fichas
    for nombre in sorted(os.listdir(carpeta)):
        if nombre.endswith(".md") and not nombre.startswith("_"):
            datos = parse_frontmatter(os.path.join(carpeta, nombre))
            if datos:
                fichas.append(datos)
    return fichas


def build():
    todas_fuentes = cargar_fichas("catalogo/fuentes")
    todas_rutas = cargar_fichas("rutas")

    fuentes_publicas = [f for f in todas_fuentes if es_fuente_publicable(f)]
    rutas_publicas = [r for r in todas_rutas if es_ruta_publicable(r)]

    excluidas_fuentes = len(todas_fuentes) - len(fuentes_publicas)
    excluidas_rutas = len(todas_rutas) - len(rutas_publicas)

    catalogo = {
        "version": "1.0.0",
        "generado_en": datetime.datetime.now().isoformat(),
        "auditoria_estado": (
            f"Saneado - {excluidas_fuentes} fuente(s) y {excluidas_rutas} ruta(s) "
            f"excluida(s) por no estar aprobadas o ser documento-interno"
        ),
        "fuentes": fuentes_publicas,
        "rutas": rutas_publicas,
    }

    os.makedirs("site", exist_ok=True)
    with open("site/catalogo.json", "w", encoding="utf-8") as f:
        json.dump(catalogo, f, indent=2, ensure_ascii=False)

    print(f"✓ site/catalogo.json generado: {len(fuentes_publicas)} de {len(todas_fuentes)} fuentes son públicas.")
    print(f"✓ {len(rutas_publicas)} de {len(todas_rutas)} rutas son públicas.")
    if excluidas_fuentes or excluidas_rutas:
        print(f"  (excluidas por no estar aprobadas / ser documento-interno: {excluidas_fuentes} fuente(s), {excluidas_rutas} ruta(s) — esto es correcto, no un error)")


if __name__ == "__main__":
    build()