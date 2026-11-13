# Incorporación de Formatos Propios (`.docx`), Preservación de Logotipos y Versionado

Esta guía regula cómo absorber un documento Word institucional proporcionado por el usuario para integrarlo a su catálogo externo de plantillas reutilizables (`<codigo>.docx` + `<codigo>.md`), cómo requisitarlo preservando al 100% su diseño gráfico y cómo administrar su evolución mediante versionado semántico.

---

## 1. Despersonalización selectiva al crear el molde maestro

Cuando el usuario entrega un archivo `.docx` real previamente utilizado en otro asunto para convertirlo en plantilla reutilizable, se aplica una **separación estricta entre identidad propia fija y residuos del asunto previo**:

### A. Qué se conserva intacto en `<codigo>.docx` (Identidad fija del titular)
- Denominación o razón social real del despacho, empresa, institución o unidad administrativa propietaria del formato.
- RFC, domicilio fiscal o convencional, teléfonos, sitio web, avisos de privacidad y leyendas institucionales permanentes del emisor.
- Logotipos corporativos, escudos, marcas de agua institucionales (`word/media/*`, `w:drawing`, `v:imagedata`), cintillos de color, bordes, márgenes, tipografías, estilos de tabla, encabezados y pies de página.
- Títulos fijos de cargos institucionales cuando la firma corresponde siempre al mismo órgano o puesto del titular.

### B. Qué se limpia obligatoriamente en `<codigo>.docx` (Residuos de terceros o asuntos previos)
- Nombres de clientes, contrapartes, proveedores, representantes legales externos, testigos o autoridades destinatarias del asunto anterior.
- RFC, CURP, números de escritura, cuentas bancarias de terceros, folios de expediente, fechas específicas, periodos y montos particulares del caso previo.
- Comentarios de revisión anteriores, control de cambios pendiente y ejemplos prellenados (`[Ej. ...]`) que pudieran filtrarse por accidente en emisiones futuras; cada posición variable se reemplaza en el molde por su marcador limpio `[1]…[N]`.

> **Apoyo técnico opcional en entornos con Python:** Si se activó `EDI-01` y se requiere depurar metadatos ocultos de autoría previa o atributos `rsid*` en el molde maestro sin alterar su maquetación, puede emplearse `vendor/documents/scripts/privacy_scrub.py` (y `comments_strip.py` / `accept_tracked_changes.py` para limpiar revisiones antiguas) sobre la copia guardada en la carpeta del usuario.

---

## 2. Almacenamiento obligatorio en el espacio del usuario (nunca dentro de la skill)

Conforme a la regla de integridad de `SKILL.md` (§5), el árbol instalado de `multisistemas-mrci-5` es inmutable durante la operación ordinaria. Por tanto:

1. **Ubicación permitida:** guardar todo formato incorporado en la carpeta del proyecto o expediente del usuario, bajo una ruta explícita y ordenada:
   ```text
   <carpeta_trabajo_usuario>/plantillas_usuario/
   ├── CATALOGO_VERSIONES.md          ← inventario, estados MPRO_0201 e historial X.Y.Z
   ├── <codigo>.docx                  ← molde limpio con logotipo y estilos originales intactos
   └── <codigo>.md                    ← estructura parametrizada [1]…[N] y Ficha de Requisitado
   ```
   *(En entornos conversacionales web sin carpeta local persistente, entregar el par `<codigo>.docx` y `<codigo>.md` como archivos descargables listos para resguardo del usuario).*
2. **Ubicación prohibida:** jamás escribir, copiar ni modificar archivos de usuario dentro de `extensions/DOC-04/`, `references/` ni `assets/` de la skill instalada.

---

## 3. Requisitado quirúrgico sobre copia física (`.docx` con logotipo)

Al generar un documento final o borrador a partir de un molde `<codigo>.docx` del usuario:

1. **Prohibición de reconstrucción en blanco:** nunca ejecutar `Document()` vacío para copiar texto o tablas manualmente, ya que ello destruye encabezados vinculados, relaciones OOXML de medios (`word/_rels/header1.xml.rels`), dimensiones exactas de logotipo, anclajes flotantes y estilos personalizados.
2. **Clonado físico previo:** copiar siempre el archivo binario íntegro antes de abrirlo:
   ```python
   import shutil
   shutil.copy2(ruta_molde_docx, ruta_entregable_docx)
   ```
