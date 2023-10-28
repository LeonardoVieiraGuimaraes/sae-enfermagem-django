from django.db import models
from django.utils.timezone import now
from multiselectfield import MultiSelectField

from usuario.models import Paciente


# Create your models here.
# SAE – Sistematização da Assistência de Enfermagem
# Puérpera Admitida em Alojamento Conjunto
class Questionario03(models.Model):
    choices_tipo_parto = (("PPN", "PPN"), ("POC", "POC"), ("Fórceps.", "Fórceps."))

    choices_s_n = (("Sim", "Sim"), ("Nao", "Não"))

    choices_venoclise_tipo = (("MSD", "MSD"), ("MSE", "MSE"))

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    tipo_parto = models.CharField(
        "Tipo de Parto", choices=choices_tipo_parto, max_length=10, default=""
    )

    data_parto = models.DateField("Data do Parto", default="")
    hora_parto = models.TimeField("Hora do Parto", default="")

    g = models.CharField(max_length=30, default="")
    p = models.CharField(max_length=30, default="")
    a = models.CharField(max_length=30, default="")
    ig = models.CharField(max_length=30, default="")
    hd = models.CharField(max_length=30, default="")
    admissao_acompanhente_livre_escolha = models.CharField(
        "Admissão com acompanhante de livre escolha",
        choices=choices_s_n,
        max_length=3,
        default="",
    )
    n_filhos_vivos = models.IntegerField("Nº de Filhos Vivo", default="")
    n_consultas_prenatal = models.IntegerField(
        "Nº de consultas no pré-natal", default=0
    )
    internacao_rn = models.CharField("Internação do RN", max_length=50, default="")
    venoclise = models.CharField(max_length=50, default="")
    venoclise_tipo = models.CharField(
        "Tipo", max_length=50, choices=choices_venoclise_tipo, default=""
    )
    sinais_flogistico = models.CharField(
        "Sinais Flogísticos", choices=choices_s_n, max_length=3, default=""
    )
    alergias = models.CharField(max_length=100, default="")
    patologias = models.CharField(max_length=100, default="")
    queixas = models.CharField(choices=choices_s_n, max_length=3, default="")
    queixas_qual = models.CharField(max_length=100, default="")
    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return self.paciente.usuario.nome


