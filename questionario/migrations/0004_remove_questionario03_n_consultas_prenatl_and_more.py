# Generated by Django 4.2.2 on 2023-06-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0003_alter_questionario03_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario03',
            name='n_consultas_prenatl',
        ),
        migrations.AddField(
            model_name='questionario03',
            name='n_consultas_prenatal',
            field=models.IntegerField(default=0, verbose_name='Nº de consultas no pré-natal'),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='admissao_acompanhente_livre_escolha',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Nao', 'Não')], default='', max_length=3, verbose_name='Admissão com acompanhante de livre escolha'),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='data_parto',
            field=models.DateField(default='', verbose_name='Data do Parto'),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='hora_parto',
            field=models.TimeField(default='', verbose_name='Hora do Parto'),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='n_filhos_vivos',
            field=models.IntegerField(default='', verbose_name='Nº de Filhos Vivo'),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='tipo_parto',
            field=models.CharField(choices=[('PPN', 'PPN'), ('POC', 'POC'), ('Fórceps.', 'Fórceps.')], default='', max_length=10, verbose_name='Tipo de Parto'),
        ),
    ]