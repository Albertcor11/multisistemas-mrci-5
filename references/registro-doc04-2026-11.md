# Registro de integración · noviembre de 2026 (`DOC-04`)

Origen funcional: capacidades formales y agnósticas de parametrización de plantillas, incorporación de moldes institucionales con logotipo, adaptación multi-destinatario con consistencia transversal y validación contra ficha maestra, integradas como extensión modular `DOC-04` (`plantillas-y-consistencia-documental`) sin modificar los paquetes binarios sellados (`assets/corpus/*.bin` ni `assets/PRE-02/`). Fecha: 12 de noviembre de 2026.

Verificar integridad con `python3 scripts/orquestador.py verificar`, `python3 scripts/abrir_corpus.py --verificar` y `python3 scripts/preparar_PRE02.py`.

## Decisiones de armonización arquitectónica

- **Frontera con `DOC-02` (`MPRO`):** `DOC-02` conserva la rectoría sobre los documentos normativos internos del ecosistema MRCI (7 secciones obligatorias de `MPRO_0100`). `DOC-04` regula formatos externos del usuario y paquetes requisitados, adoptando sin taxonomías paralelas el ciclo de vida de catálogo (`PROPUESTO → EN PRODUCCIÓN → EN REVISIÓN → VIGENTE → SUPERADO → RETIRADO`), las cuatro severidades (`Crítico`, `Mayor`, `Menor`, `Observación`) y los tres resultados de dictamen (`CONFORME`, `CONFORME CON OBSERVACIONES`, `NO CONFORME`).
- **Frontera con `REDO` y motores Word de `EDI-01`:** `REDO` conserva la redacción jurídica libre y control de cambios; `DOC-04` cubre específicamente campos `[1]…[N]` con Ficha de Requisitado de 6 columnas, catálogo externo `<codigo>.docx` + `<codigo>.md`, Tabla de Consistencia Transversal multi-destinatario y cruce campo por campo contra Ficha de Datos Maestros. Cuando el usuario aporta un molde `.docx`, su diseño y logotipos prevalecen al 100% (`shutil.copy2` + edición localizada); sin molde `.docx` del usuario, rige el perfil del módulo rector (como `PERFIL_FORMATO_WORD_MRCI.json` v1.6.0 en `EDI-01`), sin introducir paletas competidoras.
- **Operación con datos reales e higiene del repositorio:** en operación, `DOC-04` procesa datos reales del usuario, su despacho y sus clientes sin restricción; al convertir un documento previo en plantilla reutilizable sólo depura residuos del cliente/asunto anterior y conserva intacta la identidad fija real del titular del formato. Los ejemplos internos de las guías en el repositorio emplean datos sintéticos neutros.
- **Dos capas, almacenamiento externo y anonimato:** el catálogo de plantillas del usuario se guarda siempre fuera del árbol de la skill (`<carpeta_trabajo>/plantillas_usuario/`). Los entregables de Capa 1 nunca incluyen códigos internos (`DOC-04`, `MRCI`, `MPRO`, `JAPR`) ni tablas de auditoría, las cuales se emiten por separado en la Cédula Interna de Control (Capa 2).

## Cambios incorporados

| Tipo | Archivo | Cambio |
|---|---|---|
| NUEVO | `extensions/DOC-04/MODULO.md` | Instrucciones maestras de `DOC-04`: alcance, fronteras con `DOC-02`/`REDO`/`EDI-01`, operación dual (con y sin Python), Dos Capas y almacenamiento externo. |
| NUEVO | `extensions/DOC-04/references/parametrizacion-y-requisitado.md` | Descomposición en 5 categorías, numeración `[1]…[N]`, Ficha de Requisitado de 6 columnas, abstención controlada y pruebas A/B/Incompleto. |
| NUEVO | `extensions/DOC-04/references/incorporacion-formatos-usuario.md` | Despersonalización selectiva de residuos previos conservando identidad del titular, requisitado quirúrgico `.docx` y versionado semántico `X.Y.Z` con análisis de impacto. |
| NUEVO | `extensions/DOC-04/references/adaptacion-y-consistencia-transversal.md` | Reglas de transformación por perfil de destinatario y Tabla de Consistencia Transversal obligatoria en Cédula Interna. |
| NUEVO | `extensions/DOC-04/references/validacion-ficha-maestra-y-pendientes.md` | Prelación de Ficha Maestra, separación *aportado vs. mencionado/en trámite/línea de captura sin pago*, higiene de marcadores y severidades `MPRO`. |
| NUEVO | `extensions/DOC-04/scripts/auditar_plantilla_docx.py` | Verificador estándar en Python (sin dependencias externas) de preservación de logotipos/medios, cero corchetes residuales, control de `[PENDIENTE: ...]` y paridad contra ficha maestra. |
| NUEVO | `extensions/DOC-04/pruebas/test_doc04.py` | Suite automatizada de pruebas funcionales de `DOC-04` y pruebas de no-conflicto / no-regresión frente al resto del multisistema. |
| NUEVO | `references/miniskill-doc04.md` | Ficha modular de carga bajo demanda en raíz para `DOC-04`. |
| MODIFICADO | `references/catalogo-orquestador.json` | Alta de `DOC-04` (`capa: formato`) con `archivos_locales` verificables y reciprocidad en `apoyos_sugeridos` de `DOC-02`. |
| MODIFICADO | `SKILL.md` | Actualización de 18 a 19 mini-skills, incorporación de `DOC-04` en la tabla de selección (§2) y en fichas bajo demanda (§3). |
| MODIFICADO | `references/mapa.md` | Sección de acceso directo para la extensión `DOC-04`. |
| MODIFICADO | `AGENTS.md` | Actualización de referencia al catálogo (19 mini-skills) y registro en `## Historial`. |
