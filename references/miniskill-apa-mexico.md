# Mini-Skill APA-MX · Citación APA México y Auditoría Académica

Esta ficha se carga bajo demanda para cualquier producto académico, científico, libro, artículo, protocolo o tesis, activando de forma conjunta el rector editorial `EDI-01` y los controles de citación **APA MRCI México (4.ª edición en español)**, incluso cuando la materia de fondo corresponda a otro módulo especialista.

## 1. Rutas de entrada y activación

- **Guía operativa de citas y referencias:** [sistema-edicion-citas-apa-referencias.md](sistema-edicion-citas-apa-referencias.md)
- **Perfil editorial APA México:** [apa-mrci-mexico.md](apa-mrci-mexico.md)
- **Controles de auditoría APA:** [controles-auditoria-apa.md](controles-auditoria-apa.md)
- **Catálogo normativo JSON:** [sistema-apa-mexico-catalogo.json](sistema-apa-mexico-catalogo.json)
- **Activación del módulo editorial completo (`EDI-01`):**
  ```bash
  python3 scripts/orquestador.py activar EDI-01 APA-MX
  ```
  *(O mediante `python3 scripts/abrir_corpus.py --modulo EDI-01`, resolviendo las rutas internas desde la carpeta devuelta).*

## 2. Reglas de citación y verificación de fuentes

1. **Integridad de citas y lista única de referencias:**
   - Conservar todas las citas en el texto y las referencias completas al final en una lista única.
   - Identificar y leer las publicaciones originales; las tesis sólo sirven como pista de búsqueda bibliográfica, salvo que el objeto citado sea la tesis misma.
   - En paráfrasis de obras paginadas, incluir siempre el localizador específico conforme a las reglas `8.23`, `8.25` y `8.28`.
2. **Uso del Manual APA 4.ª ed. en español (Manual Moderno 2021):**
   - Mantener el corpus de ejemplos como parcial y aplicar las reglas específicas del manual a los casos no representados en los ejemplos.
   - Para localizar un apartado del manual por texto, consultar su transcripción OCR dentro de `EDI-01` (`modulos/editorial-academico-cientifico-mrci/assets/sistema-apa-mexico/Manual_APA_4_Mexico_2021_Texto.md`) y cotejar la página escaneada del PDF original ante cualquier duda.

## 3. Protocolos, tesis y tres auditorías obligatorias

1. **Protocolos y tesis (`02_protocolos_tesis`):**
   - Aplicar la estructura detallada de apartados (`ESTRUCTURA_DETALLADA_APARTADOS.md`) y la regla de objetivos **Bloom-espejo** (`REGLA_OBJETIVOS_BLOOM_Y_ESPEJO.md`) incluidas en el motor `02_protocolos_tesis` de `EDI-01`.
   - Mantener el Marco metodológico en prosa continua sin subtítulos internos cuando así lo exija el perfil aplicable.
2. **Tres auditorías obligatorias previas a la entrega:**
   - Antes de entregar cualquier producto académico o jurídico en Word, ejecutar las **tres auditorías** descritas en el `MODULO.md` de `EDI-01`:
     1. **Auditoría de formato Word (`05_formato_word_mrci`):** Incluye verificación de referencias con cursivas reales (`audit_references()`) y tablas con bandas alternas `#EAF4FB`/`#FFFFFF` (`audit_tables()`, perfil 1.6.0).
     2. **Auditoría de voz y metatexto (`04_perfil_autoral_japr`):** Control de las 42 entradas de `LEXICO_CONTROL_IA.csv` y cero rastro de nombres internos del sistema.
     3. **Auditoría visual sobre el render completo:** Revisión renglón por renglón de la versión final renderizada.
   - Ninguna de las tres auditorías sustituye a las otras dos.

## 4. Dictamen de cierre académico

- Revisar cada renglón de la versión final renderizada, cada cita y cada referencia, incluidas tablas, notas y anexos.
- Registrar en el expediente interno la evidencia, versión, huellas y cobertura por conjunto (sin mezclar este expediente con el documento entregable).
- Estado de control interno:
  - Usar `ENTREGA_BLOQUEADA` ante cualquier error, cotejo pendiente o revisión incompleta.
  - Usar `VALIDADO_PARA_ENTREGA_ACADEMICA` únicamente tras el cierre documentado de todos los controles aplicables.
- No certificar contenido sustantivo mediante simples conteos, hashes o inspección de metadatos. El estado editorial no constituye aprobación institucional ni garantía de verdad.
