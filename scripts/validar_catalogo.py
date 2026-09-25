import os
import glob
import sys
import re

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

def ejecutar_auditoria_temporal():
    print("================================================================")
    print("⏳ AUDITORÍA CRONOLÓGICA: OPERACIONALIZACIÓN DE VIGENCIA")
    print("================================================================")
    
    fuentes = cargar_todas_las_fichas("catalogo/fuentes")
    errores = 0
    # Expresión regular estricta para validar formato de fecha ISO AAAA-MM-DD
    formato_fecha = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    
    for f in fuentes:
        titulo = f.get("titulo", f.get("archivo"))
        estado = f.get("estado", "").lower()
        u_verif = f.get("ultima_verificacion", "")
        p_revis = f.get("proxima_revision", "")
        
        # REGLA DE GOBERNANZA #5 EXIGIDA POR EL AUDITOR:
        # Las fuentes 'aprobadas' deben registrar obligatoriamente sus metadatos de vigencia en formato ISO
        if estado == "aprobado":
            if not u_verif or not formato_fecha.match(u_verif):
                print(f"❌ ERROR TEMPORAL: [{titulo}] aprobado tiene 'ultima_verificacion' inválida o vacía ('{u_verif}').")
                errores += 1
            elif not p_revis or not formato_fecha.match(p_revis):
                print(f"❌ ERROR TEMPORAL: [{titulo}] aprobado tiene 'proxima_revision' inválida o vacía ('{p_revis}').")
                errores += 1
            else:
                print(f"📆 Vigencia controlada: [{titulo}] (Verificado: {u_verif} | Próxima Revisión: {p_revis})")
        else:
            print(f"➖ En espera cronológica: [{titulo}] (Estado: {estado})")
            
    print("================================================================")
    if errores > 0:
        print(f"🚨 VALIDACIÓN FALLIDA: Se encontraron {errores} fuentes sin control de vigencia activa.")
        return False
    else:
        print("🎉 ¡TODOS LOS RECURSOS REGISTRAN SU CONTROL TEMPORAL CORRECTAMENTE!")
        return True

if __name__ == "__main__":
    exito = ejecutar_auditoria_temporal()
    if not exito:
        sys.exit(1)
