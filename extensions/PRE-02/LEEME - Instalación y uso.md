# Skill Edición de Presentaciones PowerPoint

Paquete portátil de la skill `visuales-diplomado-ia`.

Esta skill transforma documentos Word, PDF, PowerPoint, hojas de cálculo y texto en
presentaciones modernas. También permite crear composiciones híbridas: la imagen aporta la
estructura gráfica y el texto se coloca encima como cuadros editables de PowerPoint. Incluye
un auditor hostil que compara el Word y el PowerPoint diapositiva por diapositiva para detectar
cualquier texto faltante, añadido, duplicado o alterado. También incorpora una biblioteca
generativa de 50 familias escénicas portadoras por 50 composiciones, con 2,500 combinaciones
posibles. Las familias no son fondos: usan objetos, personas, recorridos y superficies físicas
para sostener los cuadros de texto editables. La versión actual también incorpora seis modos
de densidad textual (`D01–D06`) para adaptar la proporción de imagen y espacio de lectura a
mensajes breves, textos medios, textos largos y contenido de fidelidad literal.
También incluye veinte familias especializadas `LT01–LT20` para texto grande y un selector que
propone tres familias razonadas a partir del contenido de cada diapositiva.
La versión actual incorpora además ocho kits mixtos `KM01–KM08` para combinar láminas breves y
extensas sin perder paleta, materiales, iluminación, figuras ni tipografía.
La versión 7 añadió la **Plantilla Escultórica Negro y Oro**, identificada como `PENO-01`:
doce composiciones con personajes blancos y dorados sobre transparencia, objetos de color,
fondo negro, franja dorada y cuadros de texto nativos colocados dentro de los elementos.
La versión 8 añadió encuadre geométrico por imagen: cada cuadro queda dentro del margen seguro
de su soporte y hereda su ángulo cuando la imagen es diagonal. PENO-01 usa Arial, títulos en
MAYÚSCULAS y negritas, tamaño calculado por superficie y énfasis semánticos en rojo, azul,
verde o negro brillantes. También prohíbe repetir una escena dentro de una presentación y
añade al auditor opciones explícitas para títulos en mayúsculas y preámbulos asignados.
La versión 9 incorpora una compuerta de coherencia semántica: antes de elegir una imagen se
registran idea, acción, relación, metáfora visual y razón de correspondencia. Se rechazan las
escenas que solo combinan con la paleta, que muestran personajes decorativos o que podrían
acompañar indistintamente tres temas no relacionados.
La versión 10 incorpora concordancia morfológica y encaje: cada cuadro debe ocupar la cara útil
de su módulo, peldaño, círculo, bloque, placa, tramo o página, seguir su dirección y mantener
visibles personajes, bordes, conectores y recorridos. Se prohíben las tarjetas flotantes que
ocultan la ilustración o uniforman formas distintas. El auditor hostil distingue además el
contenido literal del orden geométrico automático: en rutas ascendentes, ciclos, balanzas o
soportes distribuidos puede autorizarse el modo no lineal, que sigue rechazando cualquier
palabra, cifra o signo faltante, sobrante o duplicado.
La actualización transportable del 24 de septiembre de 2026 incorpora el modo de
**preservación quirúrgica de PowerPoint**. Cuando existe una presentación aprobada o corregida
manualmente, la skill conserva como fuente de verdad sus textos, imágenes, proporciones,
posiciones, capas, rotaciones, recortes y logotipos. También incorpora una auditoría hostil
PPTX contra PPTX para comprobar que la reedición no agregue, suprima, sustituya ni reordene
contenido sin autorización.
Todo el sistema está normalizado a formato 16:9. Las imágenes se generan sin palabras y todo
el contenido semántico permanece editable dentro de PowerPoint.

## Contenido del paquete

- `visuales-diplomado-ia/SKILL.md`: instrucciones principales.
- `visuales-diplomado-ia/agents/openai.yaml`: nombre y descripción visibles en Codex.
- `visuales-diplomado-ia/references/`: reglas de diseño, extracción, diagramas, generación de
  imágenes, texto editable y auditoría.
- `visuales-diplomado-ia/scripts/auditar_texto_word_pptx.py`: auditor textual estricto.
- `visuales-diplomado-ia/scripts/auditar_pptx_pptx.py`: compara una presentación fuente con la
  reedición y detecta diferencias de texto, imágenes y estructura por diapositiva.
