# Auditoría visual de una reedición humana

Usa este protocolo cuando el usuario entregue una presentación que corrigió manualmente y
solicite aprender de ella, compararla con una versión automática o convertir sus decisiones en
reglas para futuras presentaciones. La finalidad no es copiar una sola presentación, sino
distinguir principios transferibles, convenciones de una sección y excepciones locales.

## Jerarquía de autoridad

1. La petición expresa del usuario define el objetivo.
2. El documento fuente conserva la autoridad textual cuando rige fidelidad literal.
3. La reedición humana más reciente gobierna la intención visual, el encaje y la escala.
4. La plantilla institucional gobierna logotipo, formato, zonas protegidas e identidad.
5. Las reglas generales de la skill se aplican solo cuando no contradicen los niveles anteriores.

No conviertas una errata, un desbordamiento o una excepción de una sola lámina en patrón. La
autoridad visual no autoriza modificar el texto ni ocultar diferencias textuales.

## Dos modalidades de comparación

### A. Comparación pareada

Cuando existen la versión automática y la reedición humana:

- vincula cada diapositiva por número, título y contenido;
- compara tamaño, posición, proporción, recorte, rotación y capas de cada elemento;
- registra objetos eliminados, añadidos, agrupados, desagrupados o trasladados;
- distingue corrección estética, corrección de legibilidad, corrección semántica y cambio de
  estructura;
- cuantifica el cambio cuando pueda expresarse en coordenadas, porcentajes o puntos.

### B. Patrón oro sin versión previa

Si la versión automática ya no está disponible:

- declara expresamente la limitación;
- mide la reedición completa como patrón oro;
- compara solo contra datos verificables conservados —por ejemplo, número de láminas o reglas de
  la skill— y no inventes desplazamientos ni decisiones atribuidas al usuario;
- formula aprendizajes como «la reedición utiliza» o «el patrón observado indica», no como «el
  usuario movió» si no existe evidencia pareada.

## Inventario obligatorio por diapositiva

Mide y registra, como mínimo:

- tamaño y proporción del lienzo;
- título, función narrativa y sección;
- cantidad de palabras, párrafos y elementos textuales;
- cajas de título y cuerpo: `x`, `y`, ancho, alto, rotación, márgenes y alineación;
- fuente, tamaños mínimo, mediano y máximo, negrita, color y contraste;
- imágenes: rectángulo, relación de aspecto, recorte, resolución, transparencia y repetición;
- fondo de página, marco escénico, lienzo editorial y zonas protegidas;
- logotipo, folio, encabezado y pie: posición, tamaño y reserva de espacio;
- tablas, gráficas y diagramas: editabilidad, escala y relación con el texto;
- oclusiones, desbordamientos, elementos fuera del lienzo y avisos del validador;
- resultado en vista completa, mosaico y simulación de proyección.

Usa `scripts/medir_referencia_pptx.py` para obtener una primera medición reproducible. El JSON
generado no sustituye la inspección visual de cada lámina.

## Familias de maquetación que deben reconocerse

### A. Marco escénico con lienzo editorial

Personajes, objetos o arquitectura rodean un tablero, pantalla, documento o placa frontal
amplia. El lienzo es un solo portador. Dentro de él pueden vivir formas nativas de PowerPoint:
tarjetas, bandas, tablas, gráficas, cronologías o diagramas. Estas formas no son parches si
organizan la información y permanecen dentro del lienzo.

### B. Portadores individuales exactos

Cada peldaño, círculo, placa, bloque o página recibe un cuadro de texto transparente con la
misma forma, dirección y rotación. No se añaden tarjetas opacas para compensar un soporte mal
calculado.

### C. Portada o separador de sección

Predomina la identidad, un título breve y una escena simbólica. La escala y la respiración
visual son prioritarias. No se hereda automáticamente su densidad a las láminas de desarrollo.

### D. Evidencia contextual

Una imagen, tabla, gráfica o captura se mantiene junto a la explicación que le da sentido. Si
el origen la presenta como composición, consérvala unida cuando separar capas reduzca su escala,
proporción o inteligibilidad. No crees una diapositiva aislada solo para mostrar una miniatura.

### E. Página editorial de alta densidad

Para material legal, probatorio o documental `D05–D06`, una página blanca o muy limpia puede
ser superior a una escena. Reserva casi todo el lienzo para lectura, mantiene el logotipo y usa
jerarquías discretas. Es una decisión funcional, no una pérdida de estilo.

### F. Marco estructural repetible

Un escenario, fondo institucional o lienzo puede repetirse dentro de una sección si conserva la
misma función y la composición interna cambia. No lo confundas con reutilizar la misma
ilustración semántica para ideas diferentes.

## Taxonomía de repetición

- **Prohibida:** la misma ilustración semántica representa acciones o tesis distintas.
- **Controlada:** se repite un marco institucional o una arquitectura de sección, mientras
  cambian el contenido y la composición interna.
- **Obligatoria:** logotipo, folio, encabezado, franja corporativa o elemento maestro.
- **Accidental:** una imagen reaparece por copia sin motivo; debe corregirse.

Registra el hash del recurso, las diapositivas donde aparece y su función. Una coincidencia de
hash no es por sí sola un error.

## Calibración tipográfica por función

