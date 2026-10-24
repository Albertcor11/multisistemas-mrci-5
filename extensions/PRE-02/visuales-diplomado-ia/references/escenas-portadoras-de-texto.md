# Escenas portadoras de texto

## Corrección de enfoque

Una imagen para PowerPoint no se aprueba por ser bonita ni por dejar un vacío donde pueda
colocarse un párrafo. Debe actuar como **mecanismo de presentación**: sus personajes, objetos,
recorridos y contenedores organizan el contenido. El texto editable se coloca sobre superficies
que ya pertenecen a la escena.

La prueba decisiva es esta: si se eliminan los cuadros de texto, todavía deben verse claramente
los lugares donde cada idea vive y la relación entre ellos. Si solo queda un paisaje, una textura,
una nebulosa o una fotografía con espacio negativo, la imagen es un fondo y debe rechazarse.

## Cadena completa de decisión

1. **Relación del contenido:** proceso, comparación, sistema, jerarquía, riesgo, evidencia,
   decisión u otra arquitectura `C01–C50`.
2. **Densidad real:** clasifica `D01–D06` después de medir palabras, caracteres, apartados,
   jerarquía y espacio útil.
3. **Biblioteca:** usa `E01–E50` para `D01–D02`; decide por estructura en `D03`; usa
   `LT01–LT20` para `D04–D06` y para `D03` con párrafos o varios apartados.
4. **Kit mixto:** si la presentación contiene densidades distintas, selecciona `KM01–KM08`
   para limitar familias y conservar una identidad común.
5. **Acabado:** aplica paleta, material, iluminación y lenguaje `S01–S50`; el kit fija un
   acabado primario y uno secundario.
6. **Comprobación:** genera sin texto, superpone cuadros editables, renderiza y aplica la
   prueba anti-fondo.

El orden no se invierte. No se elige primero una imagen vistosa para obligar después al texto a
adaptarse a ella. Consulta [modo-mixto-kit-profesional.md](modo-mixto-kit-profesional.md) y
[seleccion-20-familias-texto-grande.md](seleccion-20-familias-texto-grande.md) cuando aplique.

## Ejemplos rectores

- **Sistema solar:** cada planeta tiene al lado una tarjeta de color integrada a su órbita. El
  sol puede sostener la tesis y los planetas, los componentes. La galaxia no es un fondo.
- **Obreros blancos:** figuras completamente blancas cargan, levantan o colocan marcos,
  círculos y bloques de color. Las figuras explican acción y responsabilidad; los objetos
  sostienen el texto.
- **Escalera financiera:** una flecha roja ascendente se convierte en escalones amplios. Figuras
  blancas suben, mueven círculos o colocan indicadores. Cada peldaño contiene una etapa o dato.
- **Puente:** los extremos sostienen situación actual y objetivo; cada tramo del puente contiene
  una condición o acción. Los personajes pueden construir los tramos.
- **Mesa de diagnóstico:** las evidencias viven en bandejas o tarjetas alrededor de una mesa;
  la conclusión ocupa un panel central.

## Requisitos de una escena aprobable

- Los portadores de texto son objetos visibles: tarjetas, paneles, círculos, plataformas,
  peldaños, módulos, contenedores, placas, marcos o caras frontales.
- Esos portadores ocupan una parte sustancial del lienzo y tienen interiores lisos, sin textura,
  brillos, estrellas, personas, iconos ni conectores que interfieran.
- Las personas o elementos figurativos ejecutan una función: cargar, construir, revisar,
  conectar, filtrar, proteger, comparar o decidir.
- La dirección visual coincide con la lectura del contenido.
- La escena es autosuficiente como composición de diapositiva; no depende de un bloque de texto
  desconectado colocado a un lado.
- El fondo mantiene baja densidad y existe para sostener contraste, no para protagonizar.
- Todo texto semántico permanece fuera del raster y se añade después como objetos nativos.

## Prueba anti-fondo

Rechaza o regenera si ocurre cualquiera de estas condiciones:

- más de la mitad del impacto visual proviene del ambiente y no de los portadores;
- las zonas de texto son solo espacio negativo amorfo;
- los cuadros editables quedarían flotando sin relación con objetos de la escena;
- los personajes posan, miran a cámara o decoran sin ejecutar una acción;
- la metáfora no permite saber dónde empieza, continúa o concluye el mensaje;
- el texto tendría que cubrir elementos esenciales para caber;
- la imagen podría intercambiarse por cualquier otra sin cambiar el significado de la lámina.

## Selección rápida de familia

| Necesidad | Familias recomendadas |
|---|---|
| Componentes alrededor de un núcleo | E01, E27 |
| Construcción o implementación | E02, E04, E29, E31 |
| Crecimiento o finanzas | E03, E47 |
| Proceso o transformación | E05, E23, E26, E34 |
| Transición o brecha | E06, E19, E30 |
| Hitos y madurez | E07, E47, E50 |
| Control y gobernanza | E12, E13, E25, E38, E42 |
| Comparación o decisión | E11, E15, E43, E45 |
| Evidencia o auditoría | E14, E16, E18, E28, E49 |
| Riesgo y contingencia | E20, E32, E41, E46 |
| Ecosistema y relaciones | E09, E22, E37, E39, E48 |
| Profundidad y causas ocultas | E21, E35 |

## Generación

Construye el prompt con la familia como argumento principal:

```bash
python3 scripts/construir_prompt_50x50.py \
  --family E01 \
  --composition C20 \
  --subject "áreas que integran el sistema de control"
```

El acabado sugerido por la familia se aplica automáticamente. Usa `--style Sxx` solo si el
proyecto necesita otro acabado. Una familia combinada con las 50 composiciones produce 50
imágenes diferentes sin reducirlas a fondos con variaciones de color.