- `visuales-diplomado-ia/scripts/construir_prompt_50x50.py`: selector y constructor de prompts
  para las 2,500 combinaciones visuales.
- `visuales-diplomado-ia/scripts/sugerir_grupos_texto_grande.py`: selecciona tres familias
  `LTxx` razonadas para una lámina extensa.
- `visuales-diplomado-ia/scripts/planificar_kit_mixto.py`: propone por diapositiva densidad,
  biblioteca `E`/`LT`/`NATIVA`, familias, composiciones y acabado.
- `visuales-diplomado-ia/scripts/validar_sistema_visual.py`: comprueba catálogos, claves,
  enlaces, archivos obligatorios y coherencia 16:9 antes de transportar la skill.
- `Muestras escenas portadoras/`: ejemplos de sistema solar con tarjetas, obreros blancos
  portadores y escalera financiera ascendente.
- `Muestras texto largo/`: seis estructuras visuales con paneles limpios para contenido extenso.
- `Biblioteca texto grande - 20 grupos/`: veinte maestros, catálogo visual y guía de selección.
- `Kits mixtos profesionales/`: mapa y reglas para combinar `E01–E50` con `LT01–LT20`.
- `visuales-diplomado-ia/assets/plantillas/PENO-01/`: PowerPoint base, vista general y doce
  recursos PNG con canal alfa de la Plantilla Escultórica Negro y Oro.
- `visuales-diplomado-ia/references/plantilla-escultorica-negro-oro.md`: reglas de selección,
  densidad, generación y control de la familia `PENO-01`.
- `visuales-diplomado-ia/references/coherencia-semantica-imagen-texto.md`: compuerta que obliga
  a representar la idea, acción y relación de cada diapositiva.
- `visuales-diplomado-ia/references/concordancia-morfologica-y-encaje.md`: cálculo de contorno,
  capacidad, rotación, oclusión y pertenencia de cada cuadro editable.
- `visuales-diplomado-ia/references/preservacion-quirurgica-pptx.md`: reglas para reeditar un
  PowerPoint aprobado sin alterar su contenido ni su composición validada.

## Instalar en otra computadora

