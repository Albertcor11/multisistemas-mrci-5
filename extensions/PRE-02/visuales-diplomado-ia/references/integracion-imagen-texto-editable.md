# Integración de imágenes con texto editable en PowerPoint

## Objetivo

Construir una composición híbrida: el gráfico raster aporta identidad, iconos, marcos,
conectores y profundidad; los cuadros de texto nativos de PowerPoint aportan todo el contenido
que el usuario necesita modificar. El resultado debe leerse como una sola pieza, no como una
imagen decorativa acompañada por párrafos.

La imagen debe ser una **escena portadora**, no un fondo. Sus personajes, objetos y recorridos
deben sostener físicamente paneles, círculos, peldaños, marcos, módulos o plataformas donde se
colocará el texto editable. Lee [escenas-portadoras-de-texto.md](escenas-portadoras-de-texto.md)
antes de generar una biblioteca o una diapositiva ilustrada.

Lee también [coherencia-semantica-imagen-texto.md](coherencia-semantica-imagen-texto.md) antes
de elegir la escena. Una superficie con espacio suficiente no es válida si su actividad,
objeto principal o relación contradicen o no explican el texto.

Después lee
[concordancia-morfologica-y-encaje.md](concordancia-morfologica-y-encaje.md). La caja debe
encajar en la cara útil del soporte y conservar su forma, dirección y elementos esenciales;
estar simplemente superpuesta sobre la imagen no es suficiente.

Cuando la escena ya tenga o deba generar espacios físicos para texto, lee también
[protocolo-portadores-exactos.md](protocolo-portadores-exactos.md). El mapa de portadores es un
contrato: no se corrige una imagen inadecuada añadiendo tarjetas sobre ella.

El contrato estricto corresponde a portadores individuales. Si la imagen contiene una gran
pantalla, pizarrón, documento o tablero frontal, ese elemento puede operar como un único
**lienzo editorial**. Dentro de él se permiten formas, tablas, gráficas y diagramas nativos de
PowerPoint que organicen la información, siempre dentro del área útil y sin cubrir la escena.

Cuando el contenido exceda unas pocas líneas, lee
[texto-largo-en-escenas.md](texto-largo-en-escenas.md) y selecciona un modo de densidad
`D01–D06`. La cantidad de texto cambia la proporción entre paneles y escena.

Si el documento combina láminas breves, medias y extensas, selecciona un kit `KM01–KM08`
con [modo-mixto-kit-profesional.md](modo-mixto-kit-profesional.md). El kit no fija una
plantilla única: mantiene paleta, acabado, personajes y materiales mientras alterna la
biblioteca escénica `E01–E50` y la biblioteca editorial `LT01–LT20`.

## Cuándo aplicar este modo

Úsalo cuando el usuario solicite cualquiera de estos resultados:

- insertar gráficos o ilustraciones dentro de PowerPoint;
- escribir texto editable dentro de los espacios de una imagen;
- conservar una estética visual generada, pero poder cambiar títulos, etiquetas o cifras;
- transformar un Word u otra fuente, sin importar su cantidad de diapositivas, en una
  presentación visual con texto modificable.

No lo uses para convertir una tabla o gráfica de datos en captura. La evidencia cuantitativa
permanece como tabla o gráfica nativa, aunque se coloque dentro de un marco visual raster.

## 1. Analizar el contenido antes de elegir la imagen

Para cada diapositiva registra:

1. mensaje que debe comprenderse de inmediato;
2. título, encabezados, explicaciones, cifras y fuente;
3. cantidad de bloques y relación entre ellos;
4. longitud real de cada texto y líneas previstas;
5. tratamiento: imagen estructural, texto editable, gráfica nativa, tabla nativa o notas;
6. rectángulo disponible para la imagen y rectángulos previstos para cada texto.

No selecciones ni generes el gráfico antes de completar este análisis. El visual debe adaptarse
al contenido; el contenido no se comprime arbitrariamente para adaptarse a una imagen elegida
por estética.

## 2. Elegir el tipo de imagen por el significado

