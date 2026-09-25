import os
import json
import glob

def cargar_fichas(ruta_carpeta):
    fichas = []
    # Buscar todas las fichas Markdown en la carpeta especificada
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
        fichas.append(ficha)
    return fichas

def construir_indice_gobernado():
    print("================================================================")
    print("🔒 CONFIGURANDO BARRERA DE SEGURIDAD EN GITHUB PAGES (AUDITORÍA)")
    print("================================================================")
    
    # Cargar las fuentes del catálogo en disco
    todas_las_fuentes = cargar_fichas("catalogo/fuentes")
    
    # APLICACIÓN DE LAS REGLAS CRÍTICAS DEL AUDITOR:
    # - Solo se publica lo que esté en estado 'aprobado'
    # - NUNCA se publican de forma automática los 'documento-interno'
    fuentes_publicables = []
    for f in todas_las_fuentes:
        estado = f.get("estado", "").lower()
        tipo = f.get("tipo", "").lower()
        titulo = f.get("titulo", f.get("archivo"))
        
        if estado == "aprobado" and tipo != "documento-interno":
            fuentes_publicables.append(f)
            print(f"✅ AUTORIZADO PARA PUBLICACIÓN E IA: {titulo}")
        else:
            print(f"🚫 BLOQUEADO POR GOBERNANZA DE PRIVACIDAD: {titulo} (Estado: {estado} | Tipo: {tipo})")

    # Cargar rutas de forma simétrica aplicando la misma restricción
    todas_las_rutas = cargar_fichas("rutas")
    rutas_publicables = [r for r in todas_las_rutas if r.get("estado", "").lower() == "aprobado"]

    # Estructurar el artefacto site/catalogo.json libre de filtraciones
    os.makedirs("site", exist_ok=True)
    indice_limpio = {
        "fuentes": fuentes_publicables,
        "rutas": rutas_publicables,
        "auditoria_estado": "Saneado - Con Barrera de Seguridad"
    }
    
    with open("site/catalogo.json", "w", encoding="utf-8") as out:
        json.dump(indice_limpio, out, indent=4, ensure_ascii=False)
        
    print("\n🎉 ¡Artefacto público site/catalogo.json resguardado con éxito!")
    print("================================================================")

if __name__ == "__main__":
    construir_indice_gobernado()
