# Mini-Skill PRE-02 · Edición y Fidelidad de Presentaciones PowerPoint

Esta ficha se carga bajo demanda cuando el encargo requiere crear, rediseñar, auditar o corregir presentaciones PowerPoint (`.pptx`), preservar una presentación aprobada, convertir documentos Word a diapositivas con fidelidad literal o aplicar el sistema visual ejecutivo **PENO-01**.

## 1. Rutas de entrada y activación

- **Instrucciones completas del módulo:** [MODULO.md](../extensions/PRE-02/visuales-diplomado-ia/MODULO.md)
- **Guía de recuperación de recursos visuales (128 archivos):** [carga-PRE-02.md](carga-PRE-02.md)
- **Activación desde el orquestador:**
  - Sólo instrucciones, catálogos JSON y scripts locales:
    ```bash
    python3 scripts/orquestador.py activar PRE-02
    ```
  - Con paquete visual completo extraído y validado (plantillas, imágenes, muestras):
    ```bash
    python3 scripts/orquestador.py activar PRE-02 --incluir-recursos-pre02
    ```
    *(O directamente mediante `python3 scripts/preparar_PRE02.py`).*

## 2. Reglas de coordinación y ejecución

1. **Coordinación con especialidad sustantiva y PRE-01:**
   - Coordinar `PRE-01` para la estructuración general de presentaciones y `PRE-02` para edición visual, composición, texto editable, fidelidad literal y preservación quirúrgica.
   - Mantener siempre al especialista jurídico, fiscal, municipal, asegurador o académico como responsable del contenido de fondo.
   - Aplicar el encargo actual del usuario por encima de valores predeterminados; no exigir una nueva autorización si el usuario ya pidió generar o editar el archivo.

2. **Reglas operativas obligatorias:**
   - **Preservación de fuentes:** Conservar los archivos fuente originales y entregar una copia editada, salvo autorización expresa de reemplazo.
   - **Fidelidad literal Word–PowerPoint:** En modalidad de fidelidad literal, conservar íntegro el texto visible y editable por diapositiva y ejecutar la auditoría Word–PowerPoint (`extensions/PRE-02/visuales-diplomado-ia/scripts/auditar_texto_word_pptx.py`); nunca resumir ni trasladar contenido sustantivo a las notas del orador.
   - **Preservación quirúrgica de diseño aprobado:** Si el usuario pide conservar un diseño aprobado, modificar únicamente las partes solicitadas y comparar todos los renders, además del texto y los datos de gráficas (`extensions/PRE-02/visuales-diplomado-ia/scripts/auditar_pptx_pptx.py`).
   - **Catálogos generativos:** Usar las 50 familias escénicas (`E01-E50`), las 20 familias de texto grande (`LT01-LT20`) y los 8 kits mixtos profesionales como catálogos de diseño. Las 2,500 combinaciones son posibilidades generativas de composición y estilo (`50x50`), no 2,500 imágenes pre-generadas incluidas.
   - **Validación del sistema visual:** Ejecutar `scripts/validar_sistema_visual.py` dentro de la copia completa preparada de `visuales-diplomado-ia` tras modificar el módulo. No presentar la validación estructural del sistema como sustituto de la auditoría visual sobre el archivo `.pptx` entregable.
   - **Compuerta de anonimato:** Verificar antes de entregar que ninguna diapositiva ni nota contenga referencias a `PRE-02`, `PENO-01`, `MRCI` o códigos de familias (`LT01`, `E01`, `D01`, etc.).
