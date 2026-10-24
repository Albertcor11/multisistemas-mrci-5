# Identidad visual institucional

Extraída del corpus de 58 referencias del diplomado. Las referencias enseñan **cómo debe
verse** el sistema, no qué contenido copiar. Nunca conviertas una referencia en plantilla.

---

## 1. Las tres familias visuales

El corpus no es homogéneo. Contiene tres familias coherentes entre sí. Elegir la familia
es la primera decisión de composición, antes que el tipo de diagrama.

### Familia A — Diagrama limpio  *(por defecto)*

Fondo transparente o blanco puro. El color vive en los elementos gráficos: tarjetas,
badges, conectores. Referencia canónica: `s4_d07_esqueleto_flujo_operativo.png`.

- Cuándo: flujos, procesos, arquitecturas, mapas de relaciones, secuencias, ciclos.
- Por qué es la default: se integra con cualquier plantilla de PowerPoint sin recortar,
  sobrevive a un cambio de fondo institucional y proyecta mejor en sala con luz.
- Riesgo a vigilar: el generador tiende a inventar un fondo degradado oscuro aunque se
  le pida transparencia. Si aparece, regenera insistiendo en el negativo correspondiente.

### Familia B — Tarjeta ejecutiva oscura

Fondo azul marino profundo, tarjetas blancas o azul claro encima, acento dorado.
Referencias: `s6_d12_ficha_sistema_leg001.png`, `s2_d10_eleccion_del_tipo_v2.png`.

- Cuándo: fichas de sistema, tablas de atributos, síntesis de cierre, diapositivas de
  concepto con peso institucional.
- Dosis: una o dos por sesión como máximo. Es la familia con más presencia visual y
  satura si se repite.
- Riesgo: el fondo oscuro obliga a la imagen a competir con la plantilla de PowerPoint.
  Úsala solo cuando la diapositiva vaya a ceder el lienzo casi completo a la imagen.

### Familia C — Escena editorial

Composición fotorrealista: escritorio, papel, objetos de oficina, con el diagrama
impreso o dibujado sobre el papel. Referencia: `s2_d05_concepto_vs_arquitectura.png`.

- Cuándo: exclusivamente contrastes antes/después de alto impacto narrativo, donde el
  objeto físico (una nota adhesiva, un documento) *es* el argumento.
- Dosis: máximo una por módulo. Es memorable justamente porque es excepcional.
- Riesgo: la más costosa de acertar y la que más texto deforma. No la uses para
  contenido técnico denso.

> Nota de coherencia: el documento original del skill prohibía los fondos oscuros y las
> fotografías. El corpus real los usa y funcionan bien en su nicho. Esta versión los
> admite como familias acotadas con cuota, en lugar de prohibirlos en el papel y
> tolerarlos en la práctica. Si prefieres el criterio estricto, limita el skill a la
> familia A y elimina las secciones B y C.

---

## 2. Paleta

### Base institucional

| Rol | Color | Hex |
|---|---|---|
| Azul institucional | estructura, contenedores primarios | `#1D4E8F` |
| Azul marino profundo | fondos familia B, nodos de inicio/fin | `#0E2A4E` |
| Blanco | tarjetas, texto sobre oscuro | `#FFFFFF` |
| Gris claro | fondos de soporte, separadores | `#E8EDF3` |
| Grafito | texto secundario | `#475569` |
| Dorado | acento premium, destacados, badges de importancia | `#D9A227` |

### Acentos semánticos

Cada color comunica algo. No decoran; significan. Usar solo el acento que corresponda.

| Color | Hex | Significado |
|---|---|---|
| Verde | `#0E9F6E` | validación, aprobación, cumplimiento, éxito |
| Teal | `#17A398` | análisis, hallazgos, examen |
| Naranja | `#E8871E` | proceso, actividad, iteración, advertencia leve |
| Morado | `#7B3FBF` | producción documental, categoría diferenciada |
| Rojo | `#D93636` | error, riesgo, carencia (solo en contraste) |
| Amarillo | `#EFC94C` | supuesto, alerta informativa |

### Reglas de color