3. **Sustitución preservando formato y medios (manejo de *run splitting*):**
   - Recorrer párrafos del cuerpo, celdas de tablas (incluidas tablas anidadas) y todas las variantes de encabezados y pies (`header`, `first_page_header`, `even_page_header`, `footer`, `first_page_footer`, `even_page_footer`) de cada sección.
   - **Precaución crítica sobre nodos gráficos:** nunca reasignar `paragraph.text = nuevo_texto` en un párrafo que contenga un nodo `<w:drawing>`, `<w:pict>` o `<v:imagedata>`, pues `python-docx` elimina todos los `runs` hijos (borrando el logotipo). Operar únicamente sobre los nodos `<w:r>` puramente textuales.
   - Si Word fragmentó un marcador `[12]` en varios `runs` consecutivos (`[`, `12`, `]`), localizar el rango exacto de `runs` textuales que componen el marcador, colocar el valor requisitado en el primer `run` del marcador (heredando su fuente, tamaño, color y negrita) y vaciar el texto residual (`""`) de los `runs` restantes del marcador sin tocar los `runs` ajenos ni las imágenes del párrafo.
   - En tablas dinámicas (`T1…Tm`), clonar con `copy.deepcopy(fila_molde._tr)` la fila patrón de datos tantas veces como registros verificados existan, rellenar cada celda conservando su estilo y eliminar la fila marcador original.
4. **Verificación automática post-requisitado:**
   Ejecutar siempre el verificador local y la compuerta de anonimato del orquestador:
   ```bash
   python3 extensions/DOC-04/scripts/auditar_plantilla_docx.py <entregable.docx> --molde <codigo.docx>
   python3 scripts/orquestador.py auditar <entregable.docx>
   ```
   Si el entorno cuenta con LibreOffice y `EDI-01` activo, complementar con renderizado visual a PNG (`render_docx.py`) para inspeccionar saltos de página y alineación de tablas al 100% de zoom.

---

## 4. Ciclo de vida, versionado semántico `X.Y.Z` y análisis de impacto del catálogo

El catálogo externo `plantillas_usuario/` adopta los estados de `DOC-02` (`MPRO_0201`):
`PROPUESTO → EN PRODUCCIÓN → EN REVISIÓN → VIGENTE → SUPERADO → RETIRADO`.

Cada ajuste sobre una plantilla del usuario incrementa su versión `X.Y.Z` bajo reglas objetivas:

| Dígito | Tipo de cambio | Supuestos que lo activan | Acciones obligatorias |
|---|---|---|---|
| `X.Y.Z` → tercer dígito (`1.0.1`) | **Menor (formal)** | Corrección ortotipográfica en texto fijo, ajuste menor de redacción fija o precisión de formato sin agregar, quitar ni redefinir campos `[1]…[N]`. | Actualizar `<codigo>.docx` / `<codigo>.md` y registrar fila en `CATALOGO_VERSIONES.md`. |
| `X.Y.0` → segundo dígito (`1.1.0`) | **Mayor / Funcional** | Alta o baja de campos `[1]…[N]`, nuevos bloques condicionales, cambio en columnas de tablas dinámicas, ajuste por reforma legal/regulatoria verificada o incorporación de una nueva plantilla relacionada al catálogo. | Ejecutar **Análisis de Impacto en Cascada** (identificar qué otras plantillas del catálogo comparten esos campos o dependen del mismo insumo maestro), actualizar las afectadas, correr pruebas A/B/Incompleto y pasar la versión previa a `SUPERADO`. |
| `X.0.0` → primer dígito (`2.0.0`) | **Estructural** | Cambio de identidad corporativa/razón social del titular, rediseño gráfico integral o sustitución completa de la arquitectura de campos del catálogo. | Análisis de impacto total del catálogo, validación integral y transición formal de la familia previa a `SUPERADO`. |

### Estructura mínima de `CATALOGO_VERSIONES.md` (en carpeta del usuario)

1. **Inventario activo:** código, título del formato, versión actual, estado `MPRO_0201`, archivos asociados (`.docx` + `.md`) y fecha de última verificación.
2. **Bitácora histórica de versiones:** versión anterior → versión nueva, fecha, clasificación (`Menor` / `Mayor` / `Estructural`), motivo del cambio, archivos modificados y responsable que validó.
3. **Matriz de impacto ante cambios:** cuando el usuario consulte qué piezas de su catálogo deben actualizarse ante un cambio normativo, contractual o administrativo, identificar exactamente qué campos `[k]` de qué plantillas `<codigo>` resultan afectados y cuál sería el salto de versión aplicable, sin alterar piezas no impactadas.
