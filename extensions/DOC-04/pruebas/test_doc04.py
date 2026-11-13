#!/usr/bin/env python3
"""Suite integral de pruebas funcionales y de no-conflicto para DOC-04.

Ejecutar desde la raíz del repositorio con:
    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest extensions/DOC-04/pruebas/test_doc04.py -v
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPO_ROOT = Path(__file__).resolve().parents[3]
ORQUESTADOR = REPO_ROOT / 'scripts/orquestador.py'
ABRIR_CORPUS = REPO_ROOT / 'scripts/abrir_corpus.py'
PREPARAR_PRE02 = REPO_ROOT / 'scripts/preparar_PRE02.py'
AUDITOR_DOC04 = REPO_ROOT / 'extensions/DOC-04/scripts/auditar_plantilla_docx.py'

PNG_MINIMO = (
    b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
    b'\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0'
    b'\x00\x00\x03\x01\x01\x00\xc9\xfe\x92\xef\x00\x00\x00\x00IEND\xaeB`\x82'
)


def construir_docx_prueba(
    ruta: Path,
    xml_parrafos_body: str,
    incluir_logo_y_header: bool = True,
    incluir_comentario: bool = False,
) -> None:
    """Construye un archivo .docx OOXML válido sin requerir librerías externas."""
    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '  <Default Extension="xml" ContentType="application/xml"/>',
        '  <Default Extension="png" ContentType="image/png"/>',
        '  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
    ]
    if incluir_logo_y_header:
        content_types.append(
            '  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
        )
    if incluir_comentario:
        content_types.append(
            '  <Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
        )
    content_types.append('</Types>')

    rels_raiz = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>'
    )

    doc_rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
    ]
    sect_pr = '<w:sectPr/>'
    if incluir_logo_y_header:
        doc_rels.append(
            '<Relationship Id="rIdHeader1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>'
        )
        sect_pr = (
            '<w:sectPr xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<w:headerReference w:type="default" r:id="rIdHeader1"/>'
            '</w:sectPr>'
        )
    doc_rels.append('</Relationships>')

    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<w:body>{xml_parrafos_body}{sect_pr}</w:body></w:document>'
    )

    header_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<w:p><w:r><w:t>Consultoría Técnica del Norte, S.C. | RFC: CTN180412AB1</w:t></w:r>'
        '<w:r><w:drawing><a:blip r:embed="rIdImg1"/></w:drawing></w:r></w:p></w:hdr>'
    )
    header_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rIdImg1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/logo_institucional.png"/>'
        '</Relationships>'
    )

    with zipfile.ZipFile(ruta, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', '\n'.join(content_types))
        zf.writestr('_rels/.rels', rels_raiz)
        zf.writestr('word/_rels/document.xml.rels', '\n'.join(doc_rels))
        zf.writestr('word/document.xml', document_xml)
        if incluir_logo_y_header:
            zf.writestr('word/header1.xml', header_xml)
            zf.writestr('word/_rels/header1.xml.rels', header_rels)
            zf.writestr('word/media/logo_institucional.png', PNG_MINIMO)
        if incluir_comentario:
            zf.writestr(
                'word/comments.xml',
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                '<w:comment w:id="0"><w:p><w:r><w:t>Revisar dato</w:t></w:r></w:p></w:comment>'
                '</w:comments>',
            )


def ejecutar_cli(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    import os
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=str(REPO_ROOT),
        env=env,
        capture_output=True,
        text=True,
    )


class TestDoc04FuncionalidadYNoConflicto(unittest.TestCase):
    """Verifica tanto la operación de DOC-04 como la ausencia de conflictos en el ecosistema."""

    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix='test_doc04_'))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    # =========================================================================
    # BLOQUE A: PRUEBAS FUNCIONALES DE DOC-04
    # =========================================================================

    def test_01_preservacion_logotipo_y_requisitado_sobre_copia(self) -> None:
        molde = self.tmpdir / 'FOR-01_molde.docx'
        entregable = self.tmpdir / 'FOR-01_requisitado.docx'

        # Molde con marcador [1] partido en múltiples runs
        construir_docx_prueba(
            molde,
            '<w:p><w:r><w:t>Contrato: </w:t></w:r>'
            '<w:r><w:t>[</w:t></w:r><w:r><w:t>1</w:t></w:r><w:r><w:t>]</w:t></w:r></w:p>',
            incluir_logo_y_header=True,
        )

        # Copia quirúrgica preservando header1.xml y word/media/logo_institucional.png
        shutil.copy2(molde, entregable)
        with zipfile.ZipFile(molde, 'r') as zin:
            entradas = {n: zin.read(n) for n in zin.namelist()}
        entradas['word/document.xml'] = (
            entradas['word/document.xml']
            .decode('utf-8')
            .replace('<w:r><w:t>[</w:t></w:r><w:r><w:t>1</w:t></w:r><w:r><w:t>]</w:t></w:r>', '<w:r><w:t>CON-2026-084</w:t></w:r>')
            .encode('utf-8')
        )
        with zipfile.ZipFile(entregable, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for nombre, contenido in entradas.items():
                zout.writestr(nombre, contenido)

        proc = ejecutar_cli(AUDITOR_DOC04, str(entregable), '--molde', str(molde))
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        data = json.loads(proc.stdout)
        self.assertTrue(data['ok'])
        self.assertEqual(data['dictamen_mpro'], 'CONFORME')
        self.assertEqual(data['estado_operativo'], 'REQUIERE_VALIDACION_HUMANA')
        self.assertTrue(data['comparacion_molde']['preservado'])

    def test_02_bloquea_perdida_de_logotipo_o_encabezado(self) -> None:
        molde = self.tmpdir / 'FOR-01_molde.docx'
        recreado_sin_logo = self.tmpdir / 'FOR-01_recreado_en_blanco.docx'

        construir_docx_prueba(molde, '<w:p><w:r><w:t>[1]</w:t></w:r></w:p>', incluir_logo_y_header=True)
        construir_docx_prueba(
            recreado_sin_logo,
            '<w:p><w:r><w:t>CON-2026-084</w:t></w:r></w:p>',
            incluir_logo_y_header=False,
        )

        proc = ejecutar_cli(AUDITOR_DOC04, str(recreado_sin_logo), '--molde', str(molde))
        self.assertNotEqual(proc.returncode, 0)
        data = json.loads(proc.stdout)
        self.assertFalse(data['ok'])
        self.assertEqual(data['severidad_maxima'], 'Crítico')
        self.assertEqual(data['dictamen_mpro'], 'NO CONFORME')
        self.assertFalse(data['comparacion_molde']['preservado'])

    def test_03_detecta_marcadores_residuales_incluso_en_runs_fragmentados(self) -> None:
        doc_sucio = self.tmpdir / 'borrador_con_residuos.docx'
        construir_docx_prueba(
            doc_sucio,
            '<w:p><w:r><w:t>Destinatario: [</w:t></w:r><w:r><w:t>Ej. Empresa Muestra</w:t></w:r><w:r><w:t>]</w:t></w:r></w:p>'
            '<w:p><w:r><w:t>Importe: {{monto_total}}</w:t></w:r></w:p>',
        )
        proc = ejecutar_cli(AUDITOR_DOC04, str(doc_sucio))
        self.assertNotEqual(proc.returncode, 0)
        data = json.loads(proc.stdout)
        self.assertFalse(data['ok'])
        self.assertGreaterEqual(len(data['marcadores_residuales']), 2)

    def test_04_control_de_pendientes_definitivo_vs_borrador(self) -> None:
        doc_pend = self.tmpdir / 'avance_con_pendiente.docx'
        construir_docx_prueba(
            doc_pend,
            '<w:p><w:r><w:t>Registro vigente: [PENDIENTE: número de registro patronal]</w:t></w:r></w:p>',
        )

        # Sin --permitir-pendientes se bloquea para entrega definitiva
        proc_def = ejecutar_cli(AUDITOR_DOC04, str(doc_pend))
        self.assertNotEqual(proc_def.returncode, 0)
        data_def = json.loads(proc_def.stdout)
        self.assertEqual(data_def['dictamen_mpro'], 'NO CONFORME')

        # Con --permitir-pendientes aprueba como BORRADOR_PARA_REVISION
        proc_borr = ejecutar_cli(AUDITOR_DOC04, str(doc_pend), '--permitir-pendientes')
        self.assertEqual(proc_borr.returncode, 0, msg=proc_borr.stdout)
        data_borr = json.loads(proc_borr.stdout)
        self.assertTrue(data_borr['ok'])
        self.assertEqual(data_borr['estado_operativo'], 'BORRADOR_PARA_REVISION')
        self.assertEqual(data_borr['dictamen_mpro'], 'CONFORME CON OBSERVACIONES')
        self.assertIn('número de registro patronal', data_borr['pendientes_declarados'])

    def test_05_ficha_maestra_residuos_previos_y_consistencia_transversal(self) -> None:
        ficha_json = self.tmpdir / 'ficha_maestra.json'
        ficha_json.write_text(
            json.dumps({
                'valores_obligatorios': ['Ingeniería Industrial del Bajío, S.A. de C.V.', 'CON-2026-084', '$145,000.00 MXN'],
                'residuos_prohibidos': ['Comercializadora Antiguo Cliente, S.A.', 'AAA010101AAA'],
                'atributos_transversales': {
                    'folio_contrato': 'CON-2026-084',
                    'importe_total': '$145,000.00 MXN',
                },
            }, ensure_ascii=False),
            encoding='utf-8',
        )

        doc_tecnico = self.tmpdir / '01_analisis_interno.md'
        doc_externo = self.tmpdir / '02_requerimiento_proveedor.md'
        doc_directivo = self.tmpdir / '03_nota_direccion.md'

        doc_tecnico.write_text(
            'Revisión de Ingeniería Industrial del Bajío, S.A. de C.V., contrato CON-2026-084 por $145,000.00 MXN.',
            encoding='utf-8',
        )
        doc_externo.write_text(
            'En relación con el contrato CON-2026-084, se condiciona el pago de $145,000.00 MXN a la entrega del comprobante bancario.',
            encoding='utf-8',
        )
        doc_directivo.write_text(
            'Resumen ejecutivo contrato CON-2026-084: retener $145,000.00 MXN hasta recibir soporte bancario.',
            encoding='utf-8',
        )

        # Paquete consistente y limpio
        proc_ok = ejecutar_cli(
            AUDITOR_DOC04,
            str(doc_tecnico),
            '--ficha-json', str(ficha_json),
            '--paquete', str(doc_externo), str(doc_directivo),
        )
        self.assertEqual(proc_ok.returncode, 0, msg=proc_ok.stdout)

        # Discrepancia transversal de monto en la nota directiva -> bloquea
        doc_directivo.write_text(
            'Resumen ejecutivo contrato CON-2026-084: retener $154,000.00 MXN hasta recibir soporte bancario.',
            encoding='utf-8',
        )
        proc_err = ejecutar_cli(
            AUDITOR_DOC04,
            str(doc_tecnico),
            '--ficha-json', str(ficha_json),
            '--paquete', str(doc_externo), str(doc_directivo),
        )
        self.assertNotEqual(proc_err.returncode, 0)
        data_err = json.loads(proc_err.stdout)
        self.assertTrue(data_err['validacion_ficha_maestra']['inconsistencias_transversales'])

        # Residuo de cliente anterior arrastrado por accidente -> bloquea
        doc_con_residuo = self.tmpdir / '04_con_residuo.md'
        doc_con_residuo.write_text(
            'Ingeniería Industrial del Bajío, S.A. de C.V., contrato CON-2026-084 por $145,000.00 MXN. RFC previo: AAA010101AAA.',
            encoding='utf-8',
        )
        proc_res = ejecutar_cli(AUDITOR_DOC04, str(doc_con_residuo), '--ficha-json', str(ficha_json))
        self.assertNotEqual(proc_res.returncode, 0)
        data_res = json.loads(proc_res.stdout)
        self.assertIn('AAA010101AAA', data_res['validacion_ficha_maestra']['residuos_asunto_previo_detectados'])

    # =========================================================================
    # BLOQUE B: PRUEBAS DE NO-CONFLICTO Y CERO REGRESIÓN EN EL MULTISISTEMA
    # =========================================================================

    def test_06_integridad_global_orquestador_corpus_y_pre02(self) -> None:
        proc_ver = ejecutar_cli(ORQUESTADOR, 'verificar')
        self.assertEqual(proc_ver.returncode, 0, msg=proc_ver.stdout + proc_ver.stderr)
        ver = json.loads(proc_ver.stdout)
        self.assertTrue(ver['ok'])
        self.assertEqual(ver['total_miniskills'], 19)
        self.assertEqual(ver['archivos_locales_faltantes'], [])
        self.assertTrue(ver['corpus_base']['ok'])
        self.assertEqual(ver['corpus_base']['modules'], 16)
        self.assertEqual(ver['corpus_base']['files'], 908)

        proc_pre02 = ejecutar_cli(PREPARAR_PRE02)
        self.assertEqual(proc_pre02.returncode, 0, msg=proc_pre02.stdout + proc_pre02.stderr)

    def test_07_no_conflicto_enrutamiento_en_las_otras_18_miniskills(self) -> None:
        """Verifica que DOC-04 nunca secuestre encargos propios de las otras 18 mini-skills."""
        casos_ajenos = [
            ('MRCI-00', 'Atiende un asunto jurídico y fiscal de cumplimiento PLD con estrategia integral'),
            ('MUN-01', 'Revisa el cobro de predial y servicios públicos en la hacienda municipal del ayuntamiento'),
            ('INM-01', 'Analiza un contrato de compraventa y fideicomiso inmobiliario ante registro público y catastro'),
            ('SEG-01', 'Evalúa rechazo de siniestro y cobertura de póliza de seguros ante CONDUSEF bajo la LCS'),
            ('JUD-01', 'Elabora un proyecto de sentencia imparcial con proyección jurisdiccional para magistrado'),
            ('JUD-02', 'Diseña demanda de amparo con conceptos de violación y precedentes de jurisprudencia'),
            ('FIL-01', 'Desarrolla un análisis filosófico de epistemología, ética y hermenéutica'),
            ('EDU-01', 'Integra plan de estudios y programa de asignatura de licenciatura para RVOE ante la SEP'),
            ('ARC-01', 'Define la arquitectura de sistemas, ADR y constitución arquitectónica del ecosistema'),
            ('AGT-01', 'Diseña un prompt de sistema y kernel de instrucciones para un agente especializado'),
            ('AGT-02', 'Configura la coordinación de agentes multi-agente y protocolo de arbitraje del orquestador'),
            ('EDI-01', 'Escribe un capítulo de libro y protocolo de tesis con formato de word académico'),
            ('APA-MX', 'Realiza auditoría APA de citas, paráfrasis y referencias bibliográficas con Manual Moderno'),
            ('PRE-01', 'Prepara una presentación ejecutiva con diapositivas y slides para exposición'),
            ('PRE-02', 'Convierte este texto a PowerPoint pptx con fidelidad literal y escenas portadoras PENO-01'),
            ('DOC-01', 'Organiza la catalogación y custodia documental del acervo en la biblioteca institucional'),
            ('DOC-02', 'Redacta un dictamen y acta bajo estándares de producción documental y formato institucional'),
            ('DOC-03', 'Audita la cadena de custodia, evidencia y materialidad del expediente probatorio'),
        ]

        for esperado, encargo in casos_ajenos:
            with self.subTest(miniskill=esperado):
                proc = ejecutar_cli(ORQUESTADOR, 'enrutar', encargo)
                self.assertEqual(proc.returncode, 0, msg=proc.stderr)
                res = json.loads(proc.stdout)
                recomendadas = res['miniskills_recomendadas']
                self.assertIn(esperado, recomendadas, f'{esperado} no se activó para: {encargo}')
                self.assertNotIn(
                    'DOC-04',
                    recomendadas,
                    f'Falso positivo: DOC-04 invadió un encargo propio de {esperado}: {encargo}',
                )

    def test_08_enrutamiento_y_activacion_doc04_preserva_rector_sustantivo(self) -> None:
        # 1) Encargo puro de formato DOC-04: el orquestador antepone MRCI-00 como respaldo sustantivo
        proc_puro = ejecutar_cli(
            ORQUESTADOR,
            'enrutar',
            'Convierte nuestro molde word en plantilla propia reutilizable con ficha de requisitado y campos variables',
        )
        self.assertEqual(proc_puro.returncode, 0)
        res_puro = json.loads(proc_puro.stdout)
        self.assertEqual(res_puro['miniskills_recomendadas'][0], 'MRCI-00')
        self.assertIn('DOC-04', res_puro['miniskills_recomendadas'])

        # 2) Encargo combinado con especialista sustantivo (SEG-01 + DOC-04)
        proc_mix = ejecutar_cli(
            ORQUESTADOR,
            'enrutar',
            'Para una reclamación de siniestro y póliza de seguro, requisitar nuestra plantilla propia validando contra la ficha maestra con consistencia transversal',
        )
        self.assertEqual(proc_mix.returncode, 0)
        res_mix = json.loads(proc_mix.stdout)
        self.assertIn('SEG-01', res_mix['miniskills_recomendadas'])
        self.assertIn('DOC-04', res_mix['miniskills_recomendadas'])

        # 3) Activación real con extracción selectiva de CORE + DOC-02 + DOC-04
        proc_act = ejecutar_cli(ORQUESTADOR, 'activar', 'MRCI-00', 'DOC-04', 'DOC-02')
        self.assertEqual(proc_act.returncode, 0, msg=proc_act.stderr)
        act = json.loads(proc_act.stdout)
        self.assertTrue(act['ok'])
        for ruta_core in act['nucleo_transversal']:
            self.assertTrue(Path(ruta_core).is_file(), f'Falta archivo CORE extraído: {ruta_core}')
        self.assertTrue(Path(act['miniskills_activas']['DOC-04']['entrada_absoluta']).is_file())
        self.assertTrue(Path(act['miniskills_activas']['DOC-02']['entrada_absoluta']).is_file())

    def test_09_compatibilidad_con_compuerta_auditar_anonimato(self) -> None:
        # Entregable limpio con datos empresariales y un [PENDIENTE: ...] legítimo -> APROBADO_PARA_ENTREGA
        borrador_limpio = self.tmpdir / 'entregable_capa1_limpio.docx'
        construir_docx_prueba(
            borrador_limpio,
            '<w:p><w:r><w:t>Por medio del presente se requiere el comprobante bancario de pago. '
            'Folio registral: [PENDIENTE: número de escritura constitutiva].</w:t></w:r></w:p>',
        )
        proc_ok = ejecutar_cli(ORQUESTADOR, 'auditar', str(borrador_limpio))
        self.assertEqual(proc_ok.returncode, 0, msg=proc_ok.stdout)
        self.assertEqual(json.loads(proc_ok.stdout)['estado'], 'APROBADO_PARA_ENTREGA')

        # Si se filtrara la marca interna DOC-04 en Capa 1 -> ENTREGA_BLOQUEADA automáticamente
        entregable_filtrado = self.tmpdir / 'entregable_con_fuga_interna.docx'
        construir_docx_prueba(
            entregable_filtrado,
            '<w:p><w:r><w:t>Documento validado con la extensión DOC-04 del sistema.</w:t></w:r></w:p>',
        )
        proc_blk = ejecutar_cli(ORQUESTADOR, 'auditar', str(entregable_filtrado))
        self.assertNotEqual(proc_blk.returncode, 0)
        rep_blk = json.loads(proc_blk.stdout)
        self.assertEqual(rep_blk['estado'], 'ENTREGA_BLOQUEADA')
        self.assertIn('DOC-04', rep_blk['filtraciones_metodologia_interna'])

    def test_10_coherencia_documental_enlaces_y_ausencia_reglas_conflictivas(self) -> None:
        archivos_md_revisar = [
            REPO_ROOT / 'SKILL.md',
            REPO_ROOT / 'AGENTS.md',
            REPO_ROOT / 'references/mapa.md',
            REPO_ROOT / 'references/miniskill-doc04.md',
            REPO_ROOT / 'references/registro-doc04-2026-11.md',
            REPO_ROOT / 'extensions/DOC-04/MODULO.md',
            REPO_ROOT / 'extensions/DOC-04/references/parametrizacion-y-requisitado.md',
            REPO_ROOT / 'extensions/DOC-04/references/incorporacion-formatos-usuario.md',
            REPO_ROOT / 'extensions/DOC-04/references/adaptacion-y-consistencia-transversal.md',
            REPO_ROOT / 'extensions/DOC-04/references/validacion-ficha-maestra-y-pendientes.md',
        ]
        patron_link = re.compile(r'\[[^\]]+\]\(([^)#\s]+)(?:#[^)]*)?\)')

        residuos_aula_prohibidos = ('divm', 'exp-00', 'exp-12', 'arr20518', '#1b365d')

        for archivo in archivos_md_revisar:
            self.assertTrue(archivo.is_file(), f'No existe el archivo esperado: {archivo}')
            contenido = archivo.read_text(encoding='utf-8')
            # Quitar bloques de código cercados antes de validar enlaces reales
            sin_codigo = re.sub(r'```.*?```', '', contenido, flags=re.DOTALL)
            for match in patron_link.finditer(sin_codigo):
                destino = match.group(1)
                if destino.startswith(('http://', 'https://', 'mailto:')):
                    continue
                ruta_resuelta = (archivo.parent / destino).resolve()
                self.assertTrue(
                    ruta_resuelta.exists(),
                    f'Enlace relativo roto en {archivo.relative_to(REPO_ROOT)}: {destino} -> {ruta_resuelta}',
                )

            if 'DOC-04' in str(archivo) or archivo.name in ('miniskill-doc04.md', 'registro-doc04-2026-11.md'):
                lower = contenido.lower()
                for residuo in residuos_aula_prohibidos:
                    self.assertNotIn(
                        residuo,
                        lower,
                        f'Residuo didáctico o color en conflicto "{residuo}" detectado en {archivo.name}',
                    )


if __name__ == '__main__':
    unittest.main()
