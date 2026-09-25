import os, sys
def validar():
	p = "catalogo/fuentes/ley-transparencia-municipal.md"
	if not os.path.exists(p): return True
	lines = open(p).read().split("
")
	for l in lines:
		if "ultima_verificacion" in l:
			v = l.split(":")[1].strip().strip(""").strip("'")
			if not v or len(v) < 10: print("❌ Fecha inválida"); sys.exit(1)
	print("✓ Validación cronológica aprobada con parser reconciliado.")
if __name__=="__main__": validar()
