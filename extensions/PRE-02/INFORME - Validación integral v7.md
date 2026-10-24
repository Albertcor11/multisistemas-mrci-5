# Validación integral — versión 7

**Resultado: APROBADO**

## Sistema comprobado

- 50 familias escénicas `E01–E50`.
- 50 composiciones `C01–C50` y 2,500 combinaciones únicas.
- 50 acabados `S01–S50`.
- 6 densidades `D01–D06`.
- 20 familias editoriales `LT01–LT20`.
- 8 kits mixtos `KM01–KM08`.
- Plantilla Escultórica Negro y Oro `PENO-01`.
- Formato visual unificado en 16:9.
- Texto semántico editable en PowerPoint.

## PENO-01 comprobado

- PowerPoint base válido con 12 diapositivas.
- 12 escenas PNG con canal alfa.
- Figuras profesionales blancas y doradas completamente vestidas.
- Fondo negro grafito y franja superior dorada.
- Composiciones para portada, proceso, finanzas, comparación, jerarquía, diagnóstico, ciclo,
  riesgos, hoja de ruta, deliberación, implementación y texto largo.
- Ninguna escena contiene texto rasterizado.
- Los cuadros de texto de muestra permanecen editables dentro de PowerPoint.

## Pruebas superadas

- validador integral `validar_sistema_visual.py` aprobado;
- validador estructural de skills aprobado;
- catálogos JSON completos, ordenados y sin identificadores duplicados;
- referencias cruzadas válidas entre familias, acabados, densidades y kits;
- vínculos Markdown y archivos obligatorios presentes;
- paquete PPTX íntegro, 12 diapositivas y sin hallazgos de geometría;
- renderizado y revisión individual de las 12 diapositivas;
- prueba de desbordamiento de PowerPoint aprobada;
- 12 imágenes PENO con resolución mínima y canal alfa declarados.

Ejecuta `python3 visuales-diplomado-ia/scripts/validar_sistema_visual.py` después de instalar
la skill en otra computadora. Debe responder `APROBADO` antes de utilizar o compartir la copia.
