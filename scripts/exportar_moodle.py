import os
import json
import csv
import glob

def cargar_fichas_aprobadas(ruta_carpeta):
    fichas = []
    archivos = glob.glob(os.path.join(ruta_carpeta, "*.md"))
    
    for ruta in archivos:
        if os.path.basename(ruta).startswith("_"):
            continue
        ficha = {"archivo": os.path.basename(ruta)}
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                if ":" in linea and not linea.strip().startswith("#"):
                    partes = linea.split(":", 1)
                    clave = partes[0].strip().lower()
                    valor = partes[1].strip()
                    ficha[clave] = valor
        
        # BARRERA DE SEGURIDAD CENTRALIZADA: 
        # Únicamente se exporta lo aprobado y se vetan por completo los documentos internos
        estado = ficha.get("estado", "").lower()
        tipo = ficha.get("tipo", "").lower()
        
        if estado == "aprobado" and tipo != "documento-interno":
            fichas.append(ficha)
            
    return fichas

def exportar_a_moodle():
    print("================================================================")
    print("🔒 SANEANDO EXPORTADOR MOODLE: APLICANDO POLÍTICA DE PRIVACIDAD")
    print("================================================================")
    
    fuentes_seguras = cargar_fichas_aprobadas("catalogo/fuentes")
    
    # Asegurar la existencia del directorio de salida para moodle
    os.makedirs("moodle/export", exist_ok=True)
    ruta_csv = "moodle/export/fuentes.csv"
    
    # Escribir el archivo CSV final filtrado libre de borradores o planes estratégicos
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Título", "Tipo", "Estado", "Licencia"])
        
        for f in fuentes_seguras:
            writer.writerow([
                f.get("id", "S/I"),
                f.get("titulo", f.get("archivo")),
                f.get("tipo", "S/I"),
                f.get("estado", "S/I"),
                f.get("licencia", "S/I")
            ])
            print(f"📦 Indexado en CSV de clases: {f.get('titulo', f.get('archivo'))}")
            
    print(f"\n🎉 ¡Exportador Moodle alineado! Archivo guardado en: {ruta_csv}")
    print("================================================================")

if __name__ == "__main__":
    exportar_a_moodle()
