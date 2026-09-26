# Campos de una ficha de fuente

Versión legible de [`catalogo.schema.json`](./catalogo.schema.json). Si cambias un campo
aquí, cámbialo también en el schema, en `catalogo/fuentes/_plantilla.md` y en
`scripts/_comunes.py` — los cuatro deben decir siempre lo mismo. No vuelvas a reescribir
uno de estos archivos por separado: es exactamente lo que causó la última reconciliación.

| Campo | Obligatorio | Valores |
|---|---|---|
| id | sí | `fuente-0001`, único, incremental de 4 dígitos |
| titulo | sí | texto |
| autor | sí | texto |
| anio | sí | número |
| tipo | sí | libro, articulo, informe, normativa, documento-interno, material-pedagogico, sitio-web, video, visual |
| url | no | dirección pública |
| licencia | sí | por-definir, cc-by, dominio-publico, con-permiso, todos-los-derechos |
| estado | sí | borrador, prueba, aprobado, restringido, obsoleto, suspendido, retirado |
| verificada | sí | si / no |
| revisor | sí | nombre o `pendiente` |
| asistencia_ia | no | si / no |
| ultima_verificacion | **sí, solo si `estado: aprobado`** | fecha ISO `AAAA-MM-DD` |
| proxima_revision | **sí, solo si `estado: aprobado`** | fecha ISO `AAAA-MM-DD` |
| rutas | no | lista de ids de ruta, ej. `[ruta-04]` |
| modulos | no | lista de slugs de carpeta de curso de la Escuela, ej. `[11-diseno-proyectos]` |
| etiquetas | no | lista |

`resumen` **no** es un campo del frontmatter: es el texto libre debajo del segundo `---`.

## Regla de publicación (barrera de seguridad)

Solo llegan a `site/catalogo.json` las fuentes con `estado: aprobado` y `tipo` distinto de
`documento-interno`. Esta regla vive en **un solo lugar**: `scripts/_comunes.py::es_fuente_publicable`.
Tanto `construir_indice.py` como `exportar_moodle.py` importan esa función — ninguno de los
dos implementa su propia copia de la regla. Si algún día hay que cambiarla, se cambia ahí y
solo ahí.

## Un `tipo` para leyes y normativas

Usa siempre `normativa`, no `ley` ni `documento-oficial` — ambos existieron brevemente en una
versión anterior del esquema y se descartaron para no tener dos palabras para lo mismo.