# NECESSIDADES PSICOBIOLÓGICAS
class Questionario0301(models.Model):
    choices_respiracao = (
        ("Eupneica", "Eupneica"),
        ("Taquipneica", "Taquipneica"),
        ("Dispneica", "Dispneica"),
        ("Bradipneica", "Bradipneica"),
    )

    choices_ap = (("MV", "MV"), ("RA", "RA"))

    choices_batimentos_cardiacos = (
        ("Normocárdica", "Normocárdica"),
        ("Bradicárdica", "Bradicárdica"),
        ("Taquicárdica", "Taquicárdica"),
    )

    choices_pressao_arterial = (
        ("Normotenso", "Normotenso"),
        ("Hipotenso", "Hipotenso"),
        ("Hipertenso", "Hipertenso"),
    )

    choices_aceita_dieta_oferecida = (
        ("Total", "Total"),
        ("Parcial", "Parcial"),
        ("Não aceita", "Não aceita"),
        ("Zero", "Zero"),
    )

    choices_abdome = (
        ("Normotenso e flácio", "Normotenso e flácio"),
        ("Globoso", "Globoso"),
        ("Distendido", "Distendido"),
        ("Doloroso", "Doloroso"),
    )

    choices_diurese = (("Espontânea", "Espontânea"), ("CVD", "CVD"), ("CVA", "CVA"))

    choices_evacuacoes = (("Presente", "Presente"), ("Ausente", "Ausente"))

    choices_sono_repouso = (
        ("Satisfatório", "Satisfatório"),
        ("Insatisfatório", "Insatisfatório"),
    )

    choices_membros_inferiores = (
        ("Sem alterações", "Sem alterações"),
        ("Edema", "Edema"),
        ("Varizes", "Varizes"),
        ("Deambulante", "Deambulante"),
    )

    choices_sinal_homans = (("Presente", "Presente"), ("Ausente", "Ausente"))

    choices_higiene = (("Preservada", "Preservada"), ("Alterada", "Alterada"))

    choices_pele_mucosa = (
        ("Corada", "Corada"),
        ("Hipocorada", "Hipocorada"),
        ("Ictérica", "Ictérica"),
        ("Outros", "Outros"),
    )

    choices_incisao_cirurgica = (
        ("curativo oclusivo", "curativo oclusivo"),
        ("limpa e seca", "limpa e seca"),
        ("Com sinais flogísticos", "Com sinais flogísticos"),
    )

    choices_perineo = (
        ("Integro", "Integro"),
        ("Lacerado", "Lacerado"),
        ("Edemaciado", "Edemaciado"),
        ("Edema", "Edema"),
        ("Hematoma", "Hematoma"),
    )

    choices_nivel_consciencia = (
        ("Lúcida", "Lúcida"),
        ("Orientada", "Orientada"),
        ("Desorientada/confusa", "Desorientada/confusa"),
        ("Sonolenta", "Sonolenta"),
        ("Outros:", "Outros:"),
    )

    choices_mamas = (
        ("Flácidas", "Flácidas"),
        ("Túrgidas", "Túrgidas"),
        ("Ingurgitadas", "Ingurgitadas"),
        ("Outros", "Outros"),
    )
    choices_mamilos = (
        ("Protusos", "Protusos"),
        ("Semi-protusos", "Semi-protusos"),
        ("Planos", "Planos"),
        ("Invertidos", "Invertidos"),
        ("Íntegros", "Íntegros"),
        ("Fissura", "Fissura"),
    )
    choices_colostro_expressao = (
        ("Presente", "Presente"),
        ("Ausente", "Ausente"),
        ("Diminuído", "Diminuído"),
    )
    choices_amamentacao = (
        ("Satisfatória", "Satisfatória"),
        ("Dificuldades", "Dificuldades"),
        ("Dor", "Dor"),
        ("Pega", "Pega"),
        ("Sucção", "Sucção"),
        ("Ordenha manual", "Ordenha manual"),
    )
    choices_utero = (
        ("Contraído", "Contraído"),
        ("Atonia", "Atonia"),
        ("Hipotônico", "Hipotônico"),
    )
    choices_involucao_uterina = (
        ("acima da CU", "acima da CU"),
        ("à altura da CU", "à altura da CU"),
        ("abaixo da CU", "abaixo da CU"),
    )
    choices_loquios = (
        ("fisiologicos", "fisiologicos"),
        ("Aumentados", "Aumentados"),
        ("fétido", "fétido"),
    )

    questionario03 = models.OneToOneField(
        Questionario03, on_delete=models.CASCADE, verbose_name="Nome do Paciente"
    )
    # OXIGENAÇÃO E CIRCULAÇÃO
    respiracao = models.CharField(
        choices=choices_respiracao, max_length=200, default=""
    )
    ap = models.CharField(choices=choices_ap, max_length=200, default="")
    batimentos_cardiacos = models.CharField(
        choices=choices_batimentos_cardiacos, max_length=200, default=""
    )
    pressao_arterial = models.CharField(
        choices=choices_pressao_arterial, max_length=200, default=""
    )

    # HIDRATAÇÃO E NUTRIÇÃO
    aceita_dieta_oferecida = models.CharField(
        choices=choices_aceita_dieta_oferecida, max_length=200, default=""
    )
    abdome = models.CharField(choices=choices_abdome, max_length=100, default="")

    # ELIMINAÇÃO
    diurese = models.CharField(choices=choices_diurese, max_length=100, default="")
    diurese_caracteristicas = models.CharField(
        "Características", max_length=100, default=""
    )
    evacuacoes = models.CharField(
        choices=choices_evacuacoes, max_length=100, default=""
    )
    evacuacoes_n_dias = models.IntegerField(default=0)

    # SONO E REPOUSO
    sono_repouso = models.CharField(
        choices=choices_sono_repouso, max_length=30, default=""
    )

    # MOTILIDADE E LOCOMOÇÃO:
    membros_inferiores = models.CharField(
        choices=choices_membros_inferiores, max_length=30, default=""
    )
    sinal_homans = models.CharField(
        choices=choices_sinal_homans, max_length=30, default=""
    )

    # CUIDADO CORPORAL
    higiene = models.CharField(choices=choices_higiene, max_length=30, default="")

    # INTEGRIDADE CUTÂNEO - MUCOSA
    pele_mucosa = models.CharField(
        choices=choices_pele_mucosa, max_length=30, default=""
    )
    pele_mucosa_outros = models.CharField("Outros", max_length=30, default="")
    inicisao_cirurgica = models.CharField(
        choices=choices_incisao_cirurgica, max_length=30, default=""
    )
    inicisao_cirurgica_quais = models.CharField("Outros", max_length=30, default="")
    perineo = models.CharField(max_length=50, default="")

    # REGULAÇÃO NEUROLÓGICA
    nivel_consciencia = models.CharField(
        choices=choices_nivel_consciencia, max_length=30, default=""
    )
    nivel_consciencia_outros = models.CharField("Outros", max_length=30, default="")

    # SEXUALIDADE E REPRODUÇÃO
    mamas = models.CharField(choices=choices_mamas, max_length=30, default="")
    mamilos = models.CharField(choices=choices_mamilos, max_length=30, default="")
    colostro_expresssao = models.CharField(
        choices=choices_colostro_expressao, max_length=30, default=""
    )
    amamentacao = models.CharField(
        choices=choices_amamentacao, max_length=30, default=""
    )
    amamentacao_motivos = models.CharField("Motivos", max_length=30, default="")
    perdas_vaginais_caracteristicas = models.CharField(max_length=30, default="")
    utero = models.CharField(choices=choices_utero, max_length=30, default="")
    involucao_uterina = models.CharField(
        choices=choices_involucao_uterina, max_length=30, default=""
    )
    involucao_uterina_acima_cu = models.CharField(
        "Acima da CU", max_length=30, default=""
    )
    loquios = models.CharField(choices=choices_loquios, max_length=30, default="")
    loquios_aumentados_quantidade = models.CharField(
        "Quantidade", max_length=30, default=""
    )

    # DADOS VITAIS E CONTROLES
    ssvvt = models.CharField("SSVVT", max_length=30, default="")
    fc = models.CharField("FC", max_length=30, default="")
    r = models.CharField("R", max_length=30, default="")
    pa = models.CharField("PA", max_length=30, default="")
    hgt = models.CharField("HGT", max_length=30, default="")
    peso = models.CharField("Peso", max_length=30, default="")
    atura = models.CharField("Altura", max_length=30, default="")
    spo2 = models.CharField("SpO2", max_length=30, default="")
    exames_alterados = models.CharField("Exames Alterados", max_length=30, default="")
    sifilis = models.CharField("Sífilis", max_length=30, default="")
    ts_mae = models.CharField("TS Mãe", max_length=30, default="")
    rn = models.CharField("RN", max_length=30, default="")

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return Questionario03.paciente.usuario.nome


