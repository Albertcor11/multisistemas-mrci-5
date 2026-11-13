---
name: plantillas-y-consistencia-documental
description: Parametrizar e incorporar formatos propios (.docx/.md) conservando logotipos y diseño, requisitarlos contra fichas maestras sin inventar datos y verificar consistencia transversal entre versiones por destinatario.
---

# Plantillas del Usuario, Requisitado y Consistencia Transversal (DOC-04)

## 1. Identidad, alcance y coordinación en el ecosistema

- **Identificador funcional:** `DOC-04`
- **Nombre interno:** `plantillas-y-consistencia-documental`
- **Capa en el orquestador:** `formato`
- **Activación selectiva:** `python3 scripts/orquestador.py activar <RECTOR_SUSTANTIVO> DOC-04` (añadir `DOC-02` o `DOC-03` cuando se requiera dictamen institucional o trazabilidad probatoria reforzada).

Al iniciar cualquier encargo, leer y aplicar el Núcleo Transversal devuelto por el orquestador (`00-protocolo-realidad-fuentes.md`, `01-perfil-humanizacion-japr.md` y `02-citacion-edicion.md`).

### Operación en entornos reales, simulados y académicos

`DOC-04` opera sin restricción con **datos reales** de personas físicas, empresas, despachos, autoridades, contratos, expedientes, cuentas y montos proporcionados por el usuario, así como en escenarios simulados o académicos. Únicamente cuando se transforma un documento previamente utilizado en una **plantilla reutilizable**, deberán eliminarse los datos residuales del cliente o asunto anterior, **conservando intactos los datos fijos reales de la entidad propietaria del formato** (denominación o razón social, RFC, domicilio, membrete, logotipo y cargos fijos de firma).

### Fronteras inter-modulares obligatorias

1. **Fondo sustantivo y vigencia normativa (`MRCI-00`, Suite Jurídico-Fiscal y especialistas):** `DOC-04` gobierna la ingeniería funcional de plantillas, el requisitado controlado y la paridad de datos; el análisis jurídico, fiscal, municipal, inmobiliario, asegurador, jurisdiccional, educativo o filosófico permanece en el módulo sustantivo rector (`MUN-01`, `INM-01`, `SEG-01`, `JUD-01`, `JUD-02`, `EDU-01`, `FIL-01` o `MRCI-00`). Queda prohibido congelar leyes, tasas, salarios mínimos o indicadores anuales dentro de `DOC-04`; toda norma o tarifa se verifica en fuente oficial vigente conforme a `00-protocolo-realidad-fuentes.md`.
2. **Coordinación con `DOC-02` (`produccion-documental-mrci` / Sistema `MPRO`):** Las 7 secciones obligatorias de `MPRO_0100` rigen los documentos normativos internos del ecosistema MRCI. `DOC-04` no impone esas 7 secciones sobre formatos propios del usuario ni sobre oficios/contratos externos, pero adopta el ciclo de vida de catálogo (`MPRO_0201`), la escala de 4 severidades y los 3 niveles de dictamen (`MPRO_0202`) en la cédula interna de control.
3. **Frontera con el modo `REDO` (Suite Jurídico-Fiscal en `EDI-01`):** `REDO` redacta o reestructura documentos jurídicos, contratos y controles de cambios en prosa libre. `DOC-04` se activa específicamente cuando el encargo exige: (a) parametrizar un formato con campos `[1]…[N]` y Ficha de Requisitado; (b) incorporar o mantener un catálogo externo `<codigo>.docx` + `<codigo>.md` con logotipo; (c) emitir versiones simultáneas por destinatario con Tabla de Consistencia Transversal; o (d) auditar exactitud fáctica campo por campo contra una Ficha de Datos Maestros.
4. **Precedencia visual frente a `EDI-01` (`vendor/documents/` y `05_formato_word_mrci` v1.6.0):**
   - **Con molde `.docx` aportado por el usuario:** el archivo del usuario es la autoridad absoluta de diseño (logotipos, encabezados, pies, márgenes, tipografía, colores y tablas). Queda prohibido sobreescribirlo con el perfil académico Azul Rey `#4169E1` o recrearlo desde un documento en blanco.
   - **Sin molde `.docx` del usuario (generación desde guía `.md`):** se aplica el perfil de formato del módulo rector del encargo (por ejemplo, `PERFIL_FORMATO_WORD_MRCI.json` v1.6.0 cuando rija `EDI-01`), sin introducir paletas ni estilos ajenos al ecosistema.
5. **Custodia y evidencia (`DOC-01` y `DOC-03`):** La catalogación institucional permanente corresponde a `DOC-01` y la cadena de custodia o valoración probatoria material corresponde a `DOC-03`.

---

## 2. Capacidades operativas y guías de referencia

Consultar bajo demanda únicamente las guías aplicables al encargo:

1. **Parametrización de formatos y Ficha de Requisitado:** [parametrizacion-y-requisitado.md](references/parametrizacion-y-requisitado.md)
   Descomposición en elementos fijos, campos variables `[1]…[N]`, bloques condicionales, tablas dinámicas y zonas intocables; construcción de la Ficha de Requisitado de 6 columnas y protocolo de prueba A / B / Incompleto.
2. **Incorporación de formatos propios `.docx` con logotipo y versionado de catálogo:** [incorporacion-formatos-usuario.md](references/incorporacion-formatos-usuario.md)
   Limpieza selectiva de residuos del asunto previo preservando la identidad fija del titular, resguardo externo del par `<codigo>.docx` + `<codigo>.md`, requisitado quirúrgico sobre copia física (`shutil.copy2`) y versionado semántico `X.Y.Z` con análisis de impacto.
