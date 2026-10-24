# Protocolo de portadores exactos

## Propósito

Evitar el defecto más grave del modo híbrido: generar una imagen con superficies vacías y
después ignorarlas para colocar nuevas tarjetas de PowerPoint encima. La imagen, el soporte y
el texto editable deben formar una sola composición. Un problema estructural de la imagen se
resuelve regenerando la imagen, no ocultándolo con paneles añadidos.

Este protocolo rige las escenas con **portadores individuales**. No lo apliques de manera que
prohíba el modo **marco escénico con lienzo editorial**. En ese modo, una gran pantalla,
pizarrón, documento o tablero frontal es un único portador y su interior puede contener formas,
tablas, gráficas, bandas y diagramas nativos de PowerPoint. Esos objetos son válidos cuando
organizan la información dentro del área útil; no son válidos si cubren personajes, salen del
lienzo o reparan una imagen sin superficie suficiente.

## 1. Contrato antes de generar

Descompón la diapositiva en unidades semánticas reales: título de diapositiva, encabezados,
cuerpos, cifras, llamadas, fuentes, tabla, gráfica o diagrama. El título, folio y logotipo se
reservan como objetos nativos fuera de los portadores de contenido.

Registra para cada portador:

- `id_portador`;
- `unidad_contenido`;
- `tipo_soporte`: placa, página, pantalla, bloque, círculo, peldaño, mesa u otro;
- `x`, `y`, `ancho`, `alto` o `poligono_util` en coordenadas de la diapositiva;
- `margen_seguro`;
- `rotacion`;
- `capacidad_lineas` y longitud máxima estimada;
- `fuente_minima` para proyección;
- `color_superficie` y `color_texto`;
- `zonas_protegidas`: manos, figuras, iconos, bordes, sombras y conectores;
- `objeto_nativo`: ninguno, tabla, gráfica o diagrama.

La cantidad de portadores debe coincidir con la cantidad de unidades que necesitan soporte.
No pidas placas vacías de reserva: crean ruido y parecen contenido omitido.

## 2. Requisitos del prompt visual

El prompt de generación debe indicar:

1. cantidad exacta de portadores;
2. ubicación y proporción de cada uno;
3. franja superior o zona de título que debe permanecer libre;
4. superficies casi frontales para párrafos o tablas;
5. márgenes limpios sin manos, figuras, sombras, iconos ni conectores;
6. ausencia absoluta de palabras, letras, números, fórmulas, marcas y texto de muestra;
7. prohibición de placas, carteles o espacios vacíos adicionales;
8. acción y metáfora coherentes con el contenido.

Para texto largo, prioriza portadores amplios y casi frontales. Una diagonal puede servir para
una etiqueta breve; no es adecuada para un párrafo si obliga a bajar la letra o simular
perspectiva con un cuadro plano.

## 3. Colocación en PowerPoint

- Inserta la escena sin deformarla.
- Usa cuadros de texto nativos con relleno transparente y línea transparente.
- Coloca cada cuadro solo dentro de la cara útil asignada.
- Hereda el ángulo del soporte cuando sea reproducible mediante rotación plana.
- Decide el color del texto por la superficie: texto claro sobre soporte oscuro y texto oscuro
  sobre soporte claro.
- Mantén encabezado y cuerpo dentro del mismo portador; pueden ser cuadros separados, pero no
  deben salir de su cara útil.
- Para una tabla o gráfica, usa un portador dedicado. El contenido, los valores y las etiquetas
  permanecen como objetos nativos editables.

No añadas rectángulos, tarjetas, paneles opacos ni bordes nuevos para crear un espacio que la
imagen no contiene. Un velo solo es aceptable cuando forma parte del material del mismo soporte,
respeta exactamente su contorno y no oculta su función; si parece una tarjeta independiente,
la diapositiva se rechaza.

## 4. Motivos obligatorios de regeneración

Regenera la escena cuando ocurra cualquiera de estos casos:

- un portador de contenido invade la franja de título, el folio o el logotipo;
- el texto no cabe con el tamaño mínimo de proyección;
- el cuadro sale de la cara útil o necesita superponerse a otro soporte;
- la perspectiva, inclinación o curvatura impide un encaje natural;
- manos, figuras, iconos, bordes, conectores o sombras cruzan el área de lectura;
- el contraste solo puede salvarse con una tarjeta opaca añadida;
- sobran o faltan portadores respecto del inventario;
- la escena no representa la idea o la acción del texto;
- un portador oscuro recibe texto oscuro, o uno claro recibe texto claro, sin contraste suficiente.

No reduzcas la tipografía, muevas el texto a un vacío ambiental ni tapes el defecto con otra
forma. La necesidad de crear una tarjeta nueva es evidencia de que la imagen falló.

## 5. Verificación obligatoria

Revisa cada diapositiva en tres escalas: tamaño completo, mosaico y simulación de proyección.
Además, ejecuta estas pruebas:

1. **Conteo:** portadores visibles = portadores inventariados.
2. **Contorno:** cuadro y márgenes permanecen dentro de la cara útil.
3. **Transparencia:** no hay relleno ni borde que fabrique un panel nuevo.
4. **Título:** ningún soporte de contenido queda oculto por la franja superior.
5. **Oclusión:** figuras, manos, iconos, sombras y conectores no invaden glifos.
6. **Contraste:** el color del texto responde al color real del soporte.
7. **Capacidad:** el texto cabe sin desbordamiento y sin bajar del mínimo legible.
8. **Movimiento:** al desplazar temporalmente el cuadro, debajo aparece el portador limpio.
9. **Editabilidad:** palabras, cifras, tablas y gráficas semánticas siguen siendo nativas.
10. **Coherencia:** la escena explica la idea y no funciona como fondo genérico.

Una sola falla bloquea la entrega. Corrige o regenera la imagen y vuelve a renderizar la
presentación completa.
