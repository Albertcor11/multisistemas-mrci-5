# Multisistemas MRCI 5.0

Skill de inteligencia artificial que integra 17 módulos especializados: jurídico, fiscal, municipal, inmobiliario, asegurador, jurisdiccional, filosófico, editorial y académico (APA México), educativo, documental, presentaciones y diseño de agentes. Ante cada encargo elige el módulo adecuado y entrega resultados con fuentes verificables.

Esta guía explica cómo instalarla. Si vas a **modificar** el proyecto, lee [AGENTS.md](AGENTS.md).

## Antes de empezar

**1. Acceso al repositorio.** El repositorio es privado. El dueño debe invitarte desde GitHub (**Settings → Collaborators → Add people**). Acepta la invitación que llega a tu correo y entra a GitHub con esa cuenta.

**2. Dónde funciona completa.** Los 16 módulos base vienen comprimidos y la skill los abre ejecutando Python. Por eso funciona completa sólo donde la IA puede ejecutar código:

| Plataforma | Funciona | Sección |
|---|---|---|
| Claude Code (terminal, VS Code, app de escritorio) | Completa | [Opción A](#opción-a-claude-code) |
| Codex de OpenAI | Completa | [Opción B](#opción-b-codex-de-openai) |
| Claude.ai (web o app) | Completa, si tu cuenta permite subir skills y tiene la ejecución de código activada | [Opción C](#opción-c-claudeai-web-o-app) |
| ChatGPT web | Parcial, sin instalación: por conversación | [Opción D](#opción-d-chatgpt-web) |
| Gemini | Parcial: Gemini CLI puede leerla en una carpeta | [Opción E](#opción-e-gemini-cli) |

**3. Python.** En tu computadora (opciones A, B y E) necesitas Python 3.10 o posterior. Compruébalo en la terminal con `python3 --version` (en Windows, `python --version`). Si no lo tienes, descárgalo de [python.org](https://www.python.org/downloads/).

## Descargar la skill

Elige una de las dos formas.

**Con Git** (recomendada, porque después se actualiza con un comando). Requiere [Git](https://git-scm.com/downloads) y haber iniciado sesión en GitHub (por ejemplo con [GitHub Desktop](https://desktop.github.com/) o `gh auth login`). El comando exacto aparece en cada opción.

**Sin Git.** En la página del repositorio pulsa **Code → Download ZIP** y descomprime el archivo con el explorador de tu sistema (doble clic en Mac, «Extraer todo» en Windows). La carpeta resultante se llama `multisistemas-mrci-5-main`: **cámbiale el nombre a `multisistemas-mrci-5`**.

En cualquier caso, la carpeta final debe tener `SKILL.md` directamente adentro, no en una subcarpeta:

```
multisistemas-mrci-5/
├── SKILL.md
├── assets/
├── references/
└── scripts/
```

## Opción A: Claude Code

1. Copia la skill en tu carpeta de skills personales.

   Mac o Linux:
   ```bash
   git clone https://github.com/Albertcor11/multisistemas-mrci-5.git ~/.claude/skills/multisistemas-mrci-5
   ```
   Windows (PowerShell):
   ```powershell
   git clone https://github.com/Albertcor11/multisistemas-mrci-5.git "$HOME\.claude\skills\multisistemas-mrci-5"
   ```
   Sin Git: mueve la carpeta `multisistemas-mrci-5` a `~/.claude/skills/` (en Windows, `C:\Users\TU_USUARIO\.claude\skills\`). Si la carpeta `skills` no existe, créala.

2. Verifica que llegó completa:
   ```bash
   cd ~/.claude/skills/multisistemas-mrci-5
   python3 scripts/abrir_corpus.py --verificar
   ```
   Debe responder `"ok": true` con `"files": 908`.

3. Abre una sesión **nueva** de Claude Code y pide algo como: *«Usa multisistemas-mrci-5 para analizar este asunto…»*. También se activa sola cuando el encargo corresponde a sus áreas.

Atajo: también puedes pedirle a Claude Code *«Instala esta skill en mis skills personales: https://github.com/Albertcor11/multisistemas-mrci-5»*; Claude hará el clonado por ti si tu GitHub tiene acceso al repositorio.

## Opción B: Codex de OpenAI

La skill ya incluye `agents/openai.yaml`, el archivo que Codex usa para mostrarla.

1. Clona la skill en la carpeta de skills de Codex (por defecto `~/.codex/skills/`; si tu versión usa otra ruta, consúltala en la documentación de Codex):
   ```bash
   git clone https://github.com/Albertcor11/multisistemas-mrci-5.git ~/.codex/skills/multisistemas-mrci-5
   ```
2. Verifica como en la opción A, paso 2.
3. Abre una sesión nueva de Codex e invócala con `$multisistemas-mrci-5`.

## Opción C: Claude.ai (web o app)

1. Descarga el ZIP (**Code → Download ZIP**), descomprímelo, cambia el nombre de la carpeta a `multisistemas-mrci-5` y vuelve a comprimir **esa carpeta** en un ZIP (clic derecho → Comprimir, o «Enviar a → Carpeta comprimida» en Windows).
2. En Claude.ai abre **Configuración → Capacidades**, confirma que la ejecución de código esté activada y, en la sección de **Skills**, sube el ZIP. Los nombres exactos del menú pueden variar según tu plan y versión.
3. En una conversación nueva, pide: *«Usa multisistemas-mrci-5 para…»*.

El ZIP pesa unos 180 MB. Si Claude.ai lo rechaza por tamaño, usa la opción A o B.

## Opción D: ChatGPT web

ChatGPT web no instala skills de este formato. Funciona por conversación, siempre que tu cuenta tenga análisis de datos (ejecución de Python) y permita subir un archivo de ese tamaño:

1. Descarga el ZIP del repositorio (**Code → Download ZIP**).
2. En una conversación nueva, súbelo y pega:
   > Descomprime este ZIP. Dentro está la skill multisistemas-mrci-5. Lee su SKILL.md y síguelo como tus instrucciones para esta conversación. Cuando necesites los módulos, ejecuta `python scripts/abrir_corpus.py` desde la carpeta de la skill, como indica SKILL.md. Mi encargo es: …
3. Repite estos pasos en cada conversación nueva.

## Opción E: Gemini CLI

Gemini no usa este formato de skills; en la versión web no funciona completa. Con [Gemini CLI](https://github.com/google-gemini/gemini-cli):

1. Clona el repositorio en cualquier carpeta y entra en ella:
   ```bash
   git clone https://github.com/Albertcor11/multisistemas-mrci-5.git
   cd multisistemas-mrci-5
   ```
2. Ejecuta `gemini` y pide: *«Lee SKILL.md y síguelo como tus instrucciones. Mi encargo es: …»*.

## Actualizar a una nueva versión

- Con Git, entra a la carpeta de la skill y ejecuta `git pull`. Después repite la verificación (`python3 scripts/abrir_corpus.py --verificar`).
- Sin Git, descarga el ZIP de nuevo y reemplaza la carpeta completa.

Los cambios de cada versión están en `references/registro-*.md` y en el historial de [AGENTS.md](AGENTS.md#historial).

## Problemas frecuentes

| Problema | Solución |
|---|---|
| La IA no reconoce la skill | Revisa que `SKILL.md` esté directamente dentro de `multisistemas-mrci-5/` y abre una sesión nueva. |
| `Repository not found` al clonar | No tienes acceso: acepta la invitación del dueño o inicia sesión en GitHub con la cuenta invitada. |
| `python3: command not found` | Instala Python 3.10 o posterior; en Windows usa `python` en lugar de `python3`. |
| La verificación no da `"ok": true` | La descarga quedó incompleta o se modificó un archivo de `assets/`: vuelve a descargar. |
| Error con nombres que llevan acentos al descomprimir | Descomprime con el explorador del sistema (Finder o Explorador de Windows), no con herramientas antiguas de terminal. |
