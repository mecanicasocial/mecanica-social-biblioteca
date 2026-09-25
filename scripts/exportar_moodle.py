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
