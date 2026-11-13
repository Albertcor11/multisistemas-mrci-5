# Mini-Skill DOC-04 · Plantillas del Usuario, Requisitado y Consistencia Transversal

Esta ficha se carga bajo demanda cuando el encargo requiere convertir un formato o documento muestra en plantilla reutilizable con Ficha de Requisitado, incorporar o rellenar moldes institucionales Word (`.docx`) conservando logotipos y diseño original, emitir versiones simultáneas de un mismo asunto para distintos destinatarios sin contradicciones de datos, o validar exactitud fáctica campo por campo contra una Ficha de Datos Maestros.

## 1. Rutas de entrada y activación

- **Instrucciones completas de la mini-skill:** [MODULO.md](../extensions/DOC-04/MODULO.md)
- **Guías operativas especializadas:**
  - [Parametrización y Ficha de Requisitado](../extensions/DOC-04/references/parametrizacion-y-requisitado.md)
  - [Incorporación de formatos `.docx` del usuario y versionado](../extensions/DOC-04/references/incorporacion-formatos-usuario.md)
  - [Adaptación multi-destinatario y consistencia transversal](../extensions/DOC-04/references/adaptacion-y-consistencia-transversal.md)
  - [Validación contra Ficha Maestra y control de pendientes](../extensions/DOC-04/references/validacion-ficha-maestra-y-pendientes.md)
- **Script opcional de auditoría estructural `.docx`/`.md`:** `extensions/DOC-04/scripts/auditar_plantilla_docx.py`
- **Activación desde el orquestador:**
  ```bash
  python3 scripts/orquestador.py activar <RECTOR_SUSTANTIVO> DOC-04
  ```
  *(Añadir `DOC-02` cuando se requiera dictamen formal de conformidad `MPRO`, y `DOC-03` para cadena de custodia y trazabilidad probatoria).*

## 2. Reglas de coordinación y ejecución

1. **Coordinación con especialidad sustantiva, `DOC-02`, `REDO` y `EDI-01`:**
   - Conservar siempre al módulo especialista (`MRCI-00`, `MUN-01`, `INM-01`, `SEG-01`, `JUD-01`, `JUD-02`, `EDU-01`, `FIL-01` o la Suite Jurídico-Fiscal) como responsable del fondo técnico y de la verificación normativa vigente.
   - Trabajar con datos reales del usuario y sus clientes sin restricción; únicamente al despersonalizar un documento previo para convertirlo en plantilla reutilizable se limpian los residuos del asunto anterior, preservando intactos los datos fijos reales y el logotipo de la entidad titular del formato.
   - Respetar al 100% la estructura, logotipos (`w:drawing`), encabezados, pies y estilos de cualquier molde `.docx` aportado por el usuario (copia física `shutil.copy2` + edición localizada; nunca recrear `Document()` en blanco ni sobreescribir con el perfil académico `#4169E1` de `EDI-01`). Sin molde `.docx` del usuario, aplicar el formato del módulo rector.
2. **Almacenamiento externo y separación en Dos Capas:**
   - Guardar el catálogo de formatos incorporados por el usuario (`<codigo>.docx`, `<codigo>.md` y su bitácora de versiones) **en la carpeta de trabajo o expediente del usuario**, jamás dentro de `extensions/DOC-04/` ni del árbol de la skill instalada.
   - **Capa 1 (Documento entregable):** limpio, autónomo y dirigido a su lector real; usar `[PENDIENTE: <dato>]` sólo si faltan insumos y el usuario pidió un borrador preliminar.
   - **Capa 2 (Cédula interna de control):** archivo independiente donde se entregan la Ficha de Requisitado, la Tabla de Consistencia Transversal, la matriz de hallazgos (`Crítico`, `Mayor`, `Menor`, `Observación`), el estado operativo (`BORRADOR_PARA_REVISION`, `VALIDADO_CON_CONDICIONES`, `REQUIERE_VALIDACION_HUMANA`) y el dictamen (`CONFORME`, `CONFORME CON OBSERVACIONES`, `NO CONFORME`).
3. **Doble compuerta previa a la entrega:**
   - Verificar preservación de medios, cero marcadores `[Ej. ...]` residuales y paridad fáctica con `python3 extensions/DOC-04/scripts/auditar_plantilla_docx.py <entregable.docx> [--molde <molde.docx>]`.
   - Ejecutar `python3 scripts/orquestador.py auditar <entregable>` hasta obtener `APROBADO_PARA_ENTREGA` (cero menciones a `DOC-04`, `MRCI`, `MPRO`, `JAPR` o códigos internos).
