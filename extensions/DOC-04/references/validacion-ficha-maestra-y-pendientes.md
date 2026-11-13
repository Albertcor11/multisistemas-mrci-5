# Validación contra Ficha de Datos Maestros, Evidencia Material y Control de Pendientes

Esta guía regula la auditoría fáctica campo por campo sobre formatos requisitados o borradores documentales, complementando en el plano operativo al protocolo transversal `00-protocolo-realidad-fuentes.md`, a `DOC-02` (`MPRO_0201` y `MPRO_0202`) y a `DOC-03` (`MTRA`).

---

## 1. Jerarquía de insumos y primacía de la Ficha de Datos Maestros

Cuando el expediente del asunto contenga múltiples documentos de entrada, el requisitado y la auditoría fáctica se sujetan al siguiente orden estricto de prelación:

1. **Instrumentos primarios y constancias oficiales verificadas** (escrituras, contratos firmados, constancias fiscales o registrales vigentes, comprobantes bancarios de pago con sello/cadena verificable, acuses oficiales).
2. **Ficha de Datos Maestros del expediente** validada por el usuario o extraída de los instrumentos primarios del nivel 1.
3. **Acuses operativos, relaciones de entrega o estados de cuenta del periodo evaluado.**
4. **Borradores previos, minutas informales, correos de remisión o notas de trabajo secundarias.**

### Regla ante contradicciones entre insumos

- Si un correo, carátula o borrador secundario contiene un dato que contradice a un instrumento primario o a la Ficha de Datos Maestros (por ejemplo: RFC con homoclave errónea, fecha de contrato equivocada, número de registro vencido o suma aritmética mal calculada), **prevalece el dato verificado de mayor jerarquía**.
- Nunca corregir en silencio sin dejar rastro para el operador: en el entregable de Capa 1 se asienta el dato maestro correcto, y en la **Cédula Interna de Control (Capa 2)** se documenta explícitamente la discrepancia detectada entre ambos insumos para conocimiento y validación humana.
- Si la contradicción ocurre entre dos documentos del **mismo nivel superior** (por ejemplo, dos cláusulas contradictorias del mismo contrato firmado), no elegir arbitrariamente: señalar la colisión y reservar decisión humana (`REQUIERE_VALIDACION_HUMANA`).

---

## 2. Separación estricta: *aportado* vs. *mencionado / en trámite / sin entero bancario*

En todo formato de revisión documental, cumplimiento contractual, auditoría de proveedores, siniestros o integración de expedientes, aplicar sin excepción las cuatro reglas materiales siguientes:

1. **Mencionado ≠ Aportado:** que un oficio de remisión o índice declare anexar un documento no prueba su existencia ni su contenido si el soporte no consta materialmente o si el acuse mismo registra entrega parcial (por ejemplo, 5 comprobantes entregados de una plantilla de 6). Contabilizar siempre unidades efectivamente exhibidas frente a unidades exigibles.
2. **"En trámite" = No acreditado a la fecha de corte:** manifestaciones como *"en proceso de presentación"*, *"pendiente de descarga"*, *"en renovación"* o *"se entregará la próxima semana"* se clasifican objetivamente como **soporte faltante / no cumplido a la fecha de revisión**, registrando textualmente el dicho del remitente solo como antecedente declarativo.
3. **Línea de captura o declaración sin pago ≠ Pago acreditado:** un formato de línea de captura (tesorería, seguridad social, contribuciones federales o locales), una propuesta de cédula de autodeterminación o un acuse de declaración con importe a cargo **sin comprobante bancario de pago efectivo** únicamente acredita la determinación o generación de la línea, **nunca la extinción ni el pago de la obligación**.
4. **Aritmética y plazos:**
   - Recalcular siempre todas las operaciones del documento (sumas de partidas, tasas de impuestos o retenciones, diferencias y conteos). Si el insumo trae una suma equivocada, reportarlo como hallazgo en la Cédula Interna.
   - En cómputos de plazos legales, contractuales o de prescripción/caducidad, verificar días hábiles/naturales conforme a la norma aplicable consultada en vivo y mantener siempre reserva de verificación final por el profesional responsable.

---

## 3. Higiene de marcadores residuales

