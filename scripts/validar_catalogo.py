"""Valida fichas de fuentes y rutas. Termina con error si hay problemas."""
import sys
from comun import RAIZ, ESTADOS, TIPOS, LICENCIAS, CURSOS_ESCUELA, cargar

errores = []
rutas = cargar("rutas")
ids_ruta = {r.get("id") for r in rutas}
carpetas_escuela = set()
for r in rutas:
    carpetas_escuela.update(r.get("modulos", []))

todos = [m for r in rutas for m in r.get("modulos", [])]
for c in CURSOS_ESCUELA:
    n = todos.count(c)
    if n != 1:
        errores.append(f"rutas: el curso '{c}' aparece {n} veces (debe estar en exactamente una ruta)")
for m in set(todos) - set(CURSOS_ESCUELA):
    errores.append(f"rutas: módulo desconocido '{m}'")

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
