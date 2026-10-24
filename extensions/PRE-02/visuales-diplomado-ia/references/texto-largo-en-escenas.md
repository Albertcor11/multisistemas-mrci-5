# Texto largo en escenas portadoras

## Principio

La longitud del texto modifica la arquitectura de la imagen. No se resuelve un párrafo largo
reduciendo la tipografía dentro de una tarjeta diseñada para una frase. A mayor densidad,
crece la superficie física de lectura y disminuye la proporción de ambiente o personajes.

Selecciona un modo `D01–D06` de
[catalogo-densidades-texto-6.json](catalogo-densidades-texto-6.json). El conteo de palabras es
solo una primera estimación: confirma siempre con la tipografía real, saltos de línea,
encabezados, viñetas, cifras, palabras largas y renderizado de la diapositiva.

## Flujo de cálculo

1. Separa título, subtítulo, cuerpo, encabezados internos, cifras, fuente y folio.
2. Cuenta palabras y caracteres del cuerpo, pero conserva también sus saltos y jerarquía.
3. Estima líneas con la tipografía y ancho reales. No uses el promedio como aprobación final.
4. Elige `D01–D06` y asigna rectángulos `x`, `y`, ancho y alto a cada bloque.
5. Para `D04–D06` —y `D03` con varios párrafos— consulta
   [seleccion-20-familias-texto-grande.md](seleccion-20-familias-texto-grande.md), propone tres
   familias `LTxx` y selecciona la primera si el usuario no indica otra. Para densidades menores,
   selecciona la familia `Exx` y composición `Cxx` capaces de construir los rectángulos.
6. Genera la imagen sin texto; coloca después el contenido como cuadros nativos.
7. Renderiza a tamaño completo, corrige desbordamientos y vuelve a comprobar.

## Modalidades para texto largo

### Macropanel sostenido

Un panel ocupa aproximadamente dos tercios del lienzo. Figuras, grúas, módulos, columnas o
plataformas lo sostienen o construyen. Adecuado para una explicación continua, conclusión,
criterio jurídico o exposición de hechos.

### Dos columnas físicas

Dos paneles verticales amplios forman parte de una misma escena. Úsalo para dos apartados
largos, regla y excepción, situación y consecuencia, o dos grupos de fundamentos. Las columnas
son cuadros de PowerPoint independientes.

### Bandas de lectura

Tres o cuatro bandas horizontales anchas permiten conservar encabezados y párrafos breves. La
escena puede mostrar trabajadores instalándolas, un archivo desplegado, una escalera de
plataformas o capas de un sistema.

### Página editorial enmarcada

Un gran tablero de una o dos columnas ocupa entre 78% y 94% del área útil. La familia escénica
vive en el borde, base o esquinas y explica la función del texto: revisar, deliberar, construir,
proteger o documentar. No es un fondo; los objetos sostienen el panel.

### Comparación extensa

Dos paneles de lectura equivalentes, con un eje, balanza, puente o mesa de deliberación que
visualiza su relación. No uses una tabla rasterizada. Si existen datos comparables, conserva la
tabla como objeto nativo.

### Continuidad autorizada

Cuando el texto no cabe con el mínimo tipográfico y el usuario permite dividir, crea una
secuencia visual coherente: misma familia y acabado, marcador nativo de continuidad y reparto
por unidades semánticas. No cortes una oración ni dupliques el encabezado como contenido nuevo.

## Modo de fidelidad literal

Si el Word exige una correspondencia exacta por diapositiva, no condenses, no traslades a notas
y no dividas sin autorización. Usa primero `D05` o `D06`, reduce la presencia ambiental y
prioriza el panel editorial. Si aun así el texto no cabe de forma legible, reporta la colisión
entre literalidad y legibilidad y solicita autorización antes de cambiar el número de láminas.

## Reglas de legibilidad

- Sin una plantilla o reedición más autoritativa, usa 14–18 pt para cuerpo principal, procura
  17 pt o más cuando el volumen lo permita y reserva 8–10 pt para detalle legal o probatorio
  no principal. Respeta un mínimo superior si la plantilla o el uso presencial lo requiere.
- No uses más de dos columnas para prosa continua.
- No coloques párrafos sobre fotografías, texturas, degradados intensos o zonas curvas.
- Mantén márgenes interiores amplios y separación visible entre párrafos.
- Los paneles destinados a texto largo deben ser casi planos a cámara; evita perspectiva
  pronunciada y formas circulares.
- La imagen puede ocupar menos superficie, pero debe seguir explicando la función del panel.
- El texto continúa siendo editable; nunca lo hornees para ganar espacio.

## Prueba de aprobación

Una diapositiva de texto largo se aprueba solo si:

- el texto completo cabe sin cortes ni reducción por debajo del mínimo;
- la lectura tiene un orden inequívoco;
- el panel está físicamente integrado a la escena;
- las figuras u objetos no invaden el área de lectura;
- al mover el texto, la superficie inferior permanece limpia;
- en fidelidad literal, la auditoría Word–PowerPoint resulta aprobada.
