# Generated by Django 4.2.3 on 2023-07-21 14:09

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0026_questionario0303_avaliacao_conduta_enfermagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario0304',
            name='volume_liquidos_deficiente_avaliacao',
        ),
        migrations.RemoveField(
            model_name='questionario0304',
            name='volume_liquidos_deficiente_intervencoes_enfermagem',
        ),
        migrations.AddField(
            model_name='questionario0303',
            name='questionario03',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='questionario.questionario03', verbose_name='Nome do Paciente'),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='check_list_enfermagem_alta_hospitalar',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Puérpera recebeu e compreendeu as informações sobre cuidados com RN, autocuidado, aleitameto materno e retorno a sua unidade de saúde na primeira semana de vida da criança para consulta puerperal', 'Puérpera recebeu e compreendeu as informações sobre cuidados com RN, autocuidado, aleitameto materno e retorno a sua unidade de saúde na primeira semana de vida da criança para consulta puerperal'), ('RN em AME com sucção ao seio, pega e posicionamento adequados, pois NÃO há restrições ao aleitamento materno', 'RN em AME com sucção ao seio, pega e posicionamento adequados, pois NÃO há restrições ao aleitamento materno'), ('RN em uso de substituto do leite humano/formula láctea pois a amamentação é contra-indicada de acordo com atualização OMS', 'RN em uso de substituto do leite humano/formula láctea pois a amamentação é contra-indicada de acordo com atualização OMS'), ('A mãe, o pai e outros cuidadores foram orientados a reconhecer situações de risco e a procurar a USF se o recémnascido apresentar problemas com aleitamento materno, icterícia ou qualquer outra alteração', 'A mãe, o pai e outros cuidadores foram orientados a reconhecer situações de risco e a procurar a USF se o recémnascido apresentar problemas com aleitamento materno, icterícia ou qualquer outra alteração'), ('A mulher foi orientada a procurar a USF ou o hospital caso apresente febre, secreção purulenta vaginal, por ferida operatória, sangramento com odor fétido ou com volume aumentado, edema assimétrico de extremidades, sofrimento emocional ou outros desconfortos, intercorrências com as mamas', 'A mulher foi orientada a procurar a USF ou o hospital caso apresente febre, secreção purulenta vaginal, por ferida operatória, sangramento com odor fétido ou com volume aumentado, edema assimétrico de extremidades, sofrimento emocional ou outros desconfortos, intercorrências com as mamas'), ('Orientada a higienizar as mãos antes e após o cuidado com o recém-nascido', 'Orientada a higienizar as mãos antes e após o cuidado com o recém-nascido'), ('Orientada a deixar a criança em decúbito dorsal, manter a amamentação ao seio até os 6 meses exclusivamente e 2 anos ou mais complementar', 'Orientada a deixar a criança em decúbito dorsal, manter a amamentação ao seio até os 6 meses exclusivamente e 2 anos ou mais complementar'), ('Alta hospitalar evoluida no prontuário, dados do RN anotado na carteira da criança', 'Alta hospitalar evoluida no prontuário, dados do RN anotado na carteira da criança'), ('Solicitado avaliação do serviço social se necessário', 'Solicitado avaliação do serviço social se necessário')], default='', max_length=5000, verbose_name='Check List de Enfermagem para Alta Hospitalar'),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='nome',
            field=models.CharField(default='', max_length=100, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='orientacoes_enfermagem',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Rotinas de permanência da mãe, pai ou representante legal nas 24horas por dia', 'Rotinas de permanência da mãe, pai ou representante legal nas 24horas por dia'), ('Cuidados com Puérpera (deambulação precoce, alimentação, curativo, 1º banho, higiene íntima, compressa fria)', 'Cuidados com Puérpera (deambulação precoce, alimentação, curativo, 1º banho, higiene íntima, compressa fria)'), ('Cuidados com RN (curativo do coto umbilical, 1º banho e troca de fraldas)', 'Cuidados com RN (curativo do coto umbilical, 1º banho e troca de fraldas)'), ('Amamentação (sinais que o bebê quer mamar, frequência, pega correta, posição correta, dificuldades, retirada do excesso de leite, importância do leite materno nos primeiros dias -icterícia, 1ª vacina, previne doenças, intestino)', 'Amamentação (sinais que o bebê quer mamar, frequência, pega correta, posição correta, dificuldades, retirada do excesso de leite, importância do leite materno nos primeiros dias -icterícia, 1ª vacina, previne doenças, intestino)'), ('Perigo do aleitamento materno cruzado', 'Perigo do aleitamento materno cruzado'), ('Perigo do aleitamento materno cruzado', 'Perigo do aleitamento materno cruzado'), ('Prejuízos no uso de bicos , chupetas ( dentição, anti-higiênico, desenvolvimento das fala, Aleitamento ao seio, diarreias)', 'Prejuízos no uso de bicos , chupetas ( dentição, anti-higiênico, desenvolvimento das fala, Aleitamento ao seio,diarreias)'), ('Orientação sobre que NÃO existe leite fraco e que o bebê em aleitamento materno NÃO precisa de água, chá ou outro alimento nos 6 primeiros meses', 'Orientação sobre que NÃO existe leite fraco e que o bebê em aleitamento materno NÃO precisa de água, chá ou outro alimento nos 6 primeiros meses'), ('Como não deixar o leite secar (Massagem, ordenha e líquidos)', 'Como não deixar o leite secar (Massagem, ordenha e líquidos)'), ('Riscos de quedas Puérpera e RN', 'Riscos de quedas Puérpera e RN'), ('Onde procurar ajuda se tiver dúvidas com a amamentação depois que voltar para casa', 'Onde procurar ajuda se tiver dúvidas com a amamentação depois que voltar para casa')], default='', max_length=1000, verbose_name='Orientações de Enfermagem – POI/ 1PO e 2PO'),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='questionario03',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='questionario.questionario03', verbose_name='Nome do Paciente'),
        ),
    ]