# NECESSIDADES PSICOSSOCIAIS E PSICOESPIRITUAIS
class Questionario0302(models.Model):
    # SEGURANÇA EMOCIONAL
    choices_seguranca_emocional = (
        ("alterações de humor", "Alterações de Humor"),
        ("Crises de Choro", "Crises de Choro"),
        ("Emotividade Exacerbada", "Emotividade Exacerbada"),
        ("Insegurança", "Insegurança"),
        ("Irritabilidade", "Irritabilidade"),
        ("Tristeza", "Tristeza"),
        ("Alegria", "Alegria"),
        ("Medo", "Medo"),
        ("Ansiedade", "Ansiedade"),
    )

    choices_amor_aceitacao = (
        ("carência afetiva", "Carência Afetiva"),
        ("desinteresse pelo RN", "desinteresse pelo RN"),
        ("Acompanhante", "Acompanhante"),
    )

    choices_s_n = (("sim", "Sim"), ("não", "Não"))

    choices_aprendizagem_educacao_saude = (
        ("Dúvidas sobre o autocuidado", "Dúvidas sobre o autocuidado"),
        (
            "Dificuldade em compreender o regime terapêutico",
            "Dificuldade em compreender o regime terapêutico",
        ),
        ("Dúvidas sobre o período pós-parto", "Dúvidas sobre o período pós-parto"),
        ("Dúvidas sobre aleitamento materno", "Dúvidas sobre aleitamento materno"),
        (
            "Dificuldades na ordenha de leite materno",
            "Dificuldades na ordenha de leite materno",
        ),
        (
            "Dúvidas/dificuldades nos cuidados com o RN",
            "Dúvidas/dificuldades nos cuidados com o RN",
        ),
    )

    choices_comunicacao_gregaria = (
        ("boa interação familiar", "boa interação familiar"),
        ("conflito familiar", "conflito familiar"),
        ("isolamento", "isolamento"),
        ("recebe visitas", "recebe visitas"),
        ("gravidez desejada", "gravidez desejada"),
        ("gravidez indesejada", "gravidez indesejada"),
    )

    choices_autoestima_autoconfianca = (
        ("satisfeita", "satisfeita"),
        ("insatisfeita", "insatisfeita"),
    )

    questionario03 = models.OneToOneField(
        Questionario03,
        on_delete=models.CASCADE,
        verbose_name="Nome do Paciente",
        default="",
    )
    # SEGURANÇA EMOCIONAL
    seguranca_emocional = MultiSelectField(
        choices=choices_seguranca_emocional, max_length=200, default=""
    )

    # AMOR E ACEITAÇÃO
    amor_aceitacao = models.CharField(
        choices=choices_amor_aceitacao, max_length=30, default=""
    )
    amor_aceitacao_apoio_familiar = models.CharField(
        "Apoio Familiar", choices=choices_s_n, max_length=30, default=""
    )
    amor_aceitacao_acompanhante = models.CharField(
        "Acompanhante", choices=choices_s_n, max_length=30, default=""
    )
    amor_aceitacao_acompanhante_quem = models.CharField(
        "Quem", max_length=30, default=""
    )

    # APRENDIZAGEM E EDUCAÇÃO EM SAÚDE
    aprendizagem_educacao_saude = models.CharField(
        choices=choices_aprendizagem_educacao_saude, max_length=50, default=""
    )

    # COMUNICAÇÃO E GREGÁRIA
    comunicacao_gregaria = models.CharField(
        choices=choices_comunicacao_gregaria, max_length=30, default=""
    )

    # AUTOESTIMA E AUTOCONFIANÇA
    percepcao_sobre_imagem_corporal = models.CharField(
        choices=choices_autoestima_autoconfianca, max_length=30, default=""
    )
    autoconfianca_como_mae = models.CharField(
        choices=choices_autoestima_autoconfianca, max_length=30, default=""
    )

    # RELIGIOSIDADE E ESPIRITUALIDADE

    religiao = models.CharField("Religião", max_length=30, default="")
    necessita_auxilio_espiritual = models.CharField(
        "Necessita de auxílio espiritual",
        choices=choices_s_n,
        max_length=30,
        default="",
    )

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    #
    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return Questionario03.paciente.usuario.nome


