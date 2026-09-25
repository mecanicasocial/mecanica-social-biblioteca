# 🗺️ Modelo de Arquitectura Integrada — Mecánica Social

El flujo de información de la ONG se rige bajo un modelo de plataforma unificada donde la verdad de los datos de contenido reside en la Biblioteca:

1. **Ficha Fuente (Markdown):** Contiene metadatos estructurados en Frontmatter y abstract analítico en el cuerpo.
2. **Validador Contractual (Python):** Audita la vigencia cronológica y el cumplimiento estricto de `catalogo.schema.json`.
3. **Catálogo de Producción (JSON):** Endpoint público consumido dinámicamente por la Escuela y el Sandbox de IA.