3. **Adaptación multi-destinatario y paridad de datos:** [adaptacion-y-consistencia-transversal.md](references/adaptacion-y-consistencia-transversal.md)
   Ajuste de densidad, estructura y tono para audiencias distintas a partir de un mismo expediente (análisis técnico interno, requerimiento externo, síntesis directiva) garantizando cero contradicciones mediante una Tabla de Consistencia Transversal obligatoria.
4. **Validación contra Ficha de Datos Maestros y control de pendientes:** [validacion-ficha-maestra-y-pendientes.md](references/validacion-ficha-maestra-y-pendientes.md)
   Prelación de la Ficha Maestra sobre borradores secundarios, separación estricta entre soporte *aportado* y soporte *mencionado / en trámite / línea de captura sin comprobante bancario*, eliminación de corchetes residuales y emisión de dictamen en cédula interna.

Cuando un encargo combine las cuatro operaciones, ejecutar en orden: **1) Validación de insumos y Ficha Maestra → 2) Requisitado del documento base → 3) Adaptación a destinatarios derivados → 4) Cruce transversal y auditoría de salida**.

---

## 3. Operación dual según capacidades del entorno

- **Entorno con ejecución de Python:**
  - Clonar siempre el molde `.docx` del usuario mediante copia física (`shutil.copy2`) y editar únicamente los tramos variables conservando corridas de formato (`w:r`), encabezados, pies e imágenes incrustadas (`w:drawing` / `word/media/*`).
  - Cuando el corpus de `EDI-01` esté activo en caché, apoyarse opcionalmente en `vendor/documents/` (`template-distill.md`, `template-create.md`, `privacy_scrub.py`, `redact_docx.py`, `docx_ooxml_patch.py` y `render_docx.py` si LibreOffice está disponible).
  - Ejecutar [auditar_plantilla_docx.py](scripts/auditar_plantilla_docx.py) para verificar preservación de medios/logotipos, ausencia de marcadores residuales `[Ej. ...]` y control de `[PENDIENTE: ...]`.
- **Entorno sin ejecución de Python:**
  - Declarar el alcance del entorno sin fingir ejecución de scripts.
  - Entregar íntegramente en Markdown estructurado la plantilla parametrizada `<codigo>.md`, su Ficha de Requisitado de 6 columnas, el texto requisitado bloque por bloque listo para vaciado en el formato institucional y la Cédula Interna de Control.

---

## 4. Separación en Dos Capas, almacenamiento externo y compuerta de entrega

### Dos capas que nunca se mezclan

1. **Capa 1 — Documento entregable (`.docx` / `.md`):** dirigido exclusivamente a su lector real (cliente, autoridad, contraparte, dirección). Debe leerse como un documento profesional autónomo. **Jamás** contiene menciones a `DOC-04`, `MRCI`, `MPRO`, `JAPR`, códigos internos del orquestador ni tablas de auditoría o checklists pegados al final. Únicamente si faltan datos determinantes y el usuario solicitó un borrador preliminar, podrá incluir marcadores limpios `[PENDIENTE: <dato requerido>]`.
2. **Capa 2 — Cédula / expediente interno de control:** archivo o reporte separado dirigido al usuario operador. Contiene la Ficha de Requisitado, la Tabla de Consistencia Transversal, la matriz de hallazgos contra Ficha Maestra (`Crítico`, `Mayor`, `Menor`, `Observación`), el estado operativo del entregable (`BORRADOR_PARA_REVISION`, `VALIDADO_CON_CONDICIONES` o `REQUIERE_VALIDACION_HUMANA`) y el dictamen (`CONFORME`, `CONFORME CON OBSERVACIONES` o `NO CONFORME`).

### Almacenamiento obligatorio fuera de la skill

Los formatos que incorpore el usuario (`<codigo>.docx`, `<codigo>.md` y su bitácora de versiones) deberán guardarse **siempre en el directorio de trabajo o expediente del usuario** (por ejemplo, `<carpeta_trabajo>/plantillas_usuario/`, o como entregables descargables en entornos web), **nunca dentro de `extensions/DOC-04/` ni en ninguna ruta interna del repositorio `multisistemas-mrci-5`**.

### Compuerta obligatoria previa a la entrega

Antes de entregar cualquier archivo de Capa 1, ejecutar:
```bash
python3 scripts/orquestador.py auditar <ruta_del_archivo_entregable>
```
Si devuelve `ENTREGA_BLOQUEADA`, depurar cualquier código interno o expresión vetada y repetir la auditoría hasta obtener `APROBADO_PARA_ENTREGA`.

---

## 5. Prohibiciones estrictas

- Inventar, suponer, interpolar o autocompletar nombres, RFC, folios, fechas, cuentas, montos o cargos ausentes en los insumos verificados.
- Dar por acreditado un pago o cumplimiento con la sola mención en un oficio, una promesa *"en trámite"* o una línea de captura sin comprobante bancario de entero efectivo.
- Recrear desde cero (`Document()` en blanco) un formato `.docx` con logotipo o membrete del usuario, o sobreescribir su diseño institucional con colores o plantillas genéricas.
- Guardar plantillas o datos del usuario dentro del directorio instalado de la skill (`extensions/DOC-04/`).
- Dejar marcadores de ejemplo del molde (`[1]`, `[Ej. ...]`, `{{campo}}`, `XXXX`) en un documento requisitado, o mezclar la Cédula Interna de Control dentro del archivo entregable de Capa 1.
