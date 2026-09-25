# 📚 Biblioteca de Contenidos - ONG Mecánica Social

Módulo interno de gestión del conocimiento y repositorio centralizado de contenidos de la **Escuela de Formación Política "Marcelo Orellana Lagos"**.

## 🏫 Biblioteca dentro de la Escuela
La Biblioteca ya no opera como un producto aislado. Su función exclusiva es actuar como la API de contenidos oficiales y marcos regulatorios que abastece a los componentes del ecosistema mediante el contrato formal unificado `site/catalogo.json`.

## 🗺️ Ecosistema Integrado

| Componente | Rol en el Ecosistema | Mecanismo de Consumo |
| :--- | :--- | :--- |
| **La Escuela** | Plataforma e Interfaz Principal | Llamadas asíncronas (`fetch`) al catálogo indexado. |
| **La Biblioteca** | Central de Conocimiento Validado | Compila fichas Markdown y genera el contrato JSON. |
| **Moodle** | Módulo de Aprendizaje Evaluativo | Consumirá el catálogo unificado en la Fase 2. |
| **IA Sandbox** | Clúster de Inteligencia Territorial | Consume los abstracts validados para emitir dictámenes. |