Antes de emitir cualquier documento (sea definitivo o preliminar), inspeccionar cuerpo, tablas, notas al pie, encabezados y pies de página para confirmar:

- **Cero residuos de plantilla:** ausencia total de marcadores numéricos `[1]`, etiquetas `[Insertar ...]`, `[Ej. ...]`, `{{variable}}`, `<campo>`, `XXXX`, líneas de subrayado vacías de formulario cuando el campo ya fue llenado o comentarios internos del molde.
- **Uso controlado de `[PENDIENTE: ...]`:** permitido **exclusivamente** cuando faltan datos verificados y el usuario solicitó un borrador preliminar; el texto dentro del corchete debe nombrar con exactitud el dato faltante (ej. `[PENDIENTE: folio de registro vigente]`), sin incluir códigos internos de la skill.

---

## 4. Lista de control universal, severidades y dictamen (Capa 2 — Cédula Interna)

Toda revisión o emisión controlada bajo `DOC-04` se respalda en la Cédula Interna verificando doce dimensiones fácticas universales:
1) Identidad de las partes; 2) Representación/facultades; 3) Vigencia del acto o contrato base; 4) Universo cuantitativo evaluado (partidas/personal/bienes); 5) Exactitud aritmética al centavo; 6) Registros o autorizaciones especiales aplicables; 7) Objeto y alcance del documento; 8) Fechas, periodos y reserva humana de plazos; 9) Separación material *aportado vs. en trámite / sin comprobante de pago*; 10) Paridad transversal entre documentos del paquete; 11) Trazabilidad de fundamentos verificados; y 12) Ausencia total de datos inventados, residuos de otros asuntos y metatexto interno.

### Escala de severidades homologada con `DOC-02` (`MPRO_0202`)

| Severidad | Supuestos objetivos | Efecto sobre la entrega |
|---|---|---|
| `Crítico` | Dato inventado o no sustentado; contradicción con Ficha Maestra; dato residual de otro cliente/asunto arrastrado desde una plantilla; línea de captura tratada como pago efectivo; divergencia numérica o de fechas entre documentos del mismo paquete; marcador `[Ej. ...]` olvidado; filtración de nombres internos del sistema (`DOC-04`, `MRCI`, etc.). | **Bloquea liberación (`NO CONFORME`).** Debe corregirse antes de entregar (o emitirse expresamente como `BORRADOR_PARA_REVISION` únicamente si el motivo es un insumo faltante marcado con `[PENDIENTE: ...]`). |
| `Mayor` | Bloque condicional pertinente omitido sin falsear hechos; falta de desglose entre entrega parcial y total; cita normativa incompleta o sin localizador verificado. | Exige corrección previa o pasa a `CONFORME CON OBSERVACIONES` sólo bajo instrucción expresa de avance. |
| `Menor` | Desajuste menor de puntuación, abreviatura no homogénea o formato de celda que no altera cifras, fechas ni sentido jurídico. | Se corrige de inmediato; de subsistir por restricción del molde externo, se documenta como `CONFORME CON OBSERVACIONES`. |
| `Observación` | Mejora preventiva sugerida sobre el diseño o la Ficha de Requisitado de la plantilla del usuario para futuras emisiones. | No bloquea (`CONFORME`); se anota para el mantenimiento del catálogo del usuario. |

### Estados del entregable y Dictamen en la Cédula Interna

- **Estado operativo del archivo de caso (`ESQUEMA_EXPEDIENTE.md`):**
  - `BORRADOR_PARA_REVISION`: contiene uno o más `[PENDIENTE: ...]` por insumos aún no entregados por el usuario; no apto para firma ni envío externo.
  - `VALIDADO_CON_CONDICIONES`: todos los controles documentales cerrados y sin pendientes fácticos, sujeto a reservas técnicas expresas en la Cédula Interna.
  - `REQUIERE_VALIDACION_HUMANA`: documento completo y auditado (`APROBADO_PARA_ENTREGA` en `orquestador.py auditar`), listo para revisión final y firma autógrafa o electrónica del responsable humano.
- **Resultado del Dictamen de Conformidad (`MPRO_0201`):** `CONFORME` | `CONFORME CON OBSERVACIONES` | `NO CONFORME`.
