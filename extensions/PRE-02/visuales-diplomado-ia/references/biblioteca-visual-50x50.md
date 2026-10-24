# Biblioteca visual generativa 50 × 50

## Objetivo

Ofrecer 50 familias de escenas profesionales, cada una capaz de producir al menos 50 imágenes
estructuralmente distintas y útiles dentro de una diapositiva. La matriz principal combina:

- [catalogo-familias-escenicas-50.json](catalogo-familias-escenicas-50.json): 50 mecanismos
  visuales portadores `E01` a `E50`;
- [catalogo-composiciones-50.json](catalogo-composiciones-50.json): 50 arquitecturas narrativas
  `C01` a `C50`;
- [catalogo-estilos-50.json](catalogo-estilos-50.json): 50 acabados opcionales `S01` a `S50`;
- `scripts/construir_prompt_50x50.py`: selector y constructor determinista de prompts.

La combinación `E × C` produce 2,500 plantillas posibles sin almacenar 2,500 PNG dentro de la
skill. Los acabados `Sxx` amplían la identidad, pero no sustituyen la función escénica. Las
imágenes finales se generan bajo demanda para el contenido real de cada presentación.

Esta matriz resuelve principalmente textos breves y medios. Para texto extenso se complementa
con [catalogo-20-familias-texto-grande.json](catalogo-20-familias-texto-grande.json); para
presentaciones con densidades mixtas se gobierna mediante
[catalogo-8-kits-mixtos-profesionales.json](catalogo-8-kits-mixtos-profesionales.json).

## Qué significa una opción

Una opción o “juego de imágenes” es una familia escénica completa, por ejemplo `E01 Sistema
solar de decisiones`, `E02 Obreros blancos portadores` o `E03 Escalera financiera ascendente`.
Sus 50 imágenes posibles surgen al combinarla con `C01` a `C50`. La familia conserva personajes,
objetos y metáfora; la composición cambia la función narrativa y la geometría. El acabado
`Sxx` define paleta, material e iluminación.

Lee [escenas-portadoras-de-texto.md](escenas-portadoras-de-texto.md). Una opción debe sostener
el texto mediante objetos visibles. Una galaxia vacía, un degradado, una textura o una persona
al lado de un gran espacio negativo son fondos, no plantillas.

Para mantener calidad profesional:

- conserva uno o dos acabados `Sxx` en toda la presentación;
- cambia de familia `Exx` cuando otra metáfora explique mejor la idea;
- rota las composiciones `Cxx` según el significado de cada diapositiva;
- no repitas una combinación `Exx-Cxx` dentro del mismo archivo sin razón narrativa.

## Selección semántica

Elige primero la composición por la relación del contenido; después la familia escénica que
puede sostenerla físicamente y, al final, el acabado por audiencia, marca y tono.

| Contenido | Composiciones recomendadas |
|---|---|
| Portada o sección | C01–C04 |
| Tesis o decisión | C05–C07, C41, C45 |
| Proceso o cronología | C08–C14, C28, C44, C47 |
| Comparación o niveles | C15–C19, C29–C32 |
| Sistema o causalidad | C20–C25, C33–C35, C48 |
| Caso o evidencia | C36–C40 |
| Control, riesgo o excepción | C42–C46 |
| Síntesis o cierre | C49–C50 |

Selecciona la familia escénica con la tabla de
[escenas-portadoras-de-texto.md](escenas-portadoras-de-texto.md). Selecciona el acabado con
estos criterios:

- institucional y jurídico: S01–S05, S15–S18, S24;
- ejecutivo y corporativo: S08–S16, S39–S43, S48–S49;
- técnico, datos e innovación: S05–S06, S12–S13, S25–S26, S35–S38, S50;
- territorial, municipal o ambiental: S21–S23, S33–S34, S44–S46;
- editorial expresivo: S02, S07, S17–S20, S27–S32, S47.

