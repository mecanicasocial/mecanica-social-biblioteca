import os
import csv
import glob

from _comunes import parse_frontmatter, es_fuente_publicable


def cargar_fichas_aprobadas(ruta_carpeta):
    fichas = []
    for ruta in sorted(glob.glob(os.path.join(ruta_carpeta, "*.md"))):
        if os.path.basename(ruta).startswith("_"):
            continue
        ficha = parse_frontmatter(ruta)
        if ficha and es_fuente_publicable(ficha):
            fichas.append(ficha)
    return fichas


def exportar_a_moodle():
    print("================================================================")
    print("🔒 EXPORTADOR MOODLE: usando la barrera de seguridad centralizada")
    print("   (scripts/_comunes.py::es_fuente_publicable — la misma que usa")
    print("    construir_indice.py, para que ambos nunca vuelvan a divergir)")
    print("================================================================")

    fuentes_seguras = cargar_fichas_aprobadas("catalogo/fuentes")

    os.makedirs("moodle/export", exist_ok=True)
    ruta_csv = "moodle/export/fuentes.csv"

    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Título", "Tipo", "Estado", "Licencia"])

        for f in fuentes_seguras:
            writer.writerow([
                f.get("id", "S/I"),
                f.get("titulo", "S/I"),
                f.get("tipo", "S/I"),
                f.get("estado", "S/I"),
                f.get("licencia", "S/I"),
            ])
            print(f"📦 Indexado en CSV de clases: {f.get('titulo')}")

    print(f"\n🎉 Exportador Moodle: {len(fuentes_seguras)} fuente(s) exportada(s) en {ruta_csv}")
    print("================================================================")


if __name__ == "__main__":
    exportar_a_moodle()