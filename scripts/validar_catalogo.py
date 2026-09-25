import os
import glob
import sys

def cargar_todas_las_fichas(ruta_carpeta):
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
        fichas.append(ficha)
    return fichas

def ejecutar_auditoria_licencias():
    print("================================================================")
    print("🔍 VALIDACIÓN DE REGLAS DE NEGOCIO E INTELLECTUAL PROPERTY (IP)")
    print("================================================================")
    
    fuentes = cargar_todas_las_fichas("catalogo/fuentes")
    errores = 0
    
    for f in fuentes:
        titulo = f.get("titulo", f.get("archivo"))
        estado = f.get("estado", "").lower()
        licencia = f.get("licencia", "").lower()
        
        # REGLA DE GOBERNANZA #4 EXIGIDA POR EL AUDITOR:
        # Si una fuente está 'aprobada', NO puede tener una licencia 'por-definir' o estar vacía.
        if estado == "aprobado":
            if not licencia or licencia == "por-definir":
                print(f"❌ ERROR CRÍTICO: La fuente [{titulo}] está APROBADA pero su licencia es '{licencia}'.")
                print("   Cambio rechazado por riesgo legal de propiedad intelectual.")
                errores += 1
            else:
                print(f"✅ Fuente aprobada con licencia válida: [{titulo}] -> ({licencia})")
        else:
            print(f"➖ Fuente en revisión: [{titulo}] (Estado: {estado} | Licencia: {licencia})")
            
    print("================================================================")
    if errores > 0:
        print(f"🚨 VALIDACIÓN FALLIDA: Se encontraron {errores} infracciones de gobernanza legal.")
        return False
    else:
        print("🎉 ¡TODAS LAS LICENCIAS CUMPLEN CON EL ESTÁNDAR INSTITUCIONAL!")
        return True

if __name__ == "__main__":
    exito = ejecutar_auditoria_licencias()
    if not exito:
        # Salida controlada para que el CI/CD de GitHub Actions bloquee el despliegue si hay errores
        sys.exit(1)