# PLANEJAMENTO DA ASSISTÊNCIA DE ENFERMAGEM
class Questionario0303(models.Model):
    choices_diagnosticos_enfermagem_01 = (
        ("Volume de Líquidos Deficiente", "Volume de Líquidos Deficiente"),
    )

    choices_diagnosticos_enfermagem_02 = (
        (
            "Disposição para amamentação melhorada",
            "Disposição para amamentação melhorada",
        ),
    )

    choices_diagnosticos_enfermagem_03 = (
        ("Privação de sono", "Privação de sono"),
        ("Padrão do sono prejudicado", "Padrão do sono prejudicado"),
    )

    choices_diagnosticos_enfermagem_04 = (
        ("Conforto prejudicado", "Conforto prejudicado"),
    )

    choices_diagnosticos_enfermagem_05 = (
        ("Integridade da pele prejudicada", "Integridade da pele prejudicada"),
    )

    choices_diagnosticos_enfermagem_06 = (("Risco de infecção", "Risco de infecção"),)

    choices_diagnosticos_enfermagem_07 = (("Dor aguda", "Dor aguda"),)

    choices_diagnosticos_enfermagem_08 = (
        ("Ansiedade", "Ansiedade"),
        ("Medo", "Medo"),
    )

    choices_diagnosticos_enfermagem_09 = (
        (
            "Disposição para processo perinatológico melhorado",
            "Disposição para processo perinatológico melhorado",
        ),
        ("Processo perinatológico ineficaz", "Processo perinatológico ineficaz"),
    )

    choices_diagnosticos_enfermagem_10 = (
        (
            "Disposição para conhecimento melhorado",
            "Disposição para conhecimento melhorado",
        ),
        ("Conhecimento deficiente", "Conhecimento deficiente"),
    )

    choices_diagnosticos_enfermagem_11 = (("Outro", "Outro"),)

    choices_intervencoes_enfermagem_01 = (
        (
            "Monitorar o estado de hidratação, conforme apropriado",
            "Monitorar o estado de hidratação, conforme apropriado",
        ),
        (
            "Oferecer líquidos, conforme apropriado",
            "Oferecer líquidos, conforme apropriado",
        ),
        ("Monitorar os sinais vitais", "Monitorar os sinais vitais"),
        (
            "Administrar terapia IV, conforme prescrição",
            "Administrar terapia IV, conforme prescrição",
        ),
    )

    choices_intervencoes_enfermagem_02 = (
        (
            "Informar sobre as vantagens e as desvantagens do aleitamento materno",
            "Informar sobre as vantagens e as desvantagens do aleitamento materno",
        ),
        (
            "Corrigir conceitos errados, informações incorretas e imprecisões sobre a amamentação",
            "Corrigir conceitos errados, informações incorretas e imprecisões sobre a amamentação",
        ),
        (
            "Monitorar e estimular amamentação sob livre demanda",
            "Monitorar e estimular amamentação sob livre demanda",
        ),
        (
            "Avaliar o padrão de sucção/deglutição do recém-nascido",
            "Avaliar o padrão de sucção/deglutição do recém-nascido",
        ),
    )

    choices_intervencoes_enfermagem_03 = (
        (
            "Evitar interrupções desnecessárias e permitir períodos de descanso",
            "Evitar interrupções desnecessárias e permitir períodos de descanso",
        ),
        ("Criar um ambiente calmo e de apoio", "Criar um ambiente calmo e de apoio"),
        (
            "Proporcionar um ambiente seguro e limpo",
            "Proporcionar um ambiente seguro e limpo",
        ),
    )

    choices_intervencoes_enfermagem_04 = (
        (
            "Descrever as razões para o relaxamento, seus benefícios, limites e tipos disponíveis",
            "Descrever as razões para o relaxamento, seus benefícios, limites e tipos disponíveis",
        ),
        (
            "Criar um ambiente calmo e sem interrupções, com iluminação difusa e temperatura confortável, sempre que "
            "possível",
            "Criar um ambiente calmo e sem interrupções, com iluminação difusa e temperatura confortável, sempre que "
            "possível",
        ),
        ("Otimizar tempo de internação", "Otimizar tempo de internação"),
    )

    choices_intervencoes_enfermagem_05 = (
        (
            "Monitorar a integridade da pele dos mamilos",
            "Monitorar a integridade da pele dos mamilos",
        ),
        (
            "Orientar sobre o cuidado dos mamilos, inclusive como evitar fissuras",
            "Orientar sobre o cuidado dos mamilos, inclusive como evitar fissuras",
        ),
        (
            "Aplicação de compressa de gelo na região perineal",
            "Aplicação de compressa de gelo na região perineal",
        ),
    )

    choices_intervencoes_enfermagem_06 = (
        (
            "Examinar o local da incisão quanto a hiperemia, edema ou sinais de deiscência",
            "Examinar o local da incisão quanto a hiperemia, edema ou sinais de deiscência",
        ),
        (
            "Realizar curativo mantendo rigor asséptico",
            "Realizar curativo mantendo rigor asséptico",
        ),
        (
            "Aplicar curativo apropriado para proteger a incisão",
            "Aplicar curativo apropriado para proteger a incisão",
        ),
    )

    choices_intervencoes_enfermagem_07 = (
        (
            "Realizar uma avaliação completa da dor, incluindo local, características, início/duração, frequência,"
            "qualidade, intensidade e gravidade, além de fatores precipitadores",
            "Realizar uma avaliação completa da dor, incluindo local, características, início/duração, frequência,"
            "qualidade, intensidade e gravidade, além de fatores precipitadores",
        ),
        (
            "Oferecer alívio da dor mediante a analgesia prescrita",
            "Oferecer alívio da dor mediante a analgesia prescrita",
        ),
        (
            "Ensinar o uso de técnicas não farmacológicas",
            "Ensinar o uso de técnicas não farmacológicas",
        ),
    )

    choices_intervencoes_enfermagem_08 = (
        (
            "Usar abordagem calma e tranquilizadora",
            "Usar abordagem calma e tranquilizadora",
        ),
        (
            "Observar sinais verbais e não verbais de ansiedade",
            "Observar sinais verbais e não verbais de ansiedade",
        ),
        (
            "Encorajar a expressão de sentimentos, percepções e medos",
            "Encorajar a expressão de sentimentos, percepções e medos",
        ),
        ("Escutar o paciente com atenção", "Escutar o paciente com atenção"),
        ("Explicar todos os procedimentos", "Explicar todos os procedimentos"),
        (
            "Oferecer informações reais sobre diagnóstico, tratamento e prognóstico",
            "Oferecer informações reais sobre diagnóstico, tratamento e prognóstico",
        ),
    )

    choices_intervencoes_enfermagem_09 = (
        (
            "Discutir os sentimentos que a mãe possa ter em relação ao bebê",
            "Discutir os sentimentos que a mãe possa ter em relação ao bebê",
        ),
        (
            "Demonstrar confiança na capacidade da mãe para cuidar do recém-nascido",
            "Demonstrar confiança na capacidade da mãe para cuidar do recém-nascido",
        ),
        (
            "Monitorar o surgimento de sintomas de depressão pós-parto",
            "Monitorar o surgimento de sintomas de depressão pós-parto",
        ),
    )

    choices_intervencoes_enfermagem_10 = (
        (
            "Determinar as necessidades de aprendizagem do paciente",
            "Determinar as necessidades de aprendizagem do paciente",
        ),
        (
            "Orientar os pais/cuidador a alimentar somente com leite materno",
            "Orientar os pais/cuidador a alimentar somente com leite materno",
        ),
        (
            "Orientar os pais/cuidador a colocar o bebê de costas para dormir",
            "Orientar os pais/cuidador a colocar o bebê de costas para dormir",
        ),
        (
            "Orientar os pais/cuidador a testar a temperatura da água do banho",
            "Orientar os pais/cuidador a testar a temperatura da água do banho",
        ),
    )

    choices_avaliacao = (
        ("Melhorado", "Melhorado"),
        ("Piorado", "Piorado"),
        ("Inalterado", "Inalterado"),
        ("Resolvido", "Resolvido"),
    )

    questionario03 = models.OneToOneField(
        Questionario03,
        on_delete=models.CASCADE,
        verbose_name="Nome do Paciente",
        default="",
    )

    diagnosticos_enfermagem_01 = MultiSelectField(
        "Diagnósticos de Enfermagem",
        choices=choices_diagnosticos_enfermagem_01,
        max_length=200,
        default="",
    )

    diagnosticos_enfermagem_02 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_02, max_length=200, default=""
    )

    diagnosticos_enfermagem_03 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_03, max_length=200, default=""
    )

    diagnosticos_enfermagem_04 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_04, max_length=200, default=""
    )

    diagnosticos_enfermagem_05 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_05, max_length=200, default=""
    )

    diagnosticos_enfermagem_06 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_06, max_length=200, default=""
    )

    diagnosticos_enfermagem_07 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_07, max_length=200, default=""
    )

    diagnosticos_enfermagem_08 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_08, max_length=200, default=""
    )

    diagnosticos_enfermagem_09 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_09, max_length=200, default=""
    )

    diagnosticos_enfermagem_10 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_10, max_length=200, default=""
    )

    diagnosticos_enfermagem_11 = MultiSelectField(
        "", choices=choices_diagnosticos_enfermagem_11, max_length=200, default=""
    )

    intervencoes_enfermagem_01 = MultiSelectField(
        "Intervenções de Enfermagem",
        choices=choices_intervencoes_enfermagem_01,
        max_length=200,
        default="",
    )

    intervencoes_enfermagem_02 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_02, max_length=200, default=""
    )

    intervencoes_enfermagem_03 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_03, max_length=200, default=""
    )

    intervencoes_enfermagem_04 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_04, max_length=200, default=""
    )

    intervencoes_enfermagem_05 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_05, max_length=200, default=""
    )

    intervencoes_enfermagem_06 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_06, max_length=200, default=""
    )

    intervencoes_enfermagem_07 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_07, max_length=200, default=""
    )

    intervencoes_enfermagem_08 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_08, max_length=200, default=""
    )

    intervencoes_enfermagem_09 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_09, max_length=200, default=""
    )

    intervencoes_enfermagem_10 = MultiSelectField(
        "", choices=choices_intervencoes_enfermagem_10, max_length=200, default=""
    )

    intervencoes_enfermagem_11 = models.TextField("", max_length=2000, default="")

    avaliacao_01 = models.CharField(
        "Avaliação", choices=choices_avaliacao, max_length=150, default=""
    )

    avaliacao_02 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_03 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_04 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_05 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_06 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_07 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_08 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_09 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_10 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_11 = models.CharField(
        "", choices=choices_avaliacao, max_length=30, default=""
    )

    avaliacao_conduta_enfermagem = models.TextField(
        "Avaliação e/ou Conduta de Enfermagem", max_length=2000, default=""
    )

    avaliacao_conduta_enfermagem_hora = models.TimeField("Hora:", default=now)

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    #
    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return Questionario03.paciente.usuario.nome


