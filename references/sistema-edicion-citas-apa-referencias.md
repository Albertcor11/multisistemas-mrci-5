# Sistema de edición de citas APA y referencias

## Función y alcance

Editar y revisar las citas dentro del texto y las referencias completas de trabajos en español destinados a México. Aplicar el perfil APA MRCI México, basado en la cuarta edición en español del manual publicado por Editorial El Manual Moderno en 2021. No confundir esa edición mexicana con la cuarta edición histórica en inglés.

Conservar la jerarquía: instrucciones actuales de la persona, requisitos auténticos de la institución destinataria y manual aplicable. Usar los ejemplos como modelos de estructura y presentación, sujetos a cotejo con el pasaje normativo cuando exista duda. No convertir una aplicación editorial previa en autoridad normativa independiente.

## Recursos incorporados

Los enlaces de Word y Excel siguientes corresponden al módulo EDI-01 recuperado mediante `scripts/abrir_corpus.py --modulo EDI-01`, no a la raíz de esta skill. El manual completo se encuentra en ese módulo bajo `assets/sistema-apa-mexico/Manual_APA_4_Mexico_2021.pdf`.

| Recurso | Uso |
| --- | --- |
| `assets/sistema-apa-mexico/Modelos_APA_4_Mexico_citas_y_referencias.docx` en EDI-01 | Comparar la presentación real de 30 modelos de citas y 21 referencias, incluidas cursivas, puntuación y sangrías. |
| `assets/sistema-apa-mexico/Tabla_APA_4_Mexico_variantes_de_tesis_verificables.xlsx` en EDI-01 | Consultar 565 instrucciones, variantes, localizadores del manual, cotejos y referencias finales. |
| [sistema-apa-mexico-catalogo.json](sistema-apa-mexico-catalogo.json) | Buscar reglas, modelos y fuentes sin abrir todo el Excel; recuperar hashes y versiones de los dos documentos incorporados. |
| [apa-mrci-mexico.md](apa-mrci-mexico.md) | Aplicar el perfil normativo general y la jerarquía de decisión. |

Interpretar las hojas del Excel: «Reglas México» organiza instrucciones y variantes; «Modelos de citas» separa formas narrativa y parentética; «Cotejo de publicaciones» conserva los datos y las correcciones de las fuentes originales; «Cobertura del manual» identifica alcance y pendientes; «Referencias finales» reúne las entradas bibliográficas completas.

Buscar en el catálogo mediante `rg -n` con el ID de regla, de modelo o de fuente, apellido, tipo de publicación o palabra de la instrucción. Usar `rows` para reglas y modelos asociados, `cases` para citas y referencias de ejemplo, `sources` para la publicación y su evidencia, y `provenance` para la tesis donde se localizó. No interpretar estos códigos de trabajo como partes de una cita APA.

## Alcance comprobado del corpus

Conservar el estado de corpus parcial: 570 instrucciones en el catálogo JSON (las 565 de la tabla Excel y 5 reglas jurídicas y de lista única añadidas en octubre de 2026), 104 con modelos de esta selección y 466 pendientes de ejemplo; 30 modelos de cita y 21 referencias de publicaciones, 51 modelos en conjunto. Usar de una a diez columnas de variantes verificadas según el bloque de la matriz. No afirmar que diez sea un máximo normativo ni que se hayan agotado todas las variantes posibles.

No inventar ejemplos para cerrar las reglas pendientes. Si el caso solicitado no está representado, localizar el apartado específico del manual y una publicación original que permita construir y verificar un modelo. Identificar ese modelo como nuevo y registrar su evidencia antes de incorporarlo.

## Flujo de edición

1. Registrar destino mexicano, edición aplicable y requisito institucional cuando exista. Conservar las preferencias ya fijadas; no volver a preguntar la edición si el contexto la determina.
2. Extraer las citas del manuscrito y su lista final. Distinguir paráfrasis, cita textual breve, cita en bloque, fuente secundaria y las excepciones que no generan una referencia recuperable.
3. Identificar la publicación realmente utilizada: libro, capítulo, artículo, reporte, comunicado, entrada de diccionario u otra categoría. Mantener esa categoría aunque el archivo sea PDF o se descargue desde una página web.
4. Abrir la publicación original y cotejar autoría, fecha, título, versión o edición, datos de la fuente, DOI o URL y localizador necesario. Usar la tesis como pista de búsqueda; no copiar sus errores ni citarla en lugar de la obra consultada. Citar una tesis únicamente cuando la tesis misma sea el objeto utilizado.
5. Seleccionar la regla y la variante que coincidan con el caso. No considerar un título distinto como variante si conserva exactamente la misma estructura. Consultar el Word para la presentación y el Excel para la evidencia y los vínculos entre reglas y modelos.
6. Construir la cita narrativa o parentética dentro del texto y la referencia completa al final. Sustituir los datos del ejemplo por los datos comprobados de la fuente utilizada; no trasladar afirmaciones, páginas o fechas de otra publicación.
7. Revisar autoría, fecha, localizador, signos, cursivas, sangrías, orden alfabético, ambigüedades y letras del año. Conservar correspondencia en ambos sentidos entre citas y referencias, aplicando las excepciones del manual.
8. Comparar la salida renderizada con los modelos de Word. Entregar la corrección con explicación breve de cambios sustantivos y pendientes reales. No declarar conformidad total cuando una fuente o regla decisiva siga sin verificarse.

