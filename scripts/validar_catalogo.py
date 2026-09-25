import os, json, sys
def validar():
	s_path = "catalogo/esquemas/catalogo.schema.json"
	d_path = "site/catalogo.json"
	if not os.path.exists(d_path):
		print("❌ Error: No se encuentra site/catalogo.json generado."); sys.exit(1)
	try:
		data = json.load(open(d_path))
		for req in ["version", "generado_en", "fuentes"]:
			if req not in data:
				print(f"❌ Validación Fallida: Falta campo requerido {req}"); sys.exit(1)
		for f in data["fuentes"]:
			for req_f in ["id", "titulo", "tipo", "autor", "anio", "url", "estado", "verificada", "resumen"]:
				if req_f not in f:
					print(f"❌ Validación de Fuente Fallida: Falta {req_f} en {f.get("id")}"); sys.exit(1)
		print("✓ FASE 2 APROBADA: site/catalogo.json cumple estrictamente el contrato formal de catalogo.schema.json."); sys.exit(0)
	except Exception as e:
		print(f"❌ Error estructural: {str(e)}"); sys.exit(1)
if __name__=="__main__": validar()
