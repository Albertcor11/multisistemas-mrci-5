# Coherencia semántica entre imagen y texto

## Regla rectora

La imagen no se elige por color, belleza, variedad o parecido superficial con otras láminas.
Debe representar la **idea, la acción y la relación central** del texto. El usuario debe poder
inferir el tema de la diapositiva al observar la escena aun antes de leer todos los cuadros.

Una escena que solo combina con la paleta o deja espacio para texto no supera esta compuerta.
Si la misma imagen pudiera acompañar sin cambios tres temas no relacionados, se considera
genérica y debe rechazarse o justificarse mediante una relación visual específica.

## Ficha semántica obligatoria por diapositiva

Antes de seleccionar o generar una imagen, registra:

1. `idea`: tesis que debe recordar la audiencia;
2. `entidades`: personas, objetos, instituciones o conceptos que intervienen;
3. `acción`: qué hacen o qué cambia;
4. `relación`: secuencia, contraste, jerarquía, control, riesgo, protección, causa, transición,
   deliberación u otra relación dominante;
5. `tensión_o_resultado`: conflicto, límite, consecuencia o conclusión;
6. `metáfora_visual`: escena concreta que vuelve visible esa lógica;
7. `por_qué_corresponde`: una frase que vincula la escena con el texto;
8. `imagen_única`: archivo o código no utilizado en otra lámina.

No pases al cálculo geométrico mientras falte cualquiera de los campos 1, 4, 6 o 7.

## Selección de escena

- Busca primero una correspondencia literal de acción: revisar con inspectores, proteger con
  escudo, construir con puente o bloques, avanzar con ruta, comparar con balanza, deliberar
  alrededor de una mesa, explicar con libro abierto.
- Cuando no exista correspondencia literal, usa una metáfora cuya relación sea inequívoca.
  Un puente sirve para transición o continuidad; no para cualquier texto de cuatro puntos.
- Haz coincidir también el número de etapas, grupos o zonas cuando ese número sea sustantivo.
- Los personajes deben ejecutar la acción del mensaje. Rechaza poses, saludos o grupos que
  solo decoran.
- El objeto principal debe expresar la relación del contenido y, además, ofrecer las zonas
  necesarias para el texto editable. La función semántica precede a la superficie disponible.
- Si ninguna escena de la biblioteca supera la compuerta, genera una nueva escena única con
  la misma identidad visual. No fuerces una imagen existente para evitar producción adicional.

## Compuerta de coherencia semántica

Califica cada candidata antes de insertarla:

| Criterio | Pregunta de control | Condición |
|---|---|---|
| Idea | ¿La escena representa la tesis y no solo el sector o la paleta? | obligatoria |
| Acción | ¿Los personajes u objetos hacen lo que el texto describe? | obligatoria |
| Relación | ¿La geometría expresa secuencia, contraste, control, jerarquía u otra relación real? | obligatoria |
| Tensión o resultado | ¿La escena permite reconocer el límite, conflicto o desenlace principal? | deseable |
| Contenedores | ¿Las superficies admiten el texto real con legibilidad? | obligatoria |
| Singularidad | ¿La escena es única dentro de la presentación? | obligatoria |

Una candidata se aprueba solo si cumple todas las condiciones obligatorias. Registra `PASS` o
`REJECT` en el manifiesto junto con `idea`, `relación`, `metáfora_visual` y
`por_qué_corresponde`.

## Pruebas posteriores al render

1. **Prueba sin texto:** oculta mental o temporalmente los cuadros. La escena debe conservar la
   relación central, aunque no comunique los detalles jurídicos o técnicos.
2. **Prueba de intercambio:** compara la imagen con las demás láminas. Si encaja mejor en otra,
   reasígnala y vuelve a calcular el diseño.
3. **Prueba contrafactual de tres temas:** imagina la misma escena en tres diapositivas ajenas.
   Si funciona igual, es demasiado genérica.
4. **Prueba de lectura:** vuelve a mostrar el texto y confirma que la escena aclara, no contradice
   ni distrae.
5. **Prueba de literalidad:** la metáfora no puede introducir hechos, cifras, sujetos o
   conclusiones ausentes del material fuente.

La coherencia estética se evalúa después de aprobar la coherencia semántica. Una imagen bella
pero incorrecta se sustituye; una imagen correcta con geometría insuficiente se regenera con
paneles adecuados.
