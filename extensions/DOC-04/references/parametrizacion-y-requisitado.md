# Parametrización de Formatos y Ficha de Requisitado

Esta guía establece el procedimiento obligatorio para convertir cualquier documento muestra, formulario institucional o machote profesional en una plantilla estructurada, verificable y libre de ambigüedades, tanto en entornos con Python como en operación puramente instruccional.

---

## 1. Descomposición estructural en cinco categorías

Antes de numerar campos o redactar una guía `<codigo>.md`, todo documento origen deberá analizarse párrafo por párrafo, tabla por tabla y sección por sección (incluidos encabezados y pies de página) para clasificar cada fragmento en una sola de las cinco categorías siguientes:

1. **Elementos fijos institucionales:** textos, cláusulas, leyendas legales, membretes, logotipos y datos reales permanentes de la entidad emisora dueña del formato (denominación o razón social, RFC, domicilio fiscal/convencional, datos de contacto institucionales y denominación fija de áreas o cargos firmantes). Se conservan íntegros.
2. **Campos variables atómicos (`[1]…[N]`):** datos que cambian en cada emisión (fechas, folios, destinatario, identificadores fiscales o registrales del tercero, importes, periodos, descripciones específicas). Se sustituyen por marcadores numerados consecutivos en orden de aparición (`[1]`, `[2]`, …, `[N]`). Si el mismo dato exacto reaparece varias veces en el documento (por ejemplo, el folio del contrato o el monto total), reutiliza el **mismo número de campo** para garantizar consistencia automática.
3. **Bloques condicionales:** párrafos, incisos o cláusulas cuya inclusión depende de un supuesto fáctico o jurídico verificable. Se delimitan explícitamente como:
   `[BLOQUE CONDICIONAL C1 — Incluir sólo si <condición objetiva>: "<texto íntegro del bloque con sus campos [k]>"]`.
4. **Tablas o listas dinámicas:** estructuras cuyo número de filas varía según los registros del expediente (partidas, facturas, documentos exhibidos, participantes, inmuebles, pólizas). Se documentan definiendo columnas fijas, tipo de dato por celda, orden de clasificación y regla aritmética de subtotales/totales (`[TABLA DINÁMICA T1: columnas C_1..C_m; regla de suma]`).
5. **Zonas intocables / prohibidas:** logotipos (`w:drawing`), sellos digitales o gráficos, cintillos corporativos, espacios de firma autógrafa, folios oficiales preimpresos y certificaciones de terceros. Queda prohibido alterarlas, redimensionarlas o suprimirlas.

---

## 2. Estándar obligatorio de la Ficha de Requisitado (6 columnas)

Toda guía `<codigo>.md` deberá incluir una **Ficha de Requisitado** con exactamente las seis columnas siguientes para la totalidad de los campos `[1]…[N]`, bloques condicionales `C1…Ck` y tablas dinámicas `T1…Tm`:

| Campo | Nombre del dato | Descripción y formato exacto | Fuente documental esperada | Obligatoriedad | Regla de validación / abstención |
|---|---|---|---|---|---|
| `[1]` | Lugar y fecha de emisión | Municipio, entidad federativa y fecha en formato `DD de <mes> de AAAA` | Instrucción de emisión o Ficha Maestra del expediente | Obligatorio | Verificar congruencia cronológica (no anterior a los actos que reseña); si no se indica fecha de firma, marcar `[PENDIENTE: fecha de emisión]`. |
| `[2]` | Folio interno del documento | Clave alfanumérica institucional (ej. `OFI-AREA-AAAA-NNN`) | Consecutivo del área emisora o Ficha Maestra | Obligatorio | Prohibido inventar consecutivos; si el área asigna el folio al firmar, insertar `[PENDIENTE: asignación de folio interno]`. |
| `[3]` | Denominación o nombre del destinatario | Razón social íntegra con régimen societario o nombre completo sin abreviar | Ficha de Datos Maestros / instrumento constitutivo o identificación | Obligatorio | Cotejo literal letra por letra contra Ficha Maestra; divergencia = hallazgo `Crítico`. |

### Reglas de redacción para las seis columnas