| Relación del contenido | Imagen estructural preferida |
|---|---|
| Secuencia o transformación | flujo, estaciones, cadena o etapas conectadas |
| Decisión o bloqueo | puertas, bifurcaciones, semáforo o zonas de detención |
| Tres niveles de intervención | continuo verde, ámbar y rojo con paneles separados |
| Fundamentos jurídicos o conceptuales | pilares, columnas o tarjetas sobre una base común |
| Componentes de un sistema | núcleo central con paneles conectados |
| Comparación | campos paralelos o paneles simétricos |
| Clasificación | zonas, cuadrantes o categorías diferenciadas |
| Caso con datos | escena o metáfora a un lado y marco para gráfica nativa al otro |
| Métricas | marcos para fórmulas, gráfica nativa y rangos destacados |
| Cronograma | línea temporal con barras de fase vacías |
| Conclusión | bandas jerarquizadas y una pregunta final |
| Fuentes | filas o fichas amplias con iconografía jurídica o académica |

Elige una composición dominante por diapositiva. Varía la geometría entre láminas, pero
mantén paleta, iconografía, iluminación, profundidad y tipografía coherentes.

### Enrutamiento obligatorio por densidad

- `D01–D02`: familia escénica `Exx` + composición `Cxx` + acabado `Sxx`.
- `D03`: usa `E` si contiene bloques independientes; usa `LT` si contiene párrafos, bandas de
  lectura o varios apartados desarrollados.
- `D04–D06`: familia editorial `LTxx` + acabado `Sxx`; reduce la escena y aumenta los paneles.
- Presentación mixta: selecciona primero `KMxx` y limita las elecciones `E`, `LT` y `S` a las
  recomendadas por el kit, salvo incompatibilidad semántica documentada.
- Datos: usa `NATIVA` para tablas y gráficas, incluso dentro de un marco del kit.

## 3. Calcular las zonas de texto

Calcula cada zona a partir del texto real y de la diapositiva final, no de una miniatura.

- Reserva primero título, folio, logotipo y fuentes visibles.
- Determina cuántas cajas necesita el mensaje. Un encabezado y su explicación pertenecen al
  mismo contenedor visual, aunque puedan ser dos cuadros de PowerPoint.
- Sin una plantilla o reedición más autoritativa, planea cuerpo principal de 14–18 pt,
  etiquetas de 10.5–14 pt y fuentes de 9–11 pt; procura 17 pt o más cuando el volumen y el uso
  presencial lo permitan. Reserva 8–10 pt para detalle legal o probatorio no principal. No
  reduzcas la letra para rescatar una composición fallida.
- Estima líneas con la tipografía, tamaño, ancho y márgenes interiores previstos; confirma la
  estimación mediante renderizado. Una fórmula matemática no sustituye la prueba visual.
- Deja aire alrededor del texto. La caja no debe tocar iconos, bordes, conectores ni sombras.
- Si el contenido no cabe en dos o tres líneas legibles, condensa sin cambiar el sentido,
  traslada detalle a notas o divide la lámina cuando esté permitido. Si rige fidelidad literal,
  usa `D05` o `D06` y no condenses, traslades ni dividas sin autorización.

Registra las zonas en coordenadas de la diapositiva: `x`, `y`, `ancho`, `alto`, alineación,
tamaño inicial y color. Estas coordenadas guían tanto el prompt de la imagen como la
construcción del PowerPoint.

### Contrato previo de portadores

Antes de generar la imagen, registra la cantidad exacta de soportes y asigna cada unidad de
contenido a uno de ellos. Para cada portador conserva: identificador, tipo, posición, área útil,
margen seguro, rotación, capacidad en líneas, tamaño mínimo, color de superficie, color de
texto y zonas protegidas. El prompt debe pedir exactamente esa cantidad y prohibir placas o
espacios vacíos adicionales.

Después de aprobar la imagen, sus caras útiles son autoritativas. Si un soporte queda bajo la
franja de título, no permite el mínimo legible, presenta perspectiva difícil, recibe sombras o
figuras sobre el área de lectura, o requiere una tarjeta opaca para que el texto funcione,
rechaza la imagen y regenera. No improvises una geometría distinta durante la maquetación.