# class Questionario030301(Questionario0303):
#     choices_avaliacao = (
#         ("Melhorado", "Melhorado"), ("Piorado", "Piorado"), ("Inalterado", "Inalterado"), ("Resolvido", "Resolvido"))
#
#     avaliacao = models.CharField("Avaliação", choices=choices_avaliacao, max_length=30, default="")


# PLANEJAMENTO DA ASSISTÊNCIA DE ENFERMAGEM
class Questionario0304(models.Model):
    choices_orientacoes_enfermagem = (
        (
            "Rotinas de permanência da mãe, pai ou representante legal nas 24horas por dia",
            "Rotinas de permanência da mãe, pai ou representante legal nas 24horas por dia",
        ),
        (
            "Cuidados com Puérpera (deambulação precoce, alimentação, curativo, 1º banho, higiene íntima, compressa "
            "fria)",
            "Cuidados com Puérpera (deambulação precoce, alimentação, curativo, 1º banho, higiene íntima, compressa "
            "fria)",
        ),
        (
            "Cuidados com RN (curativo do coto umbilical, 1º banho e troca de fraldas)",
            "Cuidados com RN (curativo do coto umbilical, 1º banho e troca de fraldas)",
        ),
        (
            "Amamentação (sinais que o bebê quer mamar, frequência, pega correta, posição correta, dificuldades, "
            "retirada do excesso de leite, importância do leite materno nos primeiros dias -icterícia, 1ª vacina, "
            "previne doenças, intestino)",
            "Amamentação (sinais que o bebê quer mamar, frequência, pega correta, posição correta, dificuldades, "
            "retirada do excesso de leite, importância do leite materno nos primeiros dias -icterícia, 1ª vacina, "
            "previne doenças, intestino)",
        ),
        (
            "Perigo do aleitamento materno cruzado",
            "Perigo do aleitamento materno cruzado",
        ),
        (
            "Perigo do aleitamento materno cruzado",
            "Perigo do aleitamento materno cruzado",
        ),
        (
            "Prejuízos no uso de bicos , chupetas ( dentição, anti-higiênico, desenvolvimento das fala, Aleitamento "
            "ao seio, diarreias)",
            "Prejuízos no uso de bicos , chupetas ( dentição, anti-higiênico, desenvolvimento das fala, Aleitamento "
            "ao seio,diarreias)",
        ),
        (
            "Orientação sobre que NÃO existe leite fraco e que o bebê em aleitamento materno NÃO precisa de água, "
            "chá ou outro alimento nos 6 primeiros meses",
            "Orientação sobre que NÃO existe leite fraco e que o bebê em aleitamento materno NÃO precisa de água, "
            "chá ou outro alimento nos 6 primeiros meses",
        ),
        (
            "Como não deixar o leite secar (Massagem, ordenha e líquidos)",
            "Como não deixar o leite secar (Massagem, ordenha e líquidos)",
        ),
        ("Riscos de quedas Puérpera e RN", "Riscos de quedas Puérpera e RN"),
        (
            "Onde procurar ajuda se tiver dúvidas com a amamentação depois que voltar para casa",
            "Onde procurar ajuda se tiver dúvidas com a amamentação depois que voltar para casa",
        ),
    )

    choices_check_list_enfermagem_alta_hospitalar = (
        (
            "Puérpera recebeu e compreendeu as informações sobre cuidados com RN, autocuidado, aleitameto materno e "
            "retorno a sua unidade de saúde na primeira semana de vida da criança para consulta puerperal",
            "Puérpera recebeu e compreendeu as informações sobre cuidados com RN, autocuidado, aleitameto materno e"
            "retorno a sua unidade de saúde na primeira semana de vida da criança para consulta puerperal",
        ),
        (
            "RN em AME com sucção ao seio, pega e posicionamento adequados, pois NÃO há restrições ao aleitamento "
            "materno",
            "RN em AME com sucção ao seio, pega e posicionamento adequados, pois NÃO há restrições ao aleitamento "
            "materno",
        ),
        (
            "RN em uso de substituto do leite humano/formula láctea pois a amamentação é contra-indicada de acordo "
            "com atualização OMS",
            "RN em uso de substituto do leite humano/formula láctea pois a amamentação é contra-indicada de acordo "
            "com atualização OMS",
        ),
        (
            "A mãe, o pai e outros cuidadores foram orientados a reconhecer situações de risco e a procurar a USF se "
            "o recémnascido apresentar problemas com aleitamento materno, icterícia ou qualquer outra alteração",
            "A mãe, o pai e outros cuidadores foram orientados a reconhecer situações de risco e a procurar a USF se "
            "o recémnascido apresentar problemas com aleitamento materno, icterícia ou qualquer outra alteração",
        ),
        (
            "A mulher foi orientada a procurar a USF ou o hospital caso apresente febre, secreção purulenta vaginal, "
            "por ferida operatória, sangramento com odor fétido ou com volume aumentado, edema assimétrico de "
            "extremidades, sofrimento emocional ou outros desconfortos, intercorrências com as mamas",
            "A mulher foi orientada a procurar a USF ou o hospital caso apresente febre, secreção purulenta vaginal, "
            "por ferida operatória, sangramento com odor fétido ou com volume aumentado, edema assimétrico de "
            "extremidades, sofrimento emocional ou outros desconfortos, intercorrências com as mamas",
        ),
        (
            "Orientada a higienizar as mãos antes e após o cuidado com o recém-nascido",
            "Orientada a higienizar as mãos antes e após o cuidado com o recém-nascido",
        ),
        (
            "Orientada a deixar a criança em decúbito dorsal, manter a amamentação ao seio até os 6 meses "
            "exclusivamente e 2 anos ou mais complementar",
            "Orientada a deixar a criança em decúbito dorsal, manter a amamentação ao seio até os 6 meses "
            "exclusivamente e 2 anos ou mais complementar",
        ),
        (
            "Alta hospitalar evoluida no prontuário, dados do RN anotado na carteira da criança",
            "Alta hospitalar evoluida no prontuário, dados do RN anotado na carteira da criança",
        ),
        (
            "Solicitado avaliação do serviço social se necessário",
            "Solicitado avaliação do serviço social se necessário",
        ),
    )

    questionario03 = models.OneToOneField(
        Questionario03,
        on_delete=models.CASCADE,
        verbose_name="Nome do Paciente",
        default="",
    )

    nome = models.CharField("Nome", max_length=100, default="")

    orientacoes_enfermagem = MultiSelectField(
        "Orientações de Enfermagem – POI/ 1PO e 2PO",
        choices=choices_orientacoes_enfermagem,
        max_length=1000,
        default="",
    )

    check_list_enfermagem_alta_hospitalar = MultiSelectField(
        "Check List de Enfermagem para Alta Hospitalar",
        choices=choices_check_list_enfermagem_alta_hospitalar,
        max_length=5000,
        default="",
    )

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)
    def __str__(self):
        return Questionario03.paciente.usuario.nome


