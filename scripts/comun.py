import os
import re
import json

def parsear_lista(val):
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        val = val.strip()
        if val.startswith('[') and val.endswith(']'):
            elementos = val[1:-1].split(',')
            return [e.strip().strip('"').strip("'") for e in elementos if e.strip()]
    return [val] if val else []

def leer_ficha_markdown(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    partes = contenido.split('---')
    if len(partes) < 3:
        return None

    yaml_raw = partes[1].strip()
    cuerpo = '---'.join(partes[2:]).strip()

    datos = {}
    for linea in yaml_raw.split('\n'):
        if ':' in linea:
            k, v = linea.split(':', 1)
            clave = k.strip()
            valor = v.strip()

            if clave in ['rutas', 'modulos', 'etiquetas']:
                datos[clave] = parsear_lista(valor)
            else:
                datos[clave] = valor.strip('"').strip("'")

    datos['cuerpo'] = cuerpo
    return datos