### Margen seguro, ángulo y encuadre

El rectángulo de cada cuadro de texto, incluidos sus márgenes interiores, debe quedar dentro
del rectángulo de la imagen y del polígono visualmente útil del soporte. No basta con que el
centro del cuadro caiga sobre el panel. Reserva una holgura interior proporcional al tamaño:
como referencia inicial, 4–7% por lado para paneles rectos y 7–10% para círculos, páginas,
placas estrechas o soportes inclinados. Confirma la holgura en el render final.

Registra también `rotación` para cada zona. Un marco, placa, peldaño, tramo, flecha o página
inclinado exige un cuadro con el mismo ángulo visual. Mantén título, cuerpo y énfasis como un
solo grupo angular cuando pertenezcan a la misma superficie. Si la perspectiva exige cizalla,
deformación trapezoidal o varias inclinaciones simultáneas, PowerPoint no puede resolverla con
un cuadro plano: usa otra superficie casi frontal o regenera la imagen. Para textos largos,
rechaza soportes con más de 8° de inclinación salvo que el tamaño proyectado siga siendo
cómodo; para etiquetas breves pueden admitirse ángulos mayores tras renderizar.

En PENO-01 usa Arial. Calcula el tamaño con área útil, caracteres, saltos, jerarquía y ángulo.
Los títulos de diapositiva se muestran en MAYÚSCULAS y negritas. En fidelidad literal, una
mayúscula de título solo puede apartarse del Word cuando el usuario lo haya autorizado de
forma expresa y el auditor registre esa transformación; cuerpo, cifras y puntuación siguen
siendo literales.

Aplica énfasis únicamente a palabras o frases existentes:

- rojo brillante `#FF2B2B`: alerta, prohibición, detención, perjuicio o prioridad crítica;
- azul brillante `#00A8FF`: datos, algoritmo, tecnología, estructura o ruta analítica;
- verde brillante `#39E75F`: garantía, validación, corrección, control o resultado favorable;
- negro brillante `#050505`: máxima autoridad o contraste sobre superficies marfil, doradas,
  amarillas o claras.

No repitas una imagen dentro de la presentación. La repetición de fondo sólido, franja o
logotipo institucional no cuenta como repetición de escena. Si el inventario de escenas se
agota, genera una variante nueva con otra actividad, composición y silueta; no recortes,
voltees ni recolores la misma imagen para simular variedad.

## 4. Generar o limpiar la imagen estructural

La imagen debe contener exclusivamente elementos visuales:

- paneles, tarjetas, círculos, bandas o espacios negativos;
- iconos con función semántica;
- conectores, flechas, caminos o divisores;
- fondos, sombras, bordes, profundidad y color.

Los paneles no pueden aparecer como tarjetas de interfaz flotantes sin relación con la escena.
Intégralos como objetos reales: un planeta junto a su placa orbital, un obrero que carga un
marco, un peldaño de una flecha ascendente, una bandeja de evidencia, un tramo de puente o una
cara frontal de un módulo.

La imagen no debe contener palabras, letras, cifras, fórmulas, fechas, títulos, folios,
marcas, logos ni texto de muestra. En el prompt exige zonas completamente limpias y con el
tamaño necesario para los cuadros calculados.

Si existe una imagen adecuada que contiene texto, úsala como objetivo de edición: elimina
todo el texto y conserva la composición, iconos, paneles, conectores, proporciones y paleta.
Inspecciona el resultado. No aceptes restos, sombras tipográficas, letras parciales ni espacios
rellenados con texturas que reduzcan la legibilidad.

## 5. Calcular tamaño, ajuste y recorte de la imagen

- Define el rectángulo final de la imagen antes de insertarla.
- Conserva su proporción. Nunca la estires horizontal o verticalmente.
- Usa `contain` cuando deban verse todos los paneles o evidencia visual.
- Usa `cover` solo cuando el recorte esté previsto y no elimine iconos, paneles o zonas de
  texto.