## Flujo de generación

1. Analiza el texto, asigna `D01–D06` y calcula las zonas editables antes de elegir la imagen.
2. Si es `D04–D06` —o `D03` con párrafos— abandona la matriz `E × C` y selecciona una familia
   `LT01–LT20`. Si el documento es mixto, selecciona antes un kit `KM01–KM08`.
3. Para `D01–D02` —o `D03` por bloques— selecciona una familia escénica `Exx`, una composición
   `Cxx` y, si hace falta, un acabado
   `Sxx`. Si no indicas acabado, el script aplica el recomendado por la familia.
4. Construye el prompt:

```bash
python3 scripts/construir_prompt_50x50.py \
  --family E01 \
  --composition C20 \
  --subject "áreas que integran el sistema de control"
```

5. Usa el prompt con la herramienta integrada de generación de imágenes. Genera una llamada
   independiente por imagen; no uses una sola variante para temas distintos.
6. Inspecciona el resultado. Rechaza cualquier palabra, número, marca o zona contaminada.
7. Aplica la prueba anti-fondo: los portadores deben ser visibles y los cuadros de texto no
   pueden quedar flotando sobre el ambiente.
8. Copia la imagen final al proyecto y coloca encima los cuadros de texto editables.
9. Registra densidad, kit, familia, composición, acabado y ruta en el manifiesto.

Para comprobar la biblioteca:

```bash
python3 scripts/construir_prompt_50x50.py --validate
```

Para comprobar de una sola vez los seis catálogos, referencias, scripts y enlaces internos:

```bash
python3 scripts/validar_sistema_visual.py
```

Para exportar el índice completo de 2,500 combinaciones:

```bash
python3 scripts/construir_prompt_50x50.py --matrix matriz-2500.csv
```

## Manifiesto de uso

Mantén por proyecto una tabla con:

1. número de diapositiva;
2. función narrativa;
3. familia escénica `Exx`;
4. composición `Cxx`;
5. acabado `Sxx`;
6. combinación `Exx-Cxx`;
7. tema enviado al generador;
8. zonas de texto previstas;
9. ruta de la imagen aprobada;
10. densidad `Dxx`, familia larga `LTxx` o kit `KMxx` cuando correspondan;
11. estado de la prueba anti-fondo y revisión final.

Este registro evita repeticiones y permite sustituir una imagen sin perder la lógica de la
presentación.

## Producción por lotes

Antes de producir 50 imágenes de una familia, genera entre tres y cinco muestras con
composiciones muy distintas. Confirma que sus objetos sostienen el texto, que los personajes
realizan acciones útiles y que las superficies editables son amplias y limpias. Después
continúa una imagen por llamada y revisa cada resultado antes de incorporarlo.

La biblioteca no autoriza la generación ciega de 2,500 archivos. Produce solo las imágenes
requeridas por el proyecto o por un lote expresamente solicitado. Si se encarga una colección
completa, trabaja por bloques y conserva un índice de aprobadas, rechazadas y regeneradas.

## Reglas de calidad

- Cada imagen debe tener una función narrativa, no ser decoración intercambiable.
- Cada imagen debe contener objetos portadores de texto claramente identificables.
- El ambiente nunca puede ser el protagonista ni sustituir la estructura de la diapositiva.
- Mantén proporción 16:9 y resolución suficiente para el tamaño final.
- Ninguna imagen contiene texto, cifras, fórmulas, logotipos ni marcas de agua.
- Las zonas descritas por la composición permanecen limpias y contrastadas.
- Todo contenido semántico se añade como texto nativo de PowerPoint.
- Gráficas y tablas se insertan como objetos editables dentro de los marcos previstos.
- No reutilices una imagen para dos ideas diferentes.
- No repitas la misma composición consecutivamente.
- Conserva unidad de acabado dentro de cada presentación.
- Renderiza y revisa la diapositiva completa después de superponer el texto.
