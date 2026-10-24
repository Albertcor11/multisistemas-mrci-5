# Concordancia morfológica y encaje del texto

## Principio

Imagen, soporte y texto deben percibirse como una sola composición. No basta con que el cuadro
quede sobre la ilustración o dentro de su rectángulo general. El cuadro debe ocupar la **cara
útil del objeto portador**, seguir su forma visual y dejar visibles los elementos que explican
la acción: personajes, manos, conectores, bordes, sombras, recorridos y jerarquías.

Esta compuerta se aplica después de aprobar la coherencia semántica y antes de construir la
diapositiva. Una imagen conceptualmente correcta se rechaza cuando sus superficies no permiten
encajar el texto real de forma fina, legible y elegante.

## Inventario geométrico por soporte

Registra para cada zona editable:

- `soporte`: marco, módulo, peldaño, círculo, bloque, engrane, anillo, placa, hito, mesa,
  tramo, página u otro objeto;
- `polígono_útil`: límites visuales de la cara disponible, no los límites de toda la imagen;
- `caja_interior`: `x`, `y`, ancho y alto ya descontando la holgura;
- `rotación`: ángulo común del soporte y el cuadro;
- `alineación`: izquierda, centro o derecha conforme al eje del objeto;
- `contraste`: color de texto y, solo si es necesario, velo integrado al material;
- `capacidad`: líneas y caracteres admisibles con Arial al tamaño mínimo permitido;
- `elementos_protegidos`: manos, rostros, iconos, bordes, conectores, sombras y objetos que no
  pueden cubrirse.

Si el texto supera la capacidad, cambia de escala, redistribuye entre soportes o elige otra
composición. No amplíes el cuadro fuera del objeto ni lo conviertas en una tarjeta flotante.

## Reglas por forma

- **Rectángulos y módulos:** conserva un margen interior uniforme de 6–10%; alinea el cuadro
  con el eje y la rotación del módulo.
- **Círculos y medallones:** usa una caja central más estrecha que el diámetro; aumenta los
  márgenes laterales en la mitad superior e inferior para respetar la curvatura.
- **Peldaños y flechas:** coloca una idea por escalón o por tramo, con el mismo ángulo visual;
  el orden de lectura debe seguir el ascenso o avance.
- **Bloques apilados:** usa una línea o un fragmento breve por cara. El bloque mayor recibe la
  explicación más extensa.
- **Escudos, engranes y núcleos:** la tesis vive en la cara central; estados, excepciones o
  controles se distribuyen en placas vinculadas.
- **Puentes y rutas:** cada texto pertenece a un tramo o hito. Las cajas no atraviesan juntas,
  pilares, personajes ni curvas esenciales.
- **Páginas y libros:** respeta el canal central, los bordes y la leve inclinación de cada
  página; no uses una caja horizontal que cruce ambas páginas.
- **Mesas y escenas de deliberación:** los criterios viven en superficies vinculadas a la
  mesa y la conclusión en el centro de decisión; evita cubrir a los participantes.

## Velo de contraste permitido

El cuadro predeterminado es transparente. Cuando la textura o el color del objeto reduzcan la
legibilidad, se permite un velo o relleno que:

1. reproduzca la forma, color, borde y rotación del soporte;
2. permanezca íntegramente dentro de su cara útil;
3. sea lo bastante transparente para conservar el material y su profundidad;
4. no parezca una tarjeta de interfaz independiente;
5. no cubra personajes, conectores ni símbolos relevantes.

No uses una colección de rectángulos oscuros uniformes sobre objetos distintos. Cada velo debe
heredar la morfología de su portador.

## Orden de construcción

1. Mide el texto real y separa sus unidades semánticas.
2. Aprueba la metáfora con la compuerta de coherencia semántica.
3. Escala y coloca la imagen sin deformarla.
4. Traza las caras útiles de los soportes y calcula su capacidad.
5. Asigna cada unidad al soporte cuya función visual corresponde.
6. Inserta cuadros nativos transparentes o velos morfológicos mínimos.
7. Renderiza a tamaño completo y corrige caja, fuente, rotación, interlineado y posición.
8. Aplica las pruebas de encaje y registra `PASS` o `REJECT`.

## Pruebas obligatorias

- **Prueba de contorno:** ningún vértice del cuadro o de sus márgenes sale del soporte.
- **Prueba de oclusión:** personajes, manos, bordes, conectores y símbolos siguen visibles.
- **Prueba de pertenencia:** al ver el cuadro, resulta evidente a qué objeto pertenece.
- **Prueba de forma:** círculo, peldaño, página o placa conservan su identidad; el texto no los
  convierte visualmente en rectángulos genéricos.
- **Prueba de dirección:** la lectura sigue el recorrido de la imagen.
- **Prueba de distancia:** título y cuerpo se leen en proyección sin reducir Arial por debajo
  del mínimo aplicable.
- **Prueba de elegancia:** hay aire constante, alineación óptica, ritmo y proporción; ninguna
  caja parece añadida después de terminar la ilustración.

Solo entrega cuando todas las zonas registren `PASS`. La fidelidad textual no justifica un
encaje deficiente: cuando ambas exigencias colisionen, cambia la composición o genera una
escena con soportes mayores.