- Una imagen a sangre completa debe soportar el título y los cuadros superpuestos sin perder
  contraste. Si no lo permite, reduce la imagen o reserva una franja nativa para el título.
- Verifica que la resolución sea suficiente para el tamaño proyectado y que la transparencia
  funcione sobre el fondo elegido.

## 6. Construir la capa editable en PowerPoint

1. Inserta primero la imagen y bloquea conceptualmente su posición.
2. Crea encima cuadros de texto nativos para títulos, encabezados, explicaciones, cifras,
   fórmulas, fechas, fuentes y folios.
3. Ajusta cada cuadro a la zona calculada y usa relleno y línea transparentes. Si el contraste
   no basta, cambia el color del texto o regenera el soporte; no añadas una tarjeta de interfaz.
4. Alinea el texto con la geometría real del panel, no solo con la diapositiva.
5. Conserva márgenes interiores y altura suficiente para negritas, acentos y saltos de línea.
6. Mantén tablas y gráficas como objetos nativos editables dentro de los marcos previstos.
7. Añade notas del presentador y fuentes sin hornearlas en la imagen.
8. Registra `Dxx`, `Exx-Cxx` o `LTxx`, `Sxx` y `KMxx` en el manifiesto de la diapositiva.

El usuario debe poder seleccionar y cambiar cualquier texto sin abrir un editor de imágenes.
Los elementos ilustrados del gráfico pueden permanecer raster, pero el contenido semántico no.

## 7. Escala para documentos extensos

No impongas un máximo de diapositivas. Para documentos largos:

- completa primero el inventario de cobertura;
- define familias de composición y evita repetir la misma consecutivamente;
- produce y revisa por bloques manejables;
- conserva un sistema único de color, tipografía y profundidad;
- integra todos los bloques en un solo `.pptx` final;
- comprueba que cada unidad del documento fuente tenga destino en diapositiva, notas, fuentes
  u omisión justificada.

La cantidad de diapositivas puede aumentar el tiempo de producción, pero no justifica usar
una plantilla automática sin análisis semántico o dejar texto incrustado en las imágenes.

## 8. Verificación obligatoria

Renderiza cada diapositiva a tamaño completo y confirma:

- la imagen corresponde al significado del texto;
- el manifiesto explica la idea, la relación, la metáfora visual y por qué la imagen
  corresponde; la compuerta de coherencia semántica está marcada `PASS`;
- el tamaño de la imagen es proporcional a su función;
- cada cuadro vive dentro de la zona prevista;
- la cantidad de portadores visibles coincide con el inventario de contenido;
- no existe ningún rectángulo, tarjeta, panel opaco o borde nuevo añadido para encubrir un
  defecto de la imagen;
- ningún soporte de contenido queda debajo de la franja de título ni fuera del área proyectable;
- cada cuadro pertenece visualmente al soporte y conserva su morfología; no hay tarjetas
  rectangulares flotantes que oculten círculos, peldaños, placas, páginas o recorridos;
- el cuadro completo respeta el margen seguro del soporte y su rotación coincide con la
  inclinación de la superficie;
- no hay texto sobre iconos, bordes, conectores o sombras esenciales;
- no hay duplicados entre texto raster y texto editable;
- títulos, etiquetas, cifras y fuentes pueden seleccionarse como objetos de PowerPoint;
- el texto conserva contraste, jerarquía y legibilidad;
- las gráficas y tablas siguen siendo editables y representan los datos correctos;
- al mover temporalmente un cuadro de texto, la zona inferior permanece limpia;
- el mosaico completo se percibe moderno, colorido, profesional y coherente, sin convertirse
  en una sucesión de composiciones idénticas.
- ninguna escena se reutiliza en otra diapositiva;
- al ocultar todos los cuadros de texto siguen siendo evidentes los contenedores y la relación
  entre ellos; si queda solo un fondo, la imagen se rechaza.

Corrige y vuelve a renderizar hasta que todas las condiciones se cumplan.
