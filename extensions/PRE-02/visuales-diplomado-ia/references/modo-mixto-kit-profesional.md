# Modo mixto: kit profesional de presentación

## Objetivo

Una presentación puede contener títulos mínimos, frases breves, diagramas, tablas, párrafos y
texto literal extenso. No impongas una sola geometría a todo el archivo. Mezcla la biblioteca
`E01–E50` con `LT01–LT20` según la densidad y la relación de cada diapositiva, conservando un
kit visual rector para que el conjunto se perciba como una sola obra.

Consulta [catalogo-8-kits-mixtos-profesionales.json](catalogo-8-kits-mixtos-profesionales.json)
para seleccionar `KM01–KM08`.

## Enrutamiento por densidad

| Densidad | Biblioteca principal | Criterio |
|---|---|---|
| `D01` | `E01–E50` | impacto, metáfora, portada, tesis o dato focal |
| `D02` | `E01–E50` | dos a cuatro portadores breves |
| `D03` | puente | usa `E` para bloques independientes y `LT` para párrafos o bandas de lectura |
| `D04` | `LT01–LT20` | panel dominante o dos columnas |
| `D05` | `LT01–LT20` | página editorial, bandas o comparación extensa |
| `D06` | `LT01–LT20` | fidelidad literal y máxima superficie de lectura |

El conteo de palabras orienta, pero no anula la función. Una portada de pocas palabras sigue
siendo `E`; una cita breve que necesita tratamiento editorial puede usar `LT01`; una tabla de
datos debe construirse como objeto nativo aunque el texto circundante sea corto.

## Selección del kit rector

1. Analiza audiencia, tema, tono y predominio del contenido completo.
2. Propón hasta tres kits `KMxx` cuando la elección no sea evidente. Explica paleta, acabados y
   familias dominantes en una línea por opción.
3. Si no hay elección, aplica el primer kit y continúa.
4. Usa un acabado primario `Sxx` en todo el cuerpo y reserva el secundario para portadas,
   divisores o una sección que necesite contraste.
5. Aplica el mismo acabado a las familias `E` y `LT`; el maestro `LT` define geometría, no obliga
   a conservar sus colores originales.

## Plan visual antes de producir

Crea una tabla interna con estas columnas:

| Diapositiva | Función | Densidad | Relación | Biblioteca | Familia | Composición | Acabado | Bloques | Razón |
|---|---|---|---|---|---|---|---|---|---|

- Para `E`, registra `Exx`, `Cxx` y `Sxx`.
- Para `LT`, registra `LTxx` y `Sxx`; registra también si usa macropanel, columnas o bandas.
- Para tablas y gráficas, registra `NATIVA` y el marco visual del kit.
- En fidelidad literal, conserva el número y orden de láminas del Word.

Para generar un primer plan reproducible, prepara una lista JSON con `slide`, `title`, `text`,
`relation` opcional y `native_data` opcional, y ejecuta:

```bash
python3 scripts/planificar_kit_mixto.py --input diapositivas.json --output plan-visual.json
```

Puedes fijar un kit con `--kit KM02`. El resultado es una propuesta: revisa significado,
geometría, literalidad y espacio útil antes de producir imágenes.

## Ritmo profesional

- No fijes una proporción artificial entre texto corto y largo; el documento decide.
- Evita, cuando la libertad editorial lo permita, más de tres láminas densas consecutivas.
  Introduce síntesis, proceso, evidencia o una transición solo si ya existe contenido para ello.
- No inventes una lámina ligera para romper el ritmo en modo literal.
- Alterna relaciones, no colores aleatorios: después de una página editorial puede seguir una
  comparación, un proceso o una evidencia si la narrativa lo exige.
- Usa habitualmente entre cuatro y ocho familias `E` y entre dos y cinco familias `LT` en una
  presentación media; aumenta o reduce según extensión, sin convertirlo en cuota obligatoria.
- Repite una familia cuando comunica continuidad; evita repetir la misma geometría tres veces
  seguidas salvo secuencia deliberada.

## Continuidad entre una lámina corta y una larga

Conserva:

- paleta y acabado `Sxx`;
- material de los marcos y temperatura de luz;
- estilo de figuras, iconos y sombras;
- grosor de bordes y radios;
- tipografía, jerarquías y márgenes nativos de PowerPoint;
- lógica de transición entre escenas.

Cambia únicamente la proporción: en `D01–D02` domina la escena; en `D04–D06` dominan los
paneles de lectura. El salto de densidad debe sentirse como una misma identidad que abre o
cierra espacio, no como dos plantillas pegadas.

## Sugerencias al usuario

Antes de una presentación nueva, presenta una recomendación compacta como:

```text
Kit recomendado: KM02 Jurídico editorial.
Textos cortos: E11, E12 y E43 para criterios, compuertas y deliberación.
Textos largos: LT04, LT05 y LT14 para fundamentos, posturas y principios.
Acabado común: S03, con S41 solo para portada o divisores.
```

No muestres todos los códigos disponibles. Ofrece el kit rector y tres o cuatro familias
relevantes de cada biblioteca. Durante la construcción, selecciona por diapositiva y registra
la elección en el manifiesto.

## Control final

La presentación mixta se aprueba solo si:

- las láminas cortas y largas comparten identidad;
- ninguna familia fue elegida solo para variar;
- la densidad coincide con el espacio útil real;
- el texto continúa completamente editable;
- no hay una serie monótona de macropaneles cuando existen relaciones diferentes;
- no hay cambios arbitrarios de color, material, iluminación o estilo de personajes;
- la auditoría literal resulta aprobada cuando corresponda.
