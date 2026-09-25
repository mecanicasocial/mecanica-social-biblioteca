import os
import json
import datetime

def parse_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
        
    frontmatter_text = parts[1]
    body_text = parts[2].strip()
    
    data = {}
    for line in frontmatter_text.strip().split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            key = k.strip()
            val = v.strip().strip('"').strip("'")
            if key == 'anio':
                val = int(val)
            data[key] = val
            
    data['resumen'] = body_text
    return data

def build():
    fuentes_dir = "catalogo/fuentes"
    output_path = "site/catalogo.json"
    
    fuentes = []
    for filename in os.listdir(fuentes_dir):
        if filename.endswith('.md') and not filename.startswith('_'):
            filepath = os.path.join(fuentes_dir, filename)
            data = parse_frontmatter(filepath)
            if data:
                fuentes.append(data)
                
    catalogo = {
        "version": "1.0.0",
        "generado_en": datetime.datetime.now().isoformat(),
        "fuentes": fuentes
    }
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(catalogo, f, indent=2, ensure_ascii=False)
    print(f"✓ site/catalogo.json generado exitosamente con {len(fuentes)} fuentes.")

if __name__ == "__main__":
    build()
