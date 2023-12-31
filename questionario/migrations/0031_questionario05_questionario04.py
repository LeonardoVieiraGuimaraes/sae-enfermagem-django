# Generated by Django 4.2.3 on 2023-07-28 19:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0002_alter_usuario_cpf_alter_usuario_data_nascimento_and_more"),
        ("questionario", "0030_alter_questionario0304_data_atualizacao_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Questionario05",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuario.paciente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Questionario04",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "admissao_obstetrica",
                    models.CharField(
                        choices=[
                            ("Risco Habitual", "Risco Habitual"),
                            ("Alto Risco", "Alto Risco"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Admissão Obstétrica",
                    ),
                ),
                (
                    "data_adminissao",
                    models.DateField(
                        default="", max_length=30, verbose_name="Data de Admissão"
                    ),
                ),
                (
                    "hora_admissao",
                    models.TimeField(
                        default="", max_length=30, verbose_name="Hora de Admissão"
                    ),
                ),
                (
                    "admissao_obstetrica_motivo",
                    models.CharField(default="", max_length=30, verbose_name="Motivo"),
                ),
                (
                    "alergias",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Alergias",
                    ),
                ),
                (
                    "alergias_descricao",
                    models.CharField(
                        default="", max_length=30, verbose_name="Descrição:"
                    ),
                ),
                (
                    "antecedentes_pessoais_patologicos",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("HAS", "HAS"),
                            ("Diabetes", "Diabetes"),
                            ("Síndrome hipertensiva", "Síndrome hipertensiva"),
                            ("Hemorragia", "Hemorragia "),
                            ("Etilismo", "Etilismo"),
                            ("Tabagismo", "Tabagismo"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Antecedentes Pessoais e Patológicos",
                    ),
                ),
                (
                    "gesta",
                    models.CharField(default="", max_length=30, verbose_name="Gesta"),
                ),
                (
                    "para",
                    models.CharField(default="", max_length=30, verbose_name="Para"),
                ),
                ("ab", models.CharField(default="", max_length=30, verbose_name="AB")),
                ("pn", models.CharField(default="", max_length=30, verbose_name="PN")),
                (
                    "filhos_vivos",
                    models.CharField(
                        default="", max_length=30, verbose_name="Filhos Vivos"
                    ),
                ),
                (
                    "dum",
                    models.CharField(default="", max_length=30, verbose_name="DUM"),
                ),
                (
                    "usg",
                    models.CharField(default="", max_length=30, verbose_name="USG"),
                ),
                (
                    "trimestre",
                    models.CharField(
                        default="", max_length=30, verbose_name="Trimestre"
                    ),
                ),
                (
                    "dpp",
                    models.DateField(default="", max_length=30, verbose_name="DPP"),
                ),
                (
                    "realizou_pre_natal",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Realizou Pré-Natal",
                    ),
                ),
                (
                    "realizou_visita_vinculacao_maternidade",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Realizou Visita de Vinculação à Maternidade",
                    ),
                ),
                (
                    "realizou_visita_vinculacao_maternidade_motivo",
                    models.CharField(default="", max_length=30, verbose_name="Motivo"),
                ),
                (
                    "estratificacao_risco_hpp",
                    models.CharField(
                        choices=[
                            ("Baixo", "Baixo"),
                            ("Médio", "Médio"),
                            ("Alto", "Alto"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Estratificação de Risco para HPP",
                    ),
                ),
                (
                    "medicamentos_uso",
                    models.CharField(
                        default="", max_length=30, verbose_name="Medicamentos em Uso"
                    ),
                ),
                (
                    "exames_complementares",
                    models.CharField(
                        default="", max_length=30, verbose_name="Exames Complementares"
                    ),
                ),
                (
                    "pas",
                    models.CharField(default="", max_length=30, verbose_name="PAS"),
                ),
                ("fc", models.CharField(default="", max_length=30, verbose_name="FC")),
                (
                    "temp",
                    models.CharField(default="", max_length=30, verbose_name="Temp"),
                ),
                ("fr", models.CharField(default="", max_length=30, verbose_name="FR")),
                (
                    "edemas_mmii",
                    models.CharField(
                        default="", max_length=30, verbose_name="Edemas MMII"
                    ),
                ),
                (
                    "dinamica_uterina",
                    models.CharField(
                        choices=[("ausente", "ausente"), ("presente", "presente")],
                        default="",
                        max_length=30,
                        verbose_name="Dinâmica Uterina",
                    ),
                ),
                (
                    "dinamica_uterina_contracoes",
                    models.IntegerField(default=0, verbose_name="Contrações"),
                ),
                (
                    "dinamica_uterina_tempo",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Tempo"
                    ),
                ),
                (
                    "tonus_uterino",
                    models.CharField(
                        default="", max_length=30, verbose_name="Tônus Uterino"
                    ),
                ),
                (
                    "hemorragias",
                    models.CharField(
                        choices=[("ausente", "ausente"), ("presente", "presente")],
                        default="",
                        max_length=30,
                        verbose_name="Hemorragias",
                    ),
                ),
                (
                    "situacao",
                    models.CharField(
                        choices=[
                            ("longitudinal", "longitudinal"),
                            ("transversa", "transversa"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Situação",
                    ),
                ),
                (
                    "apresentacao",
                    models.CharField(
                        choices=[
                            ("cefálica", "cefálica"),
                            ("pélvica", "pélvica"),
                            ("córmica", "córmica"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Apresentação",
                    ),
                ),
                (
                    "toque_vaginal",
                    models.CharField(
                        choices=[
                            ("nao realizado", "nao realizado"),
                            ("realizado", "realizado"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Toque Vaginal",
                    ),
                ),
                (
                    "toque_vaginal_dilatacao_admissao",
                    models.CharField(
                        default="", max_length=30, verbose_name="Dilatação na Admissão"
                    ),
                ),
                (
                    "toque_vaginal_hora_toque",
                    models.TimeField(
                        default=django.utils.timezone.now, verbose_name="Hora do Toque"
                    ),
                ),
                (
                    "bolsa",
                    models.CharField(
                        choices=[("integra", "integra"), ("rota", "rota")],
                        default="",
                        max_length=30,
                        verbose_name="Bolsa",
                    ),
                ),
                (
                    "bolsa_rota",
                    models.CharField(
                        default="", max_length=30, verbose_name="Bolsa Rota"
                    ),
                ),
                (
                    "liquido",
                    models.CharField(
                        choices=[("claro", "claro"), ("mecônio ", "mecônio ")],
                        default="",
                        max_length=30,
                        verbose_name="Líquido",
                    ),
                ),
                (
                    "liquido_meconio",
                    models.CharField(default="", max_length=30, verbose_name="Mais"),
                ),
                (
                    "exame_especular",
                    models.CharField(
                        choices=[
                            ("nao realizado", "nao realizado"),
                            ("realizado", "realizado"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Exame Especular",
                    ),
                ),
                (
                    "exame_especular_realizado",
                    models.CharField(
                        default="", max_length=30, verbose_name="Realizado"
                    ),
                ),
                (
                    "bcf",
                    models.CharField(default="", max_length=30, verbose_name="BCF"),
                ),
                (
                    "evolucao_dilatacao",
                    models.CharField(
                        default="", max_length=30, verbose_name="Evolução da Dilatação"
                    ),
                ),
                (
                    "dados_interesse",
                    models.CharField(
                        default="", max_length=30, verbose_name="Dados de Interesse"
                    ),
                ),
                (
                    "via_nascimento",
                    models.CharField(
                        choices=[("vaginal", "vaginal"), ("cesárea", "cesárea")],
                        default="",
                        max_length=30,
                        verbose_name="Via de Nascimento",
                    ),
                ),
                (
                    "data_parto",
                    models.DateField(
                        default="", max_length=30, verbose_name="Data do Parto"
                    ),
                ),
                (
                    "ig_ocasiao_parto",
                    models.CharField(
                        default="", max_length=30, verbose_name="IG na Ocasião do Parto"
                    ),
                ),
                (
                    "doenca_instalada_intercorrencias_parto",
                    models.CharField(
                        default="",
                        max_length=30,
                        verbose_name="Doença Instalada ou Intercorrências no Parto",
                    ),
                ),
                (
                    "episiotomia",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Episiotomia",
                    ),
                ),
                (
                    "laceracao",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Laceração",
                    ),
                ),
                (
                    "laceracao_rafia_laceracao",
                    models.CharField(
                        default="", max_length=30, verbose_name="Rafia de Laceração"
                    ),
                ),
                (
                    "uso_ocitocina_durante_trabalho_parto",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Uso de Ocitocina Durante o Trabalho de Parto",
                    ),
                ),
                (
                    "uso_misoprostol",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Uso de Misoprostol",
                    ),
                ),
                (
                    "uso_misoprostol_quantas_doses",
                    models.CharField(
                        default="", max_length=30, verbose_name="Quantas Doses"
                    ),
                ),
                (
                    "dados_recem_nascido",
                    models.CharField(
                        choices=[
                            ("Pré-Termo", "Pré-Termo"),
                            ("Termo", "Termo"),
                            ("Pós-Termo", "Pós-Termo"),
                        ],
                        default="",
                        max_length=30,
                        verbose_name="Dados do Recém-Nascido",
                    ),
                ),
                (
                    "hora_nascimento",
                    models.TimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Hora do Nascimento",
                    ),
                ),
                (
                    "apgar_1",
                    models.TimeField(
                        default=django.utils.timezone.now, verbose_name="Apgar 1"
                    ),
                ),
                (
                    "apgar_5",
                    models.TimeField(
                        default=django.utils.timezone.now, verbose_name="Apgar 5"
                    ),
                ),
                (
                    "apgar_10",
                    models.TimeField(
                        default=django.utils.timezone.now, verbose_name="Apgar 10"
                    ),
                ),
                (
                    "peso_nascer",
                    models.CharField(
                        default="", max_length=30, verbose_name="Peso ao Nascer"
                    ),
                ),
                (
                    "estatura",
                    models.CharField(
                        default="", max_length=30, verbose_name="Estatura"
                    ),
                ),
                ("pc", models.CharField(default="", max_length=30, verbose_name="PC")),
                ("pt", models.CharField(default="", max_length=30, verbose_name="PT")),
                ("pa", models.CharField(default="", max_length=30, verbose_name="PA")),
                (
                    "eliminacoes_fisiologicas_sala_parto",
                    models.CharField(
                        default="",
                        max_length=30,
                        verbose_name="Eliminações Fisiológicas na Sala de Parto",
                    ),
                ),
                (
                    "aspirado_nascer",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Aspirado ao Nascer",
                    ),
                ),
                (
                    "aspirado_nascer_indicacao",
                    models.CharField(
                        default="", max_length=30, verbose_name="Indicação"
                    ),
                ),
                (
                    "vpp",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="VPP",
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("masculino", "masculino"), ("feminino", "feminino")],
                        default="",
                        max_length=30,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "oxigenacao",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Oxigenação",
                    ),
                ),
                (
                    "medicacoes_administradas",
                    models.CharField(
                        default="",
                        max_length=30,
                        verbose_name="Medicações Administradas",
                    ),
                ),
                (
                    "realizado_contato_pele_pele",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Realizado Contato Pele a Pele",
                    ),
                ),
                (
                    "realizado_contato_pele_pele_motivo",
                    models.CharField(default="", max_length=30, verbose_name="Motivo"),
                ),
                (
                    "amamentacao_sala_parto",
                    models.CharField(
                        choices=[("sim", "Sim"), ("não", "Não")],
                        default="",
                        max_length=30,
                        verbose_name="Amamentação na Sala de Parto",
                    ),
                ),
                (
                    "amamentacao_sala_parto_motivo",
                    models.CharField(default="", max_length=30, verbose_name="Motivo"),
                ),
                (
                    "evolucao_enfermagem",
                    models.CharField(
                        default="", max_length=30, verbose_name="Evolução de Enfermagem"
                    ),
                ),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuario.paciente",
                    ),
                ),
            ],
        ),
    ]