class Questionario04(models.Model):
    choices_s_n = (("sim", "Sim"), ("não", "Não"))

    choices_admissao_obstetrica = (
        ("Risco Habitual", "Risco Habitual"),
        ("Alto Risco", "Alto Risco"),
    )

    choices_antecedentes_pessoais_patologicos = (
        ("HAS", "HAS"),
        ("Diabetes", "Diabetes"),
        ("Síndrome hipertensiva", "Síndrome hipertensiva"),
        ("Hemorragia", "Hemorragia "),
        ("Etilismo", "Etilismo"),
        ("Tabagismo", "Tabagismo"),
    )

    choices_estratificacao_risco_hpp = (
        ("Baixo", "Baixo"),
        ("Médio", "Médio"),
        ("Alto", "Alto"),
    )

    choices_dinamica_uterina = (("ausente", "ausente"), ("presente", "presente"))

    choices_tonus_uterino = (("fisiológico", "fisiológico"), ("aumentado", "aumentado"))

    choices_hemorragias = (("ausente", "ausente"), ("presente", "presente"))

    choices_situacao = (("longitudinal", "longitudinal"), ("transversa", "transversa"))

    choices_apresentacao = (
        ("cefálica", "cefálica"),
        ("pélvica", "pélvica"),
        ("córmica", "córmica"),
    )

    choices_toque_vaginal = (
        ("nao realizado", "nao realizado"),
        ("realizado", "realizado"),
    )

    choices_bolsa = (("integra", "integra"), ("rota", "rota"))

    choices_liquido = (("claro", "claro"), ("mecônio ", "mecônio "))

    choices_exame_especular = (
        ("nao realizado", "nao realizado"),
        ("realizado", "realizado"),
    )

    choices_via_nascimento = (("vaginal", "vaginal"), ("cesárea", "cesárea"))

    choices_dados_recem_nascido = (
        ("Pré-Termo", "Pré-Termo"),
        ("Termo", "Termo"),
        ("Pós-Termo", "Pós-Termo"),
    )

    choices_sexo = (("masculino", "masculino"), ("feminino", "feminino"))

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    # Admissao Obstétrica
    admissao_obstetrica = models.CharField(
        "Admissão Obstétrica",
        choices=choices_admissao_obstetrica,
        max_length=30,
        default="",
    )
    data_adminissao = models.DateField("Data de Admissão", max_length=30, default="")
    hora_admissao = models.TimeField("Hora de Admissão", max_length=30, default="")
    admissao_obstetrica_motivo = models.CharField("Motivo", max_length=30, default="")

    # Anamnese

    alergias = models.CharField(
        "Alergias", max_length=30, default="", choices=choices_s_n
    )
    alergias_descricao = models.CharField("Descrição:", max_length=30, default="")
    antecedentes_pessoais_patologicos = MultiSelectField(
        "Antecedentes Pessoais e Patológicos",
        max_length=30,
        default="",
        choices=choices_antecedentes_pessoais_patologicos,
    )

    # Antecedentes obstétricos:
    gesta = models.CharField("Gesta", max_length=30, default="")
    para = models.CharField("Para", max_length=30, default="")
    ab = models.CharField("AB", max_length=30, default="")
    pn = models.CharField("PN", max_length=30, default="")
    pc = models.CharField("PC", max_length=30, default="")
    filhos_vivos = models.CharField("Filhos Vivos", max_length=30, default="")

    # Idade Gestacional
    dum = models.CharField("DUM", max_length=30, default="")
    usg = models.CharField("USG", max_length=30, default="")
    trimestre = models.CharField("Trimestre", max_length=30, default="")
    dpp = models.DateField("DPP", max_length=30, default="")

    realizou_pre_natal = models.CharField(
        "Realizou Pré-Natal", choices=choices_s_n, max_length=30, default=""
    )
    realizou_visita_vinculacao_maternidade = models.CharField(
        "Realizou Visita de Vinculação à Maternidade",
        choices=choices_s_n,
        max_length=30,
        default="",
    )
    realizou_visita_vinculacao_maternidade_motivo = models.CharField(
        "Motivo", max_length=30, default=""
    )
    estratificacao_risco_hpp = models.CharField(
        "Estratificação de Risco para HPP",
        max_length=30,
        default="",
        choices=choices_estratificacao_risco_hpp,
    )

    medicamentos_uso = models.CharField(
        "Medicamentos em Uso", max_length=30, default=""
    )
    exames_complementares = models.CharField(
        "Exames Complementares", max_length=30, default=""
    )

    # Exame Geral
    pas = models.CharField("PAS", max_length=30, default="")

    fc = models.CharField("FC", max_length=30, default="")

    temp = models.CharField("Temp", max_length=30, default="")

    fr = models.CharField("FR", max_length=30, default="")

    edemas_mmii = models.CharField("Edemas MMII", max_length=30, default="")

    # AVALIAÇÃO OBSTÉTRICA
    dinamica_uterina = models.CharField(
        "Dinâmica Uterina", max_length=30, default="", choices=choices_dinamica_uterina
    )

    dinamica_uterina_contracoes = models.IntegerField("Contrações", default=0)

    dinamica_uterina_tempo = models.TimeField("Tempo", default="")

    tonus_uterino = models.CharField("Tônus Uterino", max_length=30, default="")

    hemorragias = models.CharField(
        "Hemorragias", max_length=30, default="", choices=choices_hemorragias
    )
    situacao = models.CharField(
        "Situação", max_length=30, default="", choices=choices_situacao
    )
    apresentacao = models.CharField(
        "Apresentação", max_length=30, default="", choices=choices_apresentacao
    )
    toque_vaginal = models.CharField(
        "Toque Vaginal", max_length=30, default="", choices=choices_toque_vaginal
    )

    toque_vaginal_dilatacao_admissao = models.CharField(
        "Dilatação na Admissão", max_length=30, default=""
    )

    toque_vaginal_hora_toque = models.TimeField("Hora do Toque", default=now)

    bolsa = models.CharField("Bolsa", max_length=30, default="", choices=choices_bolsa)

    bolsa_rota = models.CharField("Bolsa Rota", max_length=30, default="")

    liquido = models.CharField(
        "Líquido", max_length=30, default="", choices=choices_liquido
    )
    liquido_meconio = models.CharField("Mais", max_length=30, default="")

    exame_especular = models.CharField(
        "Exame Especular", max_length=30, default="", choices=choices_exame_especular
    )
    exame_especular_realizado = models.CharField("Realizado", max_length=30, default="")
    bcf = models.CharField("BCF", max_length=30, default="")
    evolucao_dilatacao = models.CharField(
        "Evolução da Dilatação", max_length=30, default=""
    )
    dados_interesse = models.CharField("Dados de Interesse", max_length=30, default="")

    # DADOS DO PARTO

    via_nascimento = models.CharField(
        "Via de Nascimento", max_length=30, default="", choices=choices_via_nascimento
    )
    data_parto = models.DateField("Data do Parto", max_length=30, default="")
    ig_ocasiao_parto = models.CharField(
        "IG na Ocasião do Parto", max_length=30, default=""
    )
    doenca_instalada_intercorrencias_parto = models.CharField(
        "Doença Instalada ou Intercorrências no Parto", max_length=30, default=""
    )
    episiotomia = models.CharField(
        "Episiotomia", max_length=30, default="", choices=choices_s_n
    )
    laceracao = models.CharField(
        "Laceração", max_length=30, default="", choices=choices_s_n
    )
    laceracao_rafia_laceracao = models.CharField(
        "Rafia de Laceração", max_length=30, default=""
    )
    uso_ocitocina_durante_trabalho_parto = models.CharField(
        "Uso de Ocitocina Durante o Trabalho de Parto",
        max_length=30,
        default="",
        choices=choices_s_n,
    )
    uso_misoprostol = models.CharField(
        "Uso de Misoprostol", max_length=30, default="", choices=choices_s_n
    )
    uso_misoprostol_quantas_doses = models.CharField(
        "Quantas Doses", max_length=30, default=""
    )

    # DADOS DO RECÉM - NASCIDO
    dados_recem_nascido = models.CharField(
        "Dados do Recém-Nascido",
        max_length=30,
        default="",
        choices=choices_dados_recem_nascido,
    )
    hora_nascimento = models.TimeField("Hora do Nascimento", default=now)

    apgar_1 = models.TimeField("Apgar 1", default=now)

    apgar_5 = models.TimeField("Apgar 5", default=now)

    apgar_10 = models.TimeField("Apgar 10", default=now)

    peso_nascer = models.CharField("Peso ao Nascer", max_length=30, default="")

    estatura = models.CharField("Estatura", max_length=30, default="")

    pc = models.CharField("PC", max_length=30, default="")

    pt = models.CharField("PT", max_length=30, default="")

    pa = models.CharField("PA", max_length=30, default="")

    eliminacoes_fisiologicas_sala_parto = models.CharField(
        "Eliminações Fisiológicas na Sala de Parto", max_length=30, default=""
    )
    aspirado_nascer = models.CharField(
        "Aspirado ao Nascer", max_length=30, default="", choices=choices_s_n
    )
    aspirado_nascer_indicacao = models.CharField("Indicação", max_length=30, default="")

    vpp = models.CharField("VPP", max_length=30, default="", choices=choices_s_n)

    sexo = models.CharField("Sexo", max_length=30, default="", choices=choices_sexo)

    oxigenacao = models.CharField(
        "Oxigenação", max_length=30, default="", choices=choices_s_n
    )
    medicacoes_administradas = models.CharField(
        "Medicações Administradas", max_length=30, default=""
    )
    realizado_contato_pele_pele = models.CharField(
        "Realizado Contato Pele a Pele", max_length=30, default="", choices=choices_s_n
    )
    realizado_contato_pele_pele_motivo = models.CharField(
        "Motivo", max_length=30, default=""
    )
    amamentacao_sala_parto = models.CharField(
        "Amamentação na Sala de Parto", max_length=30, default="", choices=choices_s_n
    )
    amamentacao_sala_parto_motivo = models.CharField(
        "Motivo", max_length=30, default=""
    )

    evolucao_enfermagem = models.CharField(
        "Evolução de Enfermagem", max_length=30, default=""
    )

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return self.paciente.usuario.nome