1. Descomprime el archivo ZIP.
2. Copia la carpeta completa `visuales-diplomado-ia` en la carpeta de skills personales:
   - macOS o Linux: `~/.codex/skills/`
   - Windows: `%USERPROFILE%\.codex\skills\`
3. Conserva exactamente el nombre de carpeta `visuales-diplomado-ia`.
4. Cierra y vuelve a abrir Codex.
5. Ejecuta `python3 scripts/validar_sistema_visual.py` dentro de la skill. Debe responder
   `APROBADO` antes de utilizar o compartir la copia instalada.

La ruta final debe terminar así:

```text
.codex/
└── skills/
    └── visuales-diplomado-ia/
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```

## Uso

Invócala expresamente escribiendo:

```text
$visuales-diplomado-ia
```

Después agrega tu solicitud y adjunta el Word, PDF, PowerPoint u otro archivo fuente.

Para pedir directamente la nueva familia escribe cualquiera de estas fórmulas:

```text
Usa la Plantilla Escultórica Negro y Oro.
Usa PENO-01.
Usa la plantilla de personajes blancos y dorados.
```

El nombre recomendado para compartirla y volver a solicitarla es **Plantilla Escultórica
Negro y Oro — PENO-01**.

Ejemplo:

```text
$visuales-diplomado-ia transforma este Word en una presentación profesional. Genera gráficos
sin texto y coloca todo el contenido en cuadros editables dentro de sus espacios.
```

Si el Word contiene apartados `DIAPOSITIVA 1`, `DIAPOSITIVA 2`, etc., la skill activa el modo
de fidelidad literal. En ese modo, el archivo final no se entrega hasta que el auditor confirme
que no falta ni sobra texto en ninguna diapositiva.

Cuando la lectura visual no sea lineal, el auditor puede ejecutarse con
`--allow-nonlinear-layout`. Esta opción no flexibiliza el contenido: exige un inventario literal
idéntico con la misma multiplicidad y solo evita que una ruta de abajo hacia arriba sea
confundida con una omisión.

Cuando solicites plantillas o variedad visual, la skill elige primero una familia escénica
`E01–E50`, después una composición `C01–C50` y finalmente un acabado `S01–S50`. Las imágenes
se generan conforme se necesitan, sin incrustar texto, y después reciben cuadros editables
dentro de PowerPoint sobre paneles, círculos, peldaños, plataformas u otros objetos visibles.

Para textos extensos, la skill calcula además la densidad `D01–D06` y amplía la superficie útil
de lectura. Puede usar un macropanel, dos columnas físicas, bandas documentales, una página
editorial o una estructura de fidelidad literal. El conteo de palabras sirve como diagnóstico
inicial; el ajuste final se confirma con tipografía, saltos de línea y renderizado real. No se
reduce el texto a tamaños ilegibles. Si el contenido literal no cabe, sólo se divide en más
diapositivas cuando el usuario lo autoriza.

Cuando una lámina se clasifica como `D04–D06`, la skill analiza su relación narrativa y ofrece
tres opciones `LTxx` con su razón, geometría y número de cuadros. Si no se elige una, utiliza
la primera recomendación y continúa la presentación.

Cuando un documento contenga textos cortos y largos, la skill elige un kit rector `KMxx`, usa
familias `E` para `D01–D02`, decide por estructura en `D03` y usa familias `LT` para `D04–D06`.
El número de láminas de cada tipo depende del contenido y no de una cuota predeterminada.

El planificador mixto acepta una lista JSON de diapositivas y genera un plan visual inicial:

```text
python3 scripts/planificar_kit_mixto.py --input diapositivas.json --output plan-visual.json
```

El resultado se revisa con el texto y el render final; no reemplaza la decisión editorial.

En PENO-01, cada zona editable registra posición, tamaño y rotación. El cuadro completo debe
permanecer dentro del soporte. Si la imagen muestra un panel diagonal, el texto adopta el
mismo ángulo; cuando existe perspectiva fuerte, se usa otro panel o se genera una escena
nueva. Ninguna imagen se repite aunque la presentación exceda doce diapositivas.

Antes de maquetar, cada imagen debe superar la compuerta de coherencia semántica. La escena no
se aprueba por verse profesional: debe mostrar la acción o relación del texto y el manifiesto
debe explicar por qué corresponde. Si no existe una opción adecuada, se genera una nueva.

Una vez aprobada la imagen, cada zona supera la compuerta morfológica. Los cuadros siguen la
forma y recorrido del soporte, dejan aire y no cubren figuras o símbolos. Si el texto literal
no cabe, se cambia la arquitectura; no se fuerza una tarjeta por encima de la escena.

Cuando el archivo de partida sea un PowerPoint ya corregido o aprobado, solicita el modo de
preservación quirúrgica. La verificación recomendada es:

```text
python3 scripts/auditar_pptx_pptx.py PRESENTACION_FUENTE.pptx PRESENTACION_REEDITADA.pptx
```

La entrega se rechaza si el auditor encuentra texto faltante o adicional, cambios no
autorizados en las imágenes, deformaciones, desplazamientos o elementos fuera de la diapositiva.

## Requisitos prácticos

- Usa una instalación de Codex que admita skills personales.
- Para crear el archivo final se necesitan las capacidades de presentaciones de PowerPoint.
- Para generar ilustraciones o fondos originales se necesita una herramienta de generación de
  imágenes disponible en la instalación de destino.
- El auditor requiere Python con `python-docx` y `python-pptx`; el entorno de documentos y
  presentaciones de Codex normalmente ya los incluye.

## Controles superados por esta versión

- integridad de 50 familias, 50 composiciones, 50 acabados, 6 densidades, 20 familias largas
  y 8 kits mixtos;
- PowerPoint base `PENO-01` con doce diapositivas y doce PNG con canal alfa;
- reglas de Arial, títulos en mayúsculas, rotación solidaria, márgenes seguros, color semántico
  y escenas no repetidas;
- compuerta de coherencia semántica con prueba sin texto, prueba de intercambio y prueba
  contrafactual de tres temas;
- compuerta de concordancia morfológica con pruebas de contorno, oclusión, pertenencia, forma,
  dirección, distancia y elegancia;
- correspondencia de referencias entre catálogos;
- enlaces internos y archivos obligatorios;
- constructor 50 × 50 y selector de texto largo;
- planificador de presentaciones mixtas;
- auditor hostil probado con un caso idéntico, uno no lineal y otro con una omisión deliberada.
- auditoría PPTX contra PPTX y reglas de preservación quirúrgica para presentaciones aprobadas.

La carpeta no incluye los documentos Word o PowerPoint usados como fuente durante otros
trabajos.