- **Formato exacto:** especificar patrón de fecha, moneda con código y dos decimales (`$0,000.00 MXN` más importe con letra cuando el acto lo exija), mayúsculas/minúsculas y régimen societario completo.
- **Fuente documental esperada:** señalar de qué pieza verificada debe provenir el dato (Ficha Maestra, contrato firmado, comprobante bancario, constancia oficial, acuse de recepción), evitando referencias vagas como *"datos del usuario"*.
- **Obligatoriedad:** clasificar únicamente como `Obligatorio`, `Condicional (especificar supuesto)` u `Opcional (especificar qué ocurre si se omite: suprimir línea o asentar "No aplica")`.
- **Regla de validación / abstención:** definir la comprobación objetiva (cruce aritmético, formato de clave, concordancia con otro campo) y el comportamiento exacto ante ausencia del insumo.

---

## 3. Regla de abstención controlada ante datos ausentes

Al requisitar cualquier plantilla a partir de los insumos entregados por el usuario:

1. **Prohibición absoluta de inferencia o relleno:** nunca deducir fechas de firma a partir de nombres de archivo, no completar RFC o CURP parciales, no asumir cargos de representación no acreditados y no arrastrar valores del documento muestra original.
2. **Modalidad de entrega definitiva:** si el usuario solicitó un documento listo para firma o emisión externa y falta al menos un campo `Obligatorio`, detener la liberación definitiva, clasificar el faltante como `Crítico` en la Cédula Interna y solicitar puntualmente el dato faltante.
3. **Modalidad de borrador preliminar:** si el usuario autorizó o solicitó expresamente un borrador de avance pese a tener insumos incompletos:
   - Insertar en la posición exacta del campo el marcador limpio `[PENDIENTE: <nombre específico del dato requerido>]`.
   - Asignar al expediente el estado `BORRADOR_PARA_REVISION` en la Cédula Interna de Control.
   - Advertir en la respuesta al usuario cuántos campos `[PENDIENTE: ...]` permanecen abiertos antes de que el archivo pueda pasar a `REQUIERE_VALIDACION_HUMANA`.

---

## 4. Protocolo de verificación de plantillas (3 corridas: A / B / Incompleto)

Antes de declarar una plantilla nueva o modificada como `VIGENTE` dentro del catálogo del usuario (`MPRO_0201`), verificar su comportamiento frente a tres escenarios de prueba documentados en la Cédula Interna:

1. **Conjunto A (Caso ordinario completo):** todos los campos obligatorios presentes, una fila en tablas dinámicas y bloques condicionales inactivos. Comprueba fluidez gramatical, concordancia de género/número y ausencia de corchetes residuales.
2. **Conjunto B (Caso complejo con variantes):** activa todos los bloques condicionales `C1…Ck` y múltiples filas en tablas dinámicas `T1…Tm`. Comprueba que los subtotales/totales cuadren, que las tablas no desborden márgenes y que los bloques condicionales encajen sin rupturas de numeración.
3. **Conjunto Incompleto (Prueba de estrés de candados):** omite deliberadamente dos campos obligatorios determinantes (por ejemplo, número de registro y comprobante de pago). Comprueba que el flujo inserte `[PENDIENTE: ...]` sin alucinar datos y que la Cédula Interna emita dictamen `NO CONFORME` para liberación definitiva.

---

## 5. Micro-ejemplo neutro de guía parametrizada (`FOR-REC-01.md`)

```markdown
# Guía de Plantilla: Constancia de Revisión de Entregables (FOR-REC-01)
- Versión de plantilla: 1.0.0 | Estado en catálogo del usuario: VIGENTE
- Archivo molde asociado: plantillas_usuario/FOR-REC-01.docx (con membrete y logotipo del emisor intactos)

## Cuerpo parametrizado
En [1], siendo el [2], el área de [3] hace constar la revisión documental correspondiente al periodo [4] respecto del expediente o contrato [5], presentado por [6] (identificador fiscal: [7]).

[TABLA DINÁMICA T1: Columna 1 = Documento exigible | Columna 2 = Estatus verificado (Aportado / En trámite — no acreditado / Omitido) | Columna 3 = Observación objetiva]

Importe total sujeto a validación documental: [8].
[BLOQUE CONDICIONAL C1 — Incluir sólo si existen partidas con estatus distinto de "Aportado":
"La liberación administrativa del importe señalado en [8] queda sujeta a la recepción material e íntegra de los soportes listados como pendientes."]
```
