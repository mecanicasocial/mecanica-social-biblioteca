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