# Ficha de Atendimento Acolhimento & Classificação de Risco em Obstetrícia
class Questionario05(models.Model):
    choices_classificacao = (
        ("Emergência", "Emergência"),
        ("Urgência", "Urgência"),
        ("Pouco Urgente", "Pouco Urgente"),
        ("Não Urgente", "Não Urgente"),
    )

    choices_s_n = (("Sim", "Sim"), ("Não", "Não"))

    choices_perda_liquido = (("Sim, relatada pelo paciente", "Sim, relatada pelo paciente"), ("Sim, visualizada pelo profissional", "Sim, visualizada pelo profissional"), ("Não", "Não"))

    choices_aspecto_liquido = (
        ("Claro", "Claro"),
        ("Meconial fluido", "Meconial fluido"),
        ("Meconial espesso", "Meconial espesso"),
    )

    choices_sangramento_vaginal = (("Ausente", "Ausente"), ("Presente", "Presente"))

    choices_observacoes = (("Alergias", "Alergias"), ("Drogas", "Drogas"), ("Outras", "Outras"))

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    data = models.DateField("Data", default=now)

    horario_chegada = models.TimeField("Horário", default=now)

    horario_classficacao = models.TimeField("Horário", default=now)

    dum = models.DateField("DUM", default=now)

    g = models.CharField("G", max_length=30, default="")
    p = models.CharField("P", max_length=30, default="")
    a = models.CharField("A", max_length=30, default="")

    queixas = models.CharField("Queixas", max_length=30, default="")

    pa = models.CharField("PA", max_length=30, default="")

    fc = models.CharField("FC", max_length=30, default="")

    fr = models.CharField("FR", max_length=30, default="")

    temp = models.CharField("Temp", max_length=30, default="")

    sato2 = models.CharField("SatO2", max_length=30, default="")

    dor = models.CharField("Dor", max_length=30, default="")

    localizacao = models.CharField("Localização", max_length=30, default="")

    contracoes_uterinas = MultiSelectField("Contrações Uterinas", default="", max_length=30, choices=choices_s_n)

    hipertonia_uterina = models.CharField(choices=choices_s_n, max_length=30, default="")

    perda_liquido = models.CharField(choices=choices_s_n, max_length=30, default="")

    aspecto_liquido = models.CharField(choices=choices_aspecto_liquido, max_length=30, default="")

    sangramento_vaginal = models.CharField(choices=choices_sangramento_vaginal, max_length=30, default="")

    bcf = models.CharField("BCF", max_length=30, default="")

    mf = models.CharField("MF", max_length=30, default="")

    outras_queixas_relatos = models.CharField("Outras Queixas e/ou relatos", max_length=30, default="")

    medicamentos_uso_gravidez = models.CharField("Medicamentos em uso na gravidez", max_length=30, default="")

    observacoes = models.CharField("Observações", max_length=30, default="", choices=choices_observacoes)

    profissional_enfermagem_coren = models.CharField("Profissional de Enfermagem (COREN)", max_length=30, default="")

    hora_atendimento_profissional_enfermagem_coren = models.TimeField("Horário", default=now)

    nome_medico_avaliador = models.CharField("Nome do Médico Avaliador", max_length=30, default="")

    hora_atendimento_nome_medico_avaliador = models.TimeField("Horário", default=now)

    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)

    # data_cadastro = models.DateField(default=now)
    # data_atualizacao = models.DateField(default=now)

    def __str__(self):
        return self.paciente.usuario.nome