Deriva la escala de la presentación humana y de la distancia prevista. Como punto de partida
sin patrón más autoritativo:

| Función | Rango orientativo |
|---|---:|
| Título narrativo o de sección | 28–34 pt |
| Cuerpo principal de exposición | 14–18 pt |
| Etiqueta de diagrama, tabla o gráfica | 10.5–14 pt |
| Fuente, folio o nota visible | 9–11 pt |
| Detalle legal o probatorio no principal | 8–10 pt |

No conviertas 17 pt en mínimo universal. Tampoco permitas que 8–10 pt soporte el mensaje que
el público debe leer durante la exposición. Si la lámina es documental y se usará también como
material de consulta, identifícala como excepción y conserva una síntesis oral visible cuando
el texto fuente y la autorización lo permitan.

## Proporción, encaje y zonas protegidas

- Conserva la relación de aspecto de cada imagen; recorta solo si el área textual no se pierde.
- El texto debe quedar dentro de la cara útil del portador o del lienzo editorial.
- El título, el logotipo, el folio y el pie son zonas protegidas.
- Personajes, manos, objetos, bordes, conectores y sombras no pueden cruzar glifos.
- Un elemento parcialmente fuera del lienzo puede ser intencional; confirma visualmente antes
  de tratar un aviso automático como error.
- En diagonales, el cuadro hereda el ángulo cuando pertenece a un portador individual. El texto
  dentro de un gran lienzo frontal conserva la orientación de lectura del lienzo.

## Control del número de diapositivas

Cuando el origen, la plantilla o la reedición fija el número de láminas, consérvalo. No generes
automáticamente:

- láminas “de evidencia” con una imagen aislada;
- continuaciones vacías o casi vacías;
- duplicados de un gráfico en tamaño distinto;
- separaciones de capas pequeñas de una imagen compuesta;
- portadas intermedias no solicitadas.

Dividir solo está permitido si el usuario lo autoriza o si el modo editorial del proyecto lo
contempla y no rige fidelidad estructural.

## Proceso de auditoría

1. Renderiza todas las diapositivas y crea mosaicos por bloques manejables.
2. Extrae métricas de estructura, texto, imágenes, colores, fuentes y repeticiones.
3. Revisa cada lámina a tamaño completo; el mosaico no sustituye la lectura individual.
4. Clasifica cada lámina en una familia de maquetación y una densidad `D01–D06`.
5. Identifica patrones por sección, no solo promedios globales.
6. Separa principios generalizables, decisiones de sección y excepciones locales.
7. Produce un informe diapositiva por diapositiva y una síntesis de reglas aprendidas.
8. Actualiza la skill únicamente con principios generalizables confirmados.
9. Valida la skill y vuelve a revisar que sus reglas no sean contradictorias.

## Compuertas de aprobación

Una reedición solo puede usarse como patrón de aprendizaje cuando:

- todas sus diapositivas fueron renderizadas y revisadas;
- el texto fue auditado contra la fuente cuando corresponde;
- las imágenes conservan proporción y contexto;
- se identificaron las excepciones de lectura y no se universalizaron;
- se documentó la política de repetición;
- el informe diferencia hechos medidos, observaciones visuales e inferencias.

## Calibración observada: GSPA, 90 diapositivas

La reedición humana `Empresa_Socialmente_Responsable_GSPA_19_diapositivas.pptx` se usa como
caso de calibración, no como plantilla universal. Sus hechos medidos son:

- formato 16:9 de 13.333 × 7.5 pulgadas;
- 90 diapositivas reales, pese al nombre histórico del archivo;
- 78 fondos escénicos y 11 páginas editoriales limpias;
- 59 escenas de fondo únicas y nueve grupos de repetición controlada;
- logotipo principal repetido en 76 láminas, aproximadamente en `x=85.63 %`, `y=3.50 %`,
  `ancho=12.34 %`, `alto=4.39 %`;
- sección narrativa: mediana de 55 palabras, cuerpo de 16 pt y título de 28 pt;
- sección legal: mediana de 145 palabras y cuerpo de 10 pt, tratada como material documental;
- sección PLD: mediana de 66 palabras, cuerpo de 13.2 pt y título de 34.5 pt;
- uso dominante de azul marino, azul medio, dorado, vino, verde y blanco;
- figuras y objetos en el perímetro; texto y diagramas dentro de un gran lienzo central;
- evidencia y gráficas conservadas en contexto, sin láminas auxiliares vacías.

Estos valores enseñan que la tipografía debe calibrarse por función, que el marco estructural
puede repetirse y que una página editorial es válida para alta densidad. No autorizan usar 10 pt
como cuerpo principal ni copiar la paleta en proyectos sin relación institucional.

## Errores que este caso obliga a evitar

- aumentar artificialmente el número de diapositivas mediante láminas de apoyo;
- separar imágenes o capas del origen hasta volverlas pequeñas e irreconocibles;
- convertir «no repetir ilustraciones» en prohibición de repetir el marco institucional;
- imponer 17 pt a todo tipo de texto sin considerar tablas, diagramas y material legal;
- impedir formas nativas dentro de un lienzo editorial por confundirlas con parches;
- colocar texto fuera del tablero para conservar personajes decorativos;
- afirmar cambios precisos sin disponer de la versión previa para medirlos.