## Citas y referencias

Mantener las citas en el cuerpo del trabajo. Colocar al final, en «Referencias», las entradas completas de las publicaciones utilizadas. No intercalar entradas bibliográficas completas en la prosa por confundirlas con citas autor-fecha.

Seleccionar forma narrativa o parentética según la oración. Conservar las comillas de la cita breve y el bloque sin comillas para las citas de 40 palabras o más. Usar un localizador verificable; distinguir la página impresa de la posición del archivo PDF. No inventar página cuando la fuente carezca de paginación.

En la paráfrasis, el número de página o párrafo es opcional (apartado 8.23) y, cuando se incluya, debe ser un número real de página o párrafo, nunca el nombre de una sección (por ejemplo, «resumen e introducción»); esa forma de localizador sólo es válida para obras sin numeración de páginas (apartado 8.28). En la cita directa, el número de página es obligatorio (apartado 8.25). Si la idea citada corresponde al argumento general de toda la obra y no a un pasaje puntual, omitir el localizador en vez de inventar uno aproximado o describir una sección.

Identificar expresamente una cita secundaria y referenciar la fuente efectivamente consultada. Conservar las excepciones normativas, como comunicaciones personales no recuperables; no completar mecánicamente la lista con una referencia ficticia.

Ordenar las referencias alfabéticamente y aplicar doble espacio y sangría francesa de 1.27 cm. Conservar cursivas nativas en Word, apellidos completos, fechas, edición, volumen, número, páginas o eLocalizador y DOI o URL según corresponda. No añadir un punto a un DOI o URL. Mantener las fechas de recuperación únicamente cuando procedan.

