# Plantilla de prompt de imagen

Andamio para generar la capa visual de una diapositiva híbrida. El modo predeterminado es
**16:9, sin texto rasterizado y con zonas calculadas para cuadros editables de PowerPoint**.
Rellena los campos entre corchetes y elimina las líneas que no apliquen.

## Preparación obligatoria

Antes de escribir el prompt:

1. mide el texto real y clasifica la lámina en `D01–D06`;
2. identifica la relación del contenido y la arquitectura `Cxx`;
3. selecciona `Exx` para contenido breve o `LTxx` para contenido extenso;
4. si el documento es mixto, selecciona un kit `KMxx` y su acabado `Sxx`;
5. calcula cada zona editable en coordenadas de la diapositiva;
6. modifica la geometría o divide la diapositiva —solo cuando esté permitido— si el texto no
   cabe; nunca lo hornees ni reduzcas a un tamaño ilegible.

## Andamio predeterminado: PowerPoint editable

```text
Use case: productivity-visual
Asset type: structural illustration for a professional 16:9 PowerPoint slide
Primary request: Create a complete slide-ready carrier scene about [SUBJECT]. This is not a
background. Its subjects, objects and blank panels must visibly organize the message and remain
useful after native PowerPoint text boxes are placed over them.

LAYOUT
[Describe the exact geometry in English: number of carriers, positions, reading order,
connections and hierarchy. Specify the Cxx architecture and whether the family is Exx or LTxx.]

TEXT DENSITY AND CARRIER SHARE
Mode [Dxx]: [word/character load and block count]. Reserve [percentage] of the usable slide area
for clean text carriers and [percentage] for scene, people and atmosphere.

EDITABLE OVERLAY ZONES
[For every text box, describe position, width, height, alignment and relationship to the
surrounding panel, icon or connector. Each zone must be a visible physical surface belonging to
the scene: card, panel, platform, step, circle, frame, module or object face.]

BACKGROUND AND SCENE
[Family A] Transparent or clean light background; no full-canvas decorative backdrop.
[Family B] Deep navy #0E2A4E background; blank light carriers with strong contrast.
[Family C] Restrained editorial scene; the carriers, not the environment, dominate.
[Describe what the people or objects do: carry, build, review, connect, filter, protect,
compare or decide.]

STYLE AND FINISH
[Sxx / KMxx]. Clean professional editorial illustration with subtle depth, disciplined grid,
consistent materials, controlled shadows, crisp silhouettes and generous breathing room.

COLOR
[Palette from the selected Sxx or KMxx. Use semantic accents only when they encode meaning.]

ICONS
[List only functional icons and their positions. Icons must not contain letters or numbers.]

NO TEXT IN IMAGE
No words, letters, numbers, formulas, dates, labels, headings, captions, placeholder text,
logos, watermarks or typographic marks anywhere in the image. Keep every editable overlay zone
completely blank, smooth, calm and high-contrast.

DO NOT INCLUDE
No slide title, slide number, module, session, header, footer, logo, watermark or brand mark.
No generic robots, humanoid AI figures, emojis, mascots, stock-photo poses, childish style,
neon, cyberpunk, ornamental 3D, glow, lens flare, rainbow gradient, fake UI, dashboard, button,
fake chart, decorative outer frame, empty scenery or unrelated copy space. Do not place texture,
icons, characters, connectors or shadows inside any reserved text zone.
```

## Ajustes por familia

**Familia A.** Repite la transparencia o el fondo limpio al inicio y al final. Si vuelve con un
panel de color no solicitado, añade: `Isolated carrier diagram on transparent background, PNG
with alpha channel, no backdrop whatsoever.`

**Familia B.** Especifica tarjetas claras, lisas y vacías. El contraste del texto se resolverá
después en PowerPoint.

**Familia C.** Describe el ambiente en dos frases como máximo. Dedica la mayor parte del prompt
a los portadores y a la acción; si el escritorio o la fotografía dominan, regenera.

**Familias LT.** Exige que el macropanel o las columnas estén casi planos a cámara y ocupen la
proporción prevista por `D04–D06`. La escena vive en bordes, base o esquinas sin invadir lectura.

## Cálculo de zonas, no presupuesto raster

La cantidad de texto determina el tamaño de los portadores, no la cantidad de palabras que el
generador debe dibujar.

| Modo | Arquitectura inicial | Regla de generación |
|---|---|---|
| `D01` | un mensaje focal | escena dominante con un portador claro |
| `D02` | dos a cuatro bloques breves | varios portadores conectados |
| `D03` | bloques medios o párrafos breves | elegir `E` o `LT` por estructura |
| `D04` | un panel dominante o dos columnas | `LT`, paneles por encima del ambiente |
| `D05` | página editorial, bandas o comparación | `LT`, lectura dominante |
| `D06` | fidelidad literal de alta densidad | `LT`, máxima superficie limpia |

El texto se inserta después con tipografía nativa y se aprueba mediante renderizado. Si una zona
no alcanza, cambia geometría, densidad o número de diapositivas cuando esté autorizado.

## Protocolo de regeneración

| Falla observada | Refuerzo |
|---|---|
| Apareció texto o pseudotexto | Repite `NO TEXT IN IMAGE` al inicio y al final; simplifica detalles |
| Apareció un fondo decorativo | `This is a carrier scene, not a background; no empty scenery.` |
| Panel insuficiente | Aumenta su proporción y reduce ambiente o personajes |
| Cuadro editable quedaría flotando | Convierte la zona en un objeto físico de la escena |
| Iconos o sombras invaden la zona | Declara un rectángulo interior totalmente limpio |
| Composición repetida | Cambia `Cxx`, no solo el color |
| Perspectiva deforma texto largo | Pide paneles frontales, casi planos a cámara |

Máximo tres intentos con la misma estructura. Después cambia `Cxx`, `Exx` o `LTxx`; no repitas
el mismo prompt esperando un resultado distinto.

## Excepción: imagen final no editable

Solo si el usuario solicita expresamente una imagen autónoma con texto incorporado puede
añadirse `TEXT TO RENDER`. Enumera allí las cadenas exactas en español, prohíbe toda palabra no
listada y revisa acentos. Esta excepción no se usa para construir PowerPoint editable, no
sustituye el auditor Word–PowerPoint y nunca se activa por conveniencia técnica.
