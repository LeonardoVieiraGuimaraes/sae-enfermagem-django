# Generated by Django 4.2.3 on 2023-07-21 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0025_questionario0303_avaliacao_01_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario0303',
            name='avaliacao_conduta_enfermagem',
            field=models.TextField(default='', max_length=2000, verbose_name='Avaliação e/ou Conduta de Enfermagem'),
        ),
        migrations.AddField(
            model_name='questionario0303',
            name='avaliacao_conduta_enfermagem_hora',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Hora:'),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='data_atualizacao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='questionario0304',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_01',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=150, verbose_name='Avaliação'),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_02',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_03',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_04',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_05',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_06',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_07',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_08',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_09',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_10',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='questionario0303',
            name='avaliacao_11',
            field=models.CharField(choices=[('Melhorado', 'Melhorado'), ('Piorado', 'Piorado'), ('Inalterado', 'Inalterado'), ('Resolvido', 'Resolvido')], default='', max_length=30, verbose_name=''),
        ),
    ]