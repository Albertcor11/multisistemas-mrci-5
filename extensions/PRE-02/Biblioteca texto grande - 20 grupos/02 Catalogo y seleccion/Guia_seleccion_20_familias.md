# Veinte familias para texto grande

## Cuándo usar esta biblioteca

Úsala después de clasificar una diapositiva como `D04`, `D05` o `D06`, o cuando una lámina
`D03` contenga varios párrafos, requisitos o argumentos que necesiten una superficie amplia.
Las familias `LT01–LT20` complementan la biblioteca `E01–E50`; están especializadas en
mantener una proporción alta de lectura sin convertir la imagen en un fondo decorativo.

Lee [catalogo-20-familias-texto-grande.json](catalogo-20-familias-texto-grande.json) para la
definición completa de cada familia.

## Diagnóstico y sugerencias

Antes de diseñar, analiza la sección de texto completa y registra:

- modo de densidad `Dxx`;
- relación dominante: explicación, comparación, secuencia, jerarquía, decisión, sistema,
  cronología, actores, riesgos, territorio, datos o síntesis;
- número de apartados reales;
- necesidad de fidelidad literal;
- presencia de tablas, cifras o fuentes que deban seguir siendo objetos nativos.

Genera **tres sugerencias ordenadas**. Para cada una indica: código y nombre, razón semántica,
geometría prevista, número de cuadros editables y proporción aproximada de lectura. Si el
usuario no elige, utiliza la primera. No detengas una conversión completa para pedir una
preferencia cuando la mejor opción sea clara.

Puedes apoyar la preselección con:

```text
python scripts/sugerir_grupos_texto_grande.py --file contenido.txt --top 3
```

El resultado del script es una ayuda reproducible, no sustituye la revisión de significado ni
la prueba de ajuste en PowerPoint.

## Mapa rápido

| Necesidad principal | Familias preferentes |
|---|---|
| Exposición continua o definición | `LT01`, `LT11`, `LT20` |
| Dos apartados largos | `LT02`, `LT05`, `LT06` |
| Tres o cuatro apartados | `LT03`, `LT07`, `LT19` |
| Jurídico o normativo | `LT04`, `LT05`, `LT14` |
| Comparación, problema–solución | `LT06`, `LT12` |
| Proceso, implementación o etapas | `LT07`, `LT08`, `LT19` |
| Historia o cronología | `LT09` |
| Seguimiento e indicadores | `LT10`, `LT18` |
| Riesgos y controles | `LT13` |
| Principios y marco conceptual | `LT14` |
| Territorio o cobertura | `LT15` |
| Actores y responsabilidades | `LT16` |
| Estrategia sistémica | `LT17` |
| Finanzas | `LT18`, `LT06`, `LT10` |
| Resumen o recomendaciones | `LT20`, `LT01` |

## Reglas de producción

1. Genera la arquitectura sin palabras, números, símbolos tipográficos ni marcas de agua.
2. Conserva los paneles casi frontales, planos, claros y libres de objetos.
3. Deja personajes, maquinaria, columnas y conectores en bordes, base o separaciones.
4. Coloca todo el contenido semántico en cuadros nativos de PowerPoint.
5. Conserva tablas, gráficas y cifras comparables como objetos nativos; la escena solo las
   enmarca cuando sea útil.
6. Registra `Dxx`, `LTxx`, número de bloques y rectángulos de texto en el manifiesto.
7. Renderiza y cambia de familia si la geometría obliga a reducir el cuerpo por debajo del
   mínimo legible.
8. En fidelidad literal, la familia elegida no autoriza resumir, reordenar ni dividir.

## Consistencia de una presentación

Dentro de una misma sección, conserva acabado, iluminación, materiales y tipo de figuras.
Alterna familias por función narrativa, no por variedad ornamental. Repite una familia cuando
la repetición comunique continuidad, por ejemplo varias láminas de fundamentos jurídicos o
las partes autorizadas de un mismo texto largo.
