# Auditoría hostil Word–PowerPoint

## Propósito

Impedir que una presentación derivada de Word contenga texto faltante, añadido, duplicado o
alterado. La auditoría es una compuerta de entrega: una diferencia de una palabra, cifra,
acento o signo de puntuación rechaza la diapositiva.

Este protocolo se aplica cuando el Word delimita diapositivas o el usuario exige igualdad
textual. Sustituye la edición libre: en este modo no se resume, parafrasea, completa, divide,
fusiona ni traslada contenido visible a notas.

## Contrato de correspondencia

El Word debe separar el contenido mediante párrafos `DIAPOSITIVA 1`, `DIAPOSITIVA 2`, etc.

- El marcador es metadato de control y no forma parte del texto esperado.
- Si el marcador incluye un título después de dos puntos, guion o raya, ese título sí forma
  parte del contenido esperado.
- Todo texto después de un marcador pertenece a esa diapositiva hasta el siguiente marcador.
- El texto anterior al primer marcador queda sin destino y provoca rechazo.
- Un marcador duplicado, una numeración discontinua o una diferencia en el número de
  diapositivas provoca rechazo.
- Párrafos y celdas de tabla se incluyen en la comparación.

No ignores fragmentos por considerarlos administrativos, repetitivos o poco importantes. Si
el Word contiene material que no debe aparecer, solicita autorización para corregir la fuente
o para producir una copia de control claramente documentada; nunca lo omitas silenciosamente.

## Qué debe coincidir

Compara por número de diapositiva:

- títulos, subtítulos, encabezados y cuerpo;
- palabras, cifras, porcentajes, fechas y fórmulas textuales;
- mayúsculas, minúsculas, acentos y signos de puntuación;
- repeticiones y cantidad de apariciones;
- orden de lectura del texto, salvo la excepción expresa para composiciones no lineales.

Solo normaliza diferencias de maquetación: saltos de línea, espacios consecutivos, espacios no
separables, guiones blandos y composición Unicode equivalente. Una viñeta aplicada como
formato no cuenta como carácter; una viñeta escrita dentro del texto sí cuenta.

La comparación sigue siendo estricta por defecto. Solo cuando el usuario ordene expresamente
que los títulos se muestren en mayúsculas, activa `--uppercase-titles`: el auditor convierte
el primer bloque de cada sección Word a mayúsculas antes de comparar y registra la excepción
en el informe. No aplica esa tolerancia al cuerpo, las cifras, la puntuación ni otros rótulos.

Si el Word contiene un título general antes de `DIAPOSITIVA 1` y el usuario confirma que debe
aparecer en la primera lámina, usa `--assign-preamble-to-slide-one`. Sin esa autorización, el
preámbulo continúa provocando rechazo por carecer de destino.

### Excepción controlada para composiciones no lineales

Una flecha ascendente, una balanza bilateral, un ciclo, una ruta o varios soportes distribuidos
pueden tener un orden visual legítimo distinto del recorrido geométrico automático de arriba a
abajo. En esos casos usa `--allow-nonlinear-layout` únicamente después de comprobar el render.
El auditor deja de exigir la secuencia geométrica global, pero conserva una comparación hostil
del inventario literal con multiplicidad: debe existir exactamente la misma cantidad de cada
palabra, cifra, acento y signo de puntuación en la diapositiva correspondiente. Una sola unidad
faltante, sobrante o duplicada mantiene el estado `RECHAZADO`.

Esta excepción no autoriza parafrasear, alterar el orden interno de una frase, trasladar texto
a otra diapositiva ni ocultarlo en notas o imágenes. Registra la excepción en el informe.

Los cuadros de notas no satisfacen contenido faltante. En este modo, el texto esperado debe
ser visible y editable en la diapositiva correspondiente.

## Prohibiciones durante la construcción

- No inventar títulos, etiquetas, transiciones, fuentes, folios o llamadas a la acción.
- No corregir ortografía, puntuación o estilo sin modificar primero la fuente autorizada.
- No acortar para hacer caber el texto; ampliar zonas, cambiar composición o pedir decisión.
- No trasladar texto a otra diapositiva.
- No duplicar una frase como rótulo y como cuerpo.
- No hornear texto en imágenes para eludir la comparación.

El diseño puede cambiar geometría, color, tipografía, jerarquía y posición. El contenido
textual no.

## Ejecución del auditor

Ejecuta desde la carpeta de la skill:

```bash
python3 scripts/auditar_texto_word_pptx.py \
  /ruta/al/original.docx \
  /ruta/a/la/presentacion.pptx \
  --report /ruta/al/informe-auditoria.md
```

El auditor devuelve:

- código `0`: aprobado;
- código `1`: diferencias textuales o revisiones visuales pendientes;
- código `2`: archivo inválido o configuración insuficiente.

El informe identifica por diapositiva los fragmentos faltantes y sobrantes y muestra el texto
esperado y encontrado. Corrige el PowerPoint, vuelve a ejecutar y conserva solo el informe
final aprobado junto con la presentación.

## Imágenes y objetos complejos

La extracción automática comprueba cuadros de texto, grupos y tablas nativas. Una imagen
puede ocultar texto rasterizado y una gráfica o SmartArt puede almacenar etiquetas en partes
que no se leen como cuadros ordinarios. Por ello, su presencia deja la auditoría pendiente.

1. Renderiza cada diapositiva a tamaño completo.
2. Inspecciona cada imagen y confirma que no contiene palabras, cifras, marcas ni restos
   tipográficos.
3. Compara manualmente todo texto visible en gráficas, SmartArt y objetos incrustados con la
   sección Word de la misma diapositiva.
4. Solo después de completar esas revisiones, repite con las constancias aplicables:

```bash
python3 scripts/auditar_texto_word_pptx.py \
  /ruta/al/original.docx \
  /ruta/a/la/presentacion.pptx \
  --report /ruta/al/informe-auditoria.md \
  --assign-preamble-to-slide-one \
  --uppercase-titles \
  --allow-nonlinear-layout \
  --confirm-images-without-text \
  --confirm-complex-objects-audited
```

No actives una constancia ni transformación por comodidad. Cada opción debe corresponder a
una revisión realizada o a una instrucción expresa. Si no puedes inspeccionar el objeto, el
estado sigue siendo `RECHAZADO`.

## Ciclo de reparación

1. Ejecutar la auditoría inicial.
2. Corregir cada faltante, sobrante, duplicado o alteración en la diapositiva indicada.
3. Repetir la comparación completa, no solo la diapositiva corregida.
4. Renderizar de nuevo para verificar ajuste y ausencia de texto rasterizado.
5. En composiciones no lineales, verificar además que la dirección visual esperada sea clara.
6. Entregar únicamente cuando el informe global muestre `APROBADO`.

Una coincidencia visual aproximada no basta. La compuerta se supera únicamente con igualdad
textual por diapositiva y con las revisiones visuales obligatorias concluidas.
