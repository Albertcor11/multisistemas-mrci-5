# Registro de integración · octubre de 2026

Origen: skill `mrci-5-investigacion-juridica-editorial`, derivada de esta integradora. Se incorporó una selección revisada de sus mejoras; las demás diferencias se descartaron por ser propias de esa distribución recortada. Fecha: 24 de octubre de 2026.

El corpus se reempaquetó y `references/inventario.json` registra las huellas nuevas (clave `actualizacion.integracion_2026_10`). Verificar con `python scripts/abrir_corpus.py --verificar`.

## Decisiones del responsable

- Manual APA: se conserva el PDF escaneado y se añade su transcripción OCR para búsqueda textual; se mantiene la referencia a la cuarta edición en español y el ejemplo original del catálogo.
- Tablas Word: rige la política 1.6.0 de bandas alternas `#EAF4FB`/`#FFFFFF`, ahora implementada en el motor y en su auditoría.
- Biblioteca autoral JAPR: se conserva la descripción completa.
- Regla general: ningún entregable menciona la metodología, los módulos ni los motores internos (SKILL.md, «Calidad de entrega»).

## Cambios incorporados

| Tipo | Archivos | Cambio |
|---|---|---|
| MODIFICADO | `00-protocolo-realidad-fuentes.md` en 16 módulos | Autoría real, búsqueda y pertinencia geográfica, autores clásicos, saturación, fuentes oficiales y capas en matrices. |
| MODIFICADO | `05-marco-juridico-transversal-mexico.md` en 11 módulos | Control terminológico: tesis aislada no es jurisprudencia (Ley de Amparo). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/controles-auditoria-apa.md` | Nueva fila: localizador de paráfrasis en obra paginada (8.23, 8.25, 8.28). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/opciones-escritura.md` | Corrige enlace roto al catálogo OPCIONES_ESCRITURA.json. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/produccion-revision-entrega.md` | Nueva sección «Dos capas»: entregable vs. expediente de control; corrige enlace roto. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/REGLAS_DE_EDICION_Y_PERFIL_AUTORAL_JAPR.md` | Tablas con bandas 1.6.0, léxico de 42 entradas sin cifra fija y enlaces corregidos. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/02_protocolos_tesis/README.md` | Remite a la estructura detallada y a la regla Bloom/espejo. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/02_protocolos_tesis/catalogos/PERFILES_TESIS.json` | 9 controles nuevos: problema con fuentes, espejo-Bloom, capas doctrina/normativa, método sin subtítulos, cronograma, aportación verificable. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/04_perfil_autoral_japr/REGLAS_DE_EDICION_Y_PERFIL_AUTORAL_JAPR.md` | Tablas con bandas 1.6.0, léxico de 42 entradas y enlace corregido. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/04_perfil_autoral_japr/catalogos/LEXICO_CONTROL_IA.csv` | LEX-031 a LEX-042: metatexto del sistema vetado y «jurisprudencia consolidada» a revisión. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/04_perfil_autoral_japr/pruebas/test_motor_perfil_autoral.py` | Dos pruebas de regresión: metatexto del sistema y «jurisprudencia consolidada». |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/05_formato_word_mrci/catalogos/PERFIL_FORMATO_WORD_MRCI.json` | Versión 1.6.0: bloque «referencias» y tablas con bandas alternas. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/05_formato_word_mrci/pruebas/test_motor_formato_word.py` | Tres pruebas de referencias (cursivas, aprobación, párrafo vacío). Además, cuatro pruebas nuevas de bandas y ajuste de la prueba de relleno (integración propia). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/05_formato_word_mrci/scripts/motor_formato_word.py` | Título y entradas de Referencias con cursivas reales y audit_references(). Además, bandas alternas #EAF4FB/#FFFFFF programadas en configure_table() y verificadas por audit_tables() (integración propia). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/06_aparato_juridico_mrci/scripts/motor_aparato_juridico.py` | Compuerta JUR-09_CATEGORIA_CON_RESPALDO y regla_categoria. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/07_libros_narrativa/README.md` | Corrige enlace roto a libros-narrativa.md. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/08_produccion_entrega/README.md`<br>`modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/09_desarrollo_editorial/README.md` | Corrige enlace roto a la operación y entrega. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/editorial-academico-cientifico-mrci/references/controles-auditoria-apa.md` | Misma fila de localizador de paráfrasis (copia vendor). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/editorial-academico-cientifico-mrci/references/opciones-escritura.md`<br>`modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/editorial-academico-cientifico-mrci/references/produccion-revision-entrega.md` | Corrige enlace roto (copia vendor). |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/suite-juridico-fiscal-cumplimiento/MODULO.md` | Fundamento sólo en fuente oficial con localizador y fecha de consulta. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/suite-juridico-fiscal-cumplimiento/references/controls.md` | Prohíbe blogs, despachos y portales como fundamento; PENDIENTE DE VERIFICACIÓN. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/skills/suite-juridico-fiscal-cumplimiento/references/entregables-y-aprobacion.md` | El entregable no menciona metodología interna; búsqueda directa antes de entregar. |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/references/figuras-apa-mexico.md` | Guía nueva: figuras, numeración y notas (APA cap. 7). |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/references/lenguaje-libre-de-sesgo.md` | Guía nueva: lenguaje libre de sesgo (APA cap. 5). |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/references/proceso-de-publicacion.md` | Guía nueva: proceso de publicación en revista (APA cap. 12). |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/02_protocolos_tesis/catalogos/ESTRUCTURA_DETALLADA_APARTADOS.md` | Catálogo nuevo: orden de apartados de proyecto y tesis, dos capas, fechas, títulos. |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/02_protocolos_tesis/catalogos/REGLA_OBJETIVOS_BLOOM_Y_ESPEJO.md` | Catálogo nuevo: prueba de espejo y niveles de Bloom. |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/05_formato_word_mrci/README.md` | README nuevo del motor Word. |
| NUEVO | `modulos/editorial-academico-cientifico-mrci/assets/sistema-apa-mexico/Manual_APA_4_Mexico_2021_Texto.md` | Transcripción OCR del manual para búsqueda textual; el PDF escaneado se conserva. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/MODULO.md` | Orden de apartados, Marco metodológico sin subtítulos, Bloom/espejo, cronograma de la tesis pendiente, tres auditorías obligatorias, audit_text() como condición de entrega, tablas con bandas 1.6.0, JUR-09. Se conservan el PDF del manual y la «cuarta edición»; se añade el OCR. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/apa-mrci-mexico.md` | Modelos jurídicos mexicanos 30 a 33, Constitución, tratados, iniciativas, abreviaturas oficiales, lista única, regla de ordenamiento en fracciones aisladas y enlaces a las 3 guías nuevas. Se conserva la ficha del ejemplar y la referencia base. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/sistema-edicion-citas-apa-referencias.md` | Localizador de paráfrasis, lista de referencias única con IDs jurídicos y conteos 570/466. Se conserva la mención de la cuarta edición. |
| MODIFICADO | `modulos/editorial-academico-cientifico-mrci/references/sistema-apa-mexico-catalogo.json` | Reglas nuevas 9.44-02, 11.4-01, 11.5-01, 11.6-01, 11.9-01; instrucciones 570, sin modelo 466. Ejemplo APA original conservado. |
| MODIFICADO | `references/sistema-apa-mexico-catalogo.json`<br>`references/controles-auditoria-apa.md` | Sincronizado con EDI-01. |
| MODIFICADO | `references/apa-mrci-mexico.md` | Sincronizado con EDI-01; las 3 guías nuevas se citan como rutas de EDI-01. |
| MODIFICADO | `references/sistema-edicion-citas-apa-referencias.md` | Mismas reglas nuevas y conteos que EDI-01. |
| MODIFICADO | `SKILL.md` | Regla de entregables sin metodología interna, OCR del manual, protocolos y tesis, tres auditorías y este registro. |

## Diferencias no incorporadas

- Cambios de texto `SKILL.md` → `MODULO.md` dentro de los originales: la integradora ya resuelve esa equivalencia sin alterarlos.
- Restricciones de alcance a cinco áreas (SKILL.md, mapa, alcance y dependencias, índice de biblioteca simplificado, guía jurídico-fiscal propia): limitarían los otros módulos.
- Sustitución del `MODULO.md` duplicado en `vendor/` por un puntero, cambio de enlace en `fuentes-citas-integridad.md` (el original funciona aquí) y archivos propios de esa distribución (`procedencia.json`, `inventario-paquete.json`, `verificar_paquete.py`, `libs/`, `requirements.txt`, `.pytest_cache`).
- Dos enlaces corregidos en guías de PRE-02: el paquete PRE-02 se verifica contra su ZIP original sellado; modificarlo rompería esa verificación.

## Límites conocidos

- Las copias editoriales internas de FIL-01 (`pensamiento-filosofico-aplicado/vendor/`) conservan su versión anterior; sólo recibieron los cambios de biblioteca 00 y 05.
- Las pruebas de los motores 03, 08 y 10 de EDI-01 ya fallaban antes de esta integración por archivos o módulos ausentes en el paquete; no se modificaron.