No subdividir la lista final en subtítulos por categoría de fuente (por ejemplo «Literatura académica», «Fuentes jurídicas» o «Criterios jurisdiccionales»); intercalar doctrina, leyes, jurisprudencia y tratados en una sola secuencia alfabética, alfabetizando por título o denominación oficial cuando la fuente carezca de autor personal. Para los modelos de referencia jurídica mexicana (precedentes con registro, códigos, leyes, Constitución y tratados) y sus abreviaturas oficiales, aplicar [Fuentes jurídicas mexicanas](apa-mrci-mexico.md#fuentes-jurídicas-mexicanas-sistema-dual-mrci) y los IDs `9.44-02`, `11.4-01`, `11.5-01`, `11.6-01`, `11.9-01`, `11.10-01` y `11.11-01` a `11.11-05` del catálogo.

El Excel presenta los ejemplos como texto; usar el Word para corroborar cursivas y sangrías. No trasladar colores, códigos de modelo ni columnas de evidencia a las citas o a las referencias del manuscrito.

## Presentación profesional

Escribir «apartado» o «apartados del manual» y conservar su numeración. Evitar símbolos decorativos, emojis, separadores gráficos y marcas visibles de Markdown en documentos finales. No usar asteriscos como sustitutos de cursivas nativas.

Conservar los signos que formen parte de la puntuación APA, del contenido literal, de una denominación, de un identificador o de una dirección electrónica. No eliminar el signo de unión de autores en una cita parentética, los paréntesis, los corchetes necesarios, los guiones de un apellido o las marcas de omisión normativamente justificadas por tratarlos como adornos.

Aplicar el formato APA de citas en bloque y referencias aunque el perfil general de Word emplee otros espaciados, alineaciones o separadores. Conservar las zonas protegidas de las citas literales y los datos bibliográficos frente a preferencias de prosa o humanización.

## Auditor hostil y condición de entrega

Aplicar una revisión adversarial obligatoria antes de entregar cualquier trabajo académico: protocolo, tesina, tesis, artículo, ensayo, capítulo, libro académico o material docente académico. Buscar activamente errores, omisiones, atribuciones engañosas, referencias incongruentes y supuestas verificaciones sin evidencia. No presumir corrección porque el redactor haya usado esta skill o porque el trabajo se parezca visualmente a un ejemplo.

Revisar todos los renglones de la versión final renderizada, página por página. Incluir portada y elementos preliminares, cuerpo, tablas, figuras y sus notas, notas al pie, bibliografía o referencias, anexos y elementos finales. Registrar la identificación de cada página y renglón efectivamente revisado; una búsqueda de patrones o un conteo automático no sustituyen la lectura del contenido. Auditar cada archivo del paquete académico en su versión final.

Para cada cita, comprobar su modalidad, autoría, fecha, localizador cuando proceda, literalidad o fidelidad de la paráfrasis, signos, cursivas y fuente que sostiene la proposición. Vincular el modelo de comparación y la regla del manual. Para cada referencia, cotejar la entrada completa con la publicación original, su categoría, correspondencia con el cuerpo y presentación final. No autorizar una referencia por la sola coincidencia de autor y año.

Si no existe un ejemplo aplicable en el corpus, verificar el apartado del manual y construir un modelo sustentado en una publicación original; incorporarlo al expediente de auditoría antes de cerrar ese control. No equiparar las 104 reglas con modelos a cobertura de todas las reglas. No exigir aplicar las 570 instrucciones cuando no correspondan al trabajo, pero justificar toda declaración de no aplicabilidad.

Conservar un registro de auditoría con estos campos:

| Registro | Evidencia exigida |
| --- | --- |
| Versión auditada | Nombre, versión y SHA-256 de cada archivo de entrega y de su render utilizado. |
| Cobertura de lectura | Identificadores de todas las páginas y renglones, evidencia revisada, estado y observación; incluir anexos y notas. |
| Citas revisadas | Ubicación, texto, fuente original, localizador, regla, modelo comparable y decisión. |
| Referencias revisadas | Entrada completa, datos cotejados, uso en el cuerpo, formato y decisión. |
| Controles aplicables | Total previsto, revisado y aprobado; motivo de cada excepción o no aplicabilidad. |
| Hallazgos | Error, ubicación, corrección, evidencia de la corrección y nueva revisión. |
| Dictamen | Estado de cierre, responsable real de la revisión, fecha y alcance. |

Calcular por separado la cobertura de renglones, de citas, de referencias y de controles aplicables. Exigir cien por ciento de revisión y aprobación en cada conjunto aplicable, cero errores abiertos, cero pendientes de verificación y ninguna excepción sin justificar. Para conjuntos sin elementos, registrar «No aplica» y su motivo; no inventar citas ni referencias para obtener un porcentaje. No promediar dimensiones para ocultar una categoría incompleta.

Usar `ENTREGA_BLOQUEADA` mientras falte evidencia, revisión, corrección o cotejo. Mantener abierto el control ante cualquier incertidumbre material. Usar `VALIDADO_PARA_ENTREGA_ACADEMICA` sólo cuando todos los controles anteriores estén cerrados y las demás condiciones editoriales del encargo estén cumplidas. Conservar los borradores internamente mientras exista un bloqueo, salvo solicitud expresa posterior de una entrega provisional identificada como no validada.

Después de corregir, volver a revisar el pasaje y sus dependencias; si cambia el archivo o su paginación, actualizar las huellas y revisar de nuevo los renglones de la versión resultante, sin reutilizar un dictamen de un archivo distinto. Emitir el resultado de entrega junto con un dictamen breve que identifique la versión, el alcance revisado y el cierre de hallazgos. No prometer infalibilidad: el cien por ciento describe la cobertura y aprobación documentadas de los controles aplicables, no una certeza absoluta de verdad ni la aprobación de una universidad o revista.

## Trazabilidad y mantenimiento

Registrar por corrección: ubicación en el manuscrito, texto anterior, texto corregido, regla aplicable, modelo de comparación, fuente original, localizador y estado de verificación. Distinguir comprobación de metadatos, lectura del pasaje y comprobación tipográfica; ninguna sustituye a las demás.

Conservar ambos documentos dentro de la skill y verificar sus hashes contra `archivos` del catálogo al actualizar. Evitar dependencias de rutas temporales o de esta conversación. Mantener la misma versión de Word, Excel y catálogo cuando cambie su contenido; registrar qué reglas siguen pendientes. No convertir los modelos en supuesta certificación institucional o jurídica.
