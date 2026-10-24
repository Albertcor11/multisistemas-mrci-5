# Preservación quirúrgica de PowerPoint

## Cuándo aplicar este modo

Úsalo cuando el usuario entregue una presentación manual que declara correcta, solicite una
réplica exacta, pida conservar el diseño y el contenido, o autorice únicamente una reparación
concreta. La presentación manual gobierna geometría, capas, grupos, proporciones, imágenes,
recortes, espacios portadores, logotipo y ritmo. El objetivo no es reinterpretarla: es mantener
todo lo aprobado y cambiar solo lo solicitado.

## Principio de intervención mínima

1. Conserva intacto el archivo fuente y trabaja sobre una copia.
2. Renderiza todas las diapositivas antes de editar y guarda ese conjunto como patrón oro.
3. Identifica la parte exacta que necesita reparación: cuadro, imagen, gráfica, relación,
   caché, tabla, nota, orden de capa u otro componente.
4. Usa una edición dirigida al objeto o parte concreta. No reconstruyas diapositivas ajenas.
5. Si una herramienta obliga a importar y exportar todo el archivo, genera una prueba antes de
   aceptarla y compara todas las láminas contra el patrón oro.

Una conversión global se rechaza cuando altera grupos, transformaciones, visibilidad, recortes,
z-order, SmartArt, tablas, gráficas, fuentes o imágenes que el usuario no pidió modificar.

## Texto presente no equivale a texto visible

La auditoría hostil de texto es necesaria, pero no suficiente. Un cuadro puede seguir dentro
del XML y desaparecer del render por:

- pérdida o cambio de una transformación de grupo;
- recorte o máscara incorrecta;
- coordenadas fuera del lienzo;
- cambio de orden de capa;
- relleno, transparencia o color que vuelven invisible el texto;
- serialización incompleta de diagramas o formas agrupadas;
- incompatibilidad entre la herramienta y una construcción nativa de PowerPoint.

Si el inventario textual coincide pero una lámina queda vacía, incompleta o visualmente
distinta, la entrega está rechazada. No presentes el resultado como fiel.

## Reparaciones de gráficas y relaciones

Cuando una gráfica se ve correctamente, pero su caché o relación interna está dañada:

- usa únicamente categorías, series y valores visibles o verificables en la fuente;
- conserva posición, dimensiones, colores, etiquetas, ejes y aspecto;
- modifica solo la parte de gráfica o relación necesaria cuando una conversión global cambie
  otras diapositivas;
- no materialices un libro nuevo si se requiere preservar fórmulas o procedencia;
- registra si la reparación está destinada solo a PowerPoint o debe ser portátil.

Una reparación interna no autoriza alterar el contenido ni «mejorar» cifras.

## Comparación obligatoria

Después de cada versión candidata:

1. Renderiza fuente y salida con el mismo motor, resolución y tamaño.
2. Compara todas las diapositivas, incluidas las no editadas.
3. Ejecuta `scripts/auditar_pptx_pptx.py` para texto, gráficas y comparación opcional de
   renders.
4. Revisa a tamaño completo toda lámina con diferencia.
5. Comprueba además mosaico y simulación de proyección.

Las diapositivas no autorizadas para cambiar deben ser idénticas en render. La lámina reparada
puede diferir únicamente en lo solicitado; si la reparación es interna y no visual, también
debe coincidir en píxeles.

## Respuesta ante una conversión destructiva

Si una importación y exportación global conserva el texto inventariado, pero elimina contenido
visible en láminas no intervenidas:

1. rechaza esa candidata;
2. conserva el archivo fallido solo como diagnóstico, fuera de la carpeta de entrega;
3. vuelve al patrón oro;
4. aplica una reparación dirigida al objeto o a la parte OOXML necesaria;
5. repite validación estructural, auditoría hostil y comparación visual completa.

No compenses la pérdida recreando aproximadamente la lámina. Si el patrón oro ya existe, debe
preservarse.

## Criterio de aprobación

La salida se aprueba solo cuando:

- conserva el número de diapositivas;
- no falta ni sobra texto, cifra o dato visible;
- las láminas no intervenidas coinciden con la fuente;
- el cambio autorizado no altera otras capas;
- no hay elementos invisibles, cortados, fuera del lienzo o detrás de una imagen;
- tablas y gráficas requeridas permanecen editables;
- la validación estructural y la importación de comprobación resultan aprobadas.

### Calibración GSPA

En `Empresa_Socialmente_Responsable_GSPA_19_diapositivas.pptx`, una conversión global conservó
el inventario textual, pero hizo desaparecer en el render el contenido agrupado de las
diapositivas 73–75. El auditor textual resultó aprobado y, aun así, la presentación era
incorrecta. Una reparación limitada a la parte interna de la gráfica defectuosa conservó las
90 diapositivas con coincidencia visual completa y mantuvo el texto y los datos. Este caso
confirma que la comparación render–render es una compuerta independiente y obligatoria.
