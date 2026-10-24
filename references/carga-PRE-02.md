# Carga completa de recursos PRE-02

Las instrucciones, catálogos y scripts están disponibles en `extensions/PRE-02/visuales-diplomado-ia/MODULO.md`. El paquete original completo de 128 archivos, incluidas imágenes, plantillas y muestras, está incorporado en partes verificadas bajo `assets/PRE-02/`; no requiere acceso a la cuenta de origen.

Ejecutar `python scripts/preparar_PRE02.py` desde la raíz de la integradora. El comando verifica las partes, reconstruye el ZIP original, coteja sus 128 archivos, extrae una copia temporal segura y ejecuta el validador del sistema visual. Usar la ruta absoluta devuelta como raíz de los recursos; entrar en `visuales-diplomado-ia/` para trabajar con sus plantillas y referencias.

La opción `--zip /ruta/al/archivo.zip` permite usar una copia externa únicamente si coincide con el original registrado. Conservar intactos los archivos fuente y guardar los resultados del usuario fuera de la skill. Los archivos SKILL.md de origen se recuperan como MODULO.md para evitar instalar otras skills; el validador temporal adapta esa denominación.

La integridad y la validación estructural del sistema visual no aprueban un PowerPoint final. Renderizar y revisar cada diapositiva, su contenido y su presentación antes de entregarlo. No afirmar 2,500 imágenes incluidas: las combinaciones de familias son posibilidades generativas, no una cantidad de archivos existentes.
