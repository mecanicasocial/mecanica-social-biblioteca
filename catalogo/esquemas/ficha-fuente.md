# 📋 Especificación de Metadatos de Fuentes (Ficha Fuente)
---
id: [string, formato slug único, ej: ley-transparencia-2026]
titulo: [string]
tipo: [enum: libro, articulo, ley, documento-oficial]
autor: [string]
anio: [integer]
url: [string]
estado: [enum: borrador, aprobado, rechazado]
verificada: [enum: si, no]
ultima_verificacion: [string, formato YYYY-MM-DD]
proxima_revision: [string, formato YYYY-MM-DD]
---
El cuerpo de este archivo Markdown debe contener única y exclusivamente el resumen estratégico o abstract analítico de la fuente, el cual será consumido por el clúster de IA.
