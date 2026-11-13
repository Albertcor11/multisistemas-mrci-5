# Adaptación Multi-Destinatario y Consistencia Transversal

Esta guía rige los encargos en que un mismo asunto, expediente o revisión técnica debe traducirse simultáneamente en **dos o más documentos dirigidos a destinatarios con distinto rol** (por ejemplo: dictamen o memorando técnico interno, oficio o requerimiento formal a contraparte/proveedor, nota ejecutiva para dirección general o comunicado operativo interno).

---

## 1. Regla de fuente única y paridad fáctica innegociable

Todo paquete multi-destinatario se construye a partir de **un solo corte fáctico validado** (la Ficha de Datos Maestros del expediente más los documentos soporte verificados). Al adaptar entre audiencias:

- **Qué SÍ cambia:** extensión, orden expositivo (apertura por hallazgos técnicos vs. requerimiento puntual vs. decisión ejecutiva), nivel de detalle procedimental y registro comunicativo acorde a la relación jurídica o institucional con el lector.
- **Qué NUNCA cambia:** razones sociales o nombres completos, RFC/CURP/registros oficiales, fechas de contratos o eventos, folios de expedientes/facturas/pólizas, periodos revisados, conteos de soportes exhibidos frente a faltantes, importes desglosados (subtotal, impuestos, retenciones, total), moneda y plazos objetivos.

Una variación involuntaria de un solo dígito, fecha o denominación entre dos entregables del mismo paquete constituye un hallazgo `Crítico` y bloquea la liberación del conjunto completo.

---

## 2. Reglas de transformación según el perfil del destinatario

| Perfil de destinatario | Propósito del documento | Densidad y estructura | Regla de resguardo y tono |
|---|---|---|---|
| **A. Técnico / Control Interno** *(Jurídico, Fiscal, Contraloría, Auditoría, Cumplimiento)* | Sustentar exhaustivamente el diagnóstico, la evidencia revisada, los faltantes y las consecuencias normativas o contractuales. | Extensión completa: antecedentes verificados, inventario íntegro de pruebas (*aportadas vs. mencionadas/en trámite*), análisis técnico fundamentado y acciones recomendadas. | Precisión técnica estricta; explicita reservas probatorias, riesgos cuantificados y puntos pendientes de verificación humana. |
| **B. Externo / Contraparte o Autoridad** *(Proveedor, Cliente externo, Aseguradora, Dependencia)* | Requerir cumplimiento, notificar determinaciones, formalizar entregas o desahogar prevenciones con efectos jurídicos o contractuales. | Extensión focalizada: identificación exacta del vínculo/expediente, relación numerada y verificable de lo exhibido o requerido, fundamento aplicable y condición o plazo de atención. | **Frontera de confidencialidad obligatoria:** prohibido filtrar deliberaciones estratégicas internas, calificaciones subjetivas, hipótesis de litigio o estimaciones internas de contingencia del emisor. |
| **C. Directivo / Órgano de Decisión** *(Dirección General, Presidencia, Consejo, Comité)* | Habilitar una toma de decisión inmediata e informada con lectura ágil (1 a 2 cuartillas máximo). | Apertura directa en el primer párrafo con la conclusión central, el impacto económico/operativo exacto y las decisiones concretas requeridas (autorizar, retener, firmar, escalar). | Lenguaje ejecutivo directo, sin jerga innecesaria ni transcripción masiva de artículos, pero conservando intactas las cifras exactas y las condiciones críticas. |
| **D. Operativo / Difusión Interna** *(Boletín de área, instrucción a equipos ejecutores)* | Estandarizar criterios de actuación o controles de recepción para el personal operativo. | Reglas claras de acción inmediata (*qué recibir, qué rechazar, cuándo escalar*), listas de cotejo operativas y vigencia del criterio. | Prescriptivo y práctico; cuando se refiera a casos previos como antecedente interno, mantener coherencia exacta con las reglas institucionales vigentes. |

---

## 3. Tabla de Consistencia Transversal obligatoria (Capa 2 — Cédula Interna)

Siempre que se generen o revisen dos o más documentos derivados del mismo asunto, deberá construirse e incluirse en la **Cédula Interna de Control** (nunca pegada dentro de los archivos entregables de Capa 1) una **Tabla de Consistencia Transversal** que cruce celda por celda todos los datos duros compartidos:

| Atributo crítico | Valor maestro verificado (fuente) | Entregable 1 (`<archivo_1>`) | Entregable 2 (`<archivo_2>`) | Entregable N (`<archivo_N>`) | Resultado de paridad |
|---|---|---|---|---|---|
| Partes y RFC / IDs | `<Valor exacto — Ficha Maestra>` | `<Valor asentado o N/A justificado>` | `<Valor asentado>` | `<Valor asentado>` | `IDÉNTICO` |
| Vínculo / Contrato / Expediente y fecha | `<Valor exacto — Contrato / Ficha>` | `<Valor asentado>` | `<Valor asentado>` | `<Valor asentado>` | `IDÉNTICO` |
| Periodo o acto evaluado | `<Mes / ejercicio / fecha corte>` | `<Valor asentado>` | `<Valor asentado>` | `<Valor asentado>` | `IDÉNTICO` |
| Conteo documental (aportados vs. faltantes) | `<X aportados / Y pendientes de Z>` | `<X / Y de Z>` | `<Y requeridos>` | `<Y pendientes>` | `CONCORDANTE` |
| Importes (subtotal, impuestos, total) | `<$Subtotal + $Imp = $Total MXN>` | `<$Subtotal / $Imp / $Total>` | `<$Total sujeto a condición>` | `<$Total en riesgo>` | `IDÉNTICO` |
| Condición, plazo o consecuencia | `<Regla contractual/legal exacta>` | `<Regla detallada>` | `<Condición exigida>` | `<Decisión propuesta>` | `CONCORDANTE` |

### Reglas de verificación sobre la tabla

1. **Cotejo sobre el archivo real generado:** los valores de las columnas `Entregable 1…N` se extraen leyendo el texto efectivo de los archivos `.docx`/`.md` ya producidos, no de la intención previa de redacción.
2. **Distinción entre `IDÉNTICO` y `CONCORDANTE`:**
   - Los identificadores, fechas, folios y cifras monetarias deben ser **exactamente idénticos** (o mostrar la suma exacta de sus componentes desglosados).
   - Cuando un resumen ejecutivo reporta solo el importe total (`$Total`) mientras el documento técnico desglosa `$Subtotal + $Impuesto = $Total`, el cruce es `CONCORDANTE` siempre que la suma aritmética sea exacta al centavo.
3. **Corrección antes de entregar:** si cualquier fila arroja discrepancia, corregir los entregables afectados, regenerar la tabla y ejecutar `python3 scripts/orquestador.py auditar` sobre cada archivo de Capa 1 antes de presentar el paquete al usuario.