- No todas las imágenes en azul y dorado. La variación cromática dentro de la paleta es
  identidad, no ruido.
- Nada de franjas doradas por defecto.
- En secuencias numeradas, un color por paso, progresando azul → verde → ámbar →
  morado → rojo, como en `s1_d11_cinco_componentes.png`.
- Nunca un degradado tipo arcoíris ni un halo de color detrás de los elementos.

---

## 3. Composición

- Orientación horizontal y composición objetivo **16:9**, igual que la diapositiva final.
  Si la herramienta permite fijar dimensiones, solicita una salida 16:9 de alta resolución
  —por ejemplo 1920×1080 o 3840×2160—; si entrega otra medida, conserva la proporción al
  colocarla y no estires la imagen. No afirmes que una herramienta entrega siempre una
  dimensión concreta.
- Rejilla invisible: todo alineado horizontal y verticalmente. Los centros de los badges
  circulares comparten línea; las bases de las tarjetas comparten línea.
- Jerarquía por tamaño: el elemento primario es visiblemente mayor.
- Contenedores: tarjetas con esquinas redondeadas de 8 a 12 px y sombra suave.
- Conectores: flechas direccionales sólidas para flujo, líneas finas para relación,
  proximidad para agrupación. Una flecha ambigua arruina el diagrama entero.
- Espacio negativo generoso. Un visual con aire se lee; uno lleno se ignora.
- Distribución balanceada: nada de peso acumulado en un costado.

## 4. Tipografía editable en PowerPoint

En presentaciones, **ninguna palabra se hornea dentro de la imagen**. La imagen reserva
paneles y superficies limpias; títulos, etiquetas, cifras, fechas, fórmulas y fuentes se
colocan encima como objetos nativos de PowerPoint.

- Sans-serif geométrica limpia y contemporánea, aplicada en PowerPoint.
- Negrita para encabezados de bloque; regular para explicaciones.
- Jerarquía de tres niveles como máximo por diapositiva.
- Números grandes y prominentes cuando la secuencia o el dato lo justifiquen.
- Mayúsculas solo en etiquetas cortas.
- Español con acentuación correcta y texto completamente seleccionable.

Solo si el usuario pide expresamente una imagen final no editable puede considerarse texto
rasterizado; esa excepción no pertenece al flujo predeterminado de PowerPoint ni sustituye la
auditoría textual.

## 5. Iconografía

Iconos planos con profundidad sutil, dentro de badges circulares de color sólido,
símbolo en blanco. Cada icono tiene función semántica.

| Concepto | Icono |
|---|---|
| Objetivo / meta | Diana |
| Jurídico / justicia | Balanza |
| Procesamiento / sistema | Engrane |
| Validación / aprobado | Palomita en escudo |
| Análisis / investigación | Lupa sobre documento |
| Seguridad / confidencialidad | Candado |
| Roles / equipo | Figuras humanas |
| Resultados / métricas | Gráfica de barras |
| Retroalimentación / ciclo | Flechas circulares |
| Decisión / dirección | Bifurcación de flechas o brújula |
| Documentación / biblioteca | Libro abierto o carpeta |
| Entrada / datos | Documento con líneas |
| Producto / entregable | Documento con palomita |
| Error / riesgo | Triángulo de advertencia |
| Contexto / información | "i" en círculo |
| Inicio / fin | Play y bandera a cuadros |

## 6. Estética prohibida

Nunca: infantil, caricaturesca, clipart, estética genérica de Canva, emojis, mascotas,
robots genéricos, humanoides de IA, neón, cyberpunk, 3D ornamental, halos luminosos,
marcos decorativos externos, texturas pesadas, degradados dramáticos.

## 7. Variación controlada

Mantén una **familia visual**, no una plantilla rígida.

- Puede variar: composición, geometría, orientación de los elementos, cantidad de
  bloques, tipo de diagrama, proporción de acento, tratamiento de categorías.
- Debe conservarse: sobriedad, limpieza, jerarquía clara, vocabulario iconográfico,
  identidad cromática, tono ejecutivo.

Dos diapositivas consecutivas de la misma sesión no deben compartir composición.
