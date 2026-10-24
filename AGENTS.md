# Guía para agentes y desarrolladores

Este archivo explica cómo mantener el repositorio. No forma parte de las instrucciones de la skill: quien la *usa* sólo lee `SKILL.md`. Quien la *modifica* (persona o IA) debe leer esto antes de tocar nada.

## Qué es este repositorio

Una sola skill instalable, `multisistemas-mrci-5` (Multisistemas MRCI 5.0), que integra 17 módulos: 16 base dentro de un corpus empaquetado y PRE-02 como extensión. `SKILL.md` es la entrada y enruta cada encargo a un módulo rector; `references/mapa.md` lista los módulos y sus códigos (MRCI-00, EDI-01, DOC-03, etc.).

```
SKILL.md                    instrucciones de la skill (lo que lee la IA que la usa)
agents/openai.yaml          metadatos para Codex/OpenAI
references/                 guías raíz, inventarios y registros de cambios
scripts/abrir_corpus.py     extrae y verifica los 16 módulos base
scripts/reempaquetar_corpus.py  regenera el corpus tras editar módulos
scripts/preparar_PRE02.py   extrae y valida el paquete visual PRE-02
assets/corpus/parte-NN.bin  los 16 módulos, en un ZIP partido en piezas de 16 MB
assets/PRE-02/, extensions/PRE-02/  módulo PRE-02
```

## Lo que no es evidente

- **Los módulos no están a la vista.** Viven dentro de `assets/corpus/*.bin`, que juntas forman un ZIP cuyos miembros se llaman por su SHA-256. `references/inventario.json` relaciona cada ruta `modulos/...` con su huella. Editar los `.bin` a mano o el inventario por separado rompe la verificación.
- **`MODULO.md` = `SKILL.md` original.** Cada módulo era una skill independiente; su `SKILL.md` se guarda como `MODULO.md` para que exista una sola skill instalada. No renombrar esas menciones dentro de los textos: `SKILL.md` y `abrir_corpus.py --originales` ya resuelven la equivalencia.
- **PRE-02 está sellado.** `preparar_PRE02.py` exige que su ZIP coincida byte por byte con el original (`references/inventario-PRE-02.json`). No editar `assets/PRE-02/` ni los archivos de `extensions/PRE-02/` registrados ahí sin rediseñar esa verificación.
- **Nombres con acentos.** El inventario conserva algunas rutas en Unicode NFD. Comparar siempre en NFC sin reescribir las rutas registradas; `reempaquetar_corpus.py` ya lo hace.
- **Copias repetidas.** Los archivos de biblioteca común (`biblioteca/00-…` a `08-…`) se repiten en varios módulos (por ejemplo, `00-protocolo-realidad-fuentes.md` en los 16 y `05-marco-juridico-transversal-mexico.md` en 11), y hay copias de referencias en la raíz (`references/apa-mrci-mexico.md`, `controles-auditoria-apa.md`, `sistema-apa-mexico-catalogo.json`, `sistema-edicion-citas-apa-referencias.md`) que deben mantenerse sincronizadas con EDI-01. Al cambiar una, buscar las demás con `rg -l` o comparar hashes.
- **FIL-01 tiene su propia copia** de los motores editoriales en `pensamiento-filosofico-aplicado/vendor/`; no se actualiza sola cuando cambia EDI-01.

## Cómo modificar un módulo

1. Crear una rama: `git switch -c <nombre-descriptivo>`.
2. Extraer: `python3 scripts/abrir_corpus.py` imprime una carpeta temporal con `modulos/`.
3. Editar los archivos dentro de esa carpeta. Para archivos nuevos, colocarlos dentro de la carpeta del módulo correspondiente.
4. Si se ejecutan pruebas, usar `PYTHONDONTWRITEBYTECODE=1`; aun así el script ignora `__pycache__`, `.pyc`, `.pytest_cache` y `.DS_Store`.
5. Revisar qué detecta: `python3 scripts/reempaquetar_corpus.py <carpeta> --simular`.
6. Regenerar: `python3 scripts/reempaquetar_corpus.py <carpeta> --version <ID> --fecha AAAA-MM-DD --registro references/<registro>.md`. Borrar archivos exige `--permitir-borrados`.
7. Verificar: `python3 scripts/abrir_corpus.py --verificar` y volver a extraer para cotejar el contenido.
8. Escribir el registro en `references/registro-<tema>-<AAAA-MM>.md` y enlazarlo desde `SKILL.md` si cambia el comportamiento.
9. Commit en la rama, Pull Request hacia `main`, revisión y merge.

Los cambios en `SKILL.md`, `references/` o `scripts/` de la raíz se editan directamente, sin reempaquetar.

## Verificaciones antes de un Pull Request

- `python3 scripts/abrir_corpus.py --verificar` → `"ok": true`.
- `python3 scripts/preparar_PRE02.py` → validación aprobada.
- Pruebas de los motores editoriales tocados: `python3 <carpeta>/modulos/editorial-academico-cientifico-mrci/vendor/MRCI_Editorial_Local/motores/<motor>/pruebas/test_*.py`. Requieren `python-docx` y `lxml` para el motor Word.
- Enlaces relativos de los `.md` modificados resueltos desde la carpeta de cada archivo.

Problemas conocidos que ya existían en el original y no indican un error nuevo: las pruebas de los motores `03_estilo_latino` (falta `fuentes_controladas/MATRIZ_FUENTES_ESTILO_LATINO.csv`), `08_produccion_entrega` (falta el módulo `centro_operacion`) y `10_presentaciones_produccion_visual` (una falla).

## Decisiones vigentes del responsable

No revertirlas sin consultarlo:

- El manual APA de México se conserva como PDF escaneado en EDI-01, junto con su transcripción OCR (`Manual_APA_4_Mexico_2021_Texto.md`). Se cita como cuarta edición en español.
- Tablas Word con bandas alternas `#EAF4FB`/`#FFFFFF` (perfil `PERFIL_FORMATO_WORD_MRCI.json` 1.6.0), implementadas en `configure_table()` y verificadas por `audit_tables()`.
- La biblioteca autoral JAPR conserva su descripción completa.
- Ningún entregable menciona la metodología, la skill, los módulos ni los motores internos (`SKILL.md`, «Calidad de entrega»).
- El alcance es de 17 módulos; no recortarlo al importar mejoras de distribuciones parciales.

## Historial

| Fecha | Cambio | Detalle |
|---|---|---|
| 2026-09-30 | Versión base «Multisistema 5.0 Virgen» | Commit `b3ab404` |
| 2026-10-24 | Mejoras de investigación jurídica y editorial desde `mrci-5-investigacion-juridica-editorial` | [registro](references/registro-integracion-2026-10.md), PR #1 |
| 2026-10-24 | Guía de mantenimiento y `reempaquetar_corpus.py` | Este archivo, PR #2 |
| 2026-10-24 | Instrucciones de instalación por plataforma | `README.md`, PR #3 |

Agregar una fila por cada actualización.

## Repositorio y entorno

- GitHub: `Albertcor11/multisistemas-mrci-5` (privado). Trabajar en ramas y unir a `main` por Pull Request.
- Python 3.10 o posterior para los scripts; los motores pueden requerir `python-docx`, `lxml`, `Pillow`, `pdf2image`/Poppler, LibreOffice o Node, según `references/entorno-y-alcance.md`.
