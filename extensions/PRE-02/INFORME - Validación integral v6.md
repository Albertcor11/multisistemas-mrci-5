# Validación integral — versión 6

**Resultado: APROBADO**

## Sistema comprobado

- 50 familias escénicas `E01–E50`.
- 50 composiciones `C01–C50` y 2,500 combinaciones únicas.
- 50 acabados `S01–S50`.
- 6 densidades `D01–D06`.
- 20 familias editoriales `LT01–LT20`.
- 8 kits mixtos `KM01–KM08`.
- Formato visual unificado en 16:9.
- Texto semántico generado dentro de imágenes: ninguno; permanece editable en PowerPoint.

## Pruebas superadas

- catálogos JSON válidos, completos, ordenados y sin identificadores duplicados;
- referencias cruzadas válidas entre familias, acabados, densidades y kits;
- archivos obligatorios y enlaces Markdown presentes;
- cinco scripts con sintaxis válida;
- constructor 50 × 50 aprobado;
- selector de texto largo aprobado;
- planificador mixto `E`/`LT`/`NATIVA` aprobado;
- auditor hostil aprobado con texto idéntico;
- auditor hostil rechazó correctamente una omisión deliberada;
- copia transportable idéntica a la skill instalada;
- 50 maestros escénicos y 20 maestros de texto largo verificados en 1672 × 941, proporción 16:9.

Ejecuta `python3 visuales-diplomado-ia/scripts/validar_sistema_visual.py` después de instalarla
en otra computadora. Debe responder `APROBADO`.
