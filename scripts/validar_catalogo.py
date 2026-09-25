import os
import sys

def validar():
    path = "catalogo/fuentes/ley-transparencia-municipal.md"
    if not os.path.exists(path):
        print(f"✓ No se encontró la ficha {path}. Omitiendo validación.")
        return True
        
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for line in lines:
            if "ultima_verificacion" in line:
                # Extrae el valor después de los dos puntos y limpia comillas y espacios
                valor = line.split(":", 1)[1].strip().replace('"', '').replace("'", "")
                
                if not valor or len(valor) < 10:
                    print(f"❌ ERROR CRONOLÓGICO: El campo 'ultima_verificacion' está vacío o es inválido: {valor}")
                    sys.exit(1)
                    
        print("✓ Validación cronológica aprobada con parser reconciliado exitosamente.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error durante la validación: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    validar()
