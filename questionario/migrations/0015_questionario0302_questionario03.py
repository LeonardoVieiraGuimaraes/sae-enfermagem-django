# Generated by Django 4.2.3 on 2023-07-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0014_questionario0301_amamentacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario0302',
            name='questionario03',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='questionario.questionario03', verbose_name='Nome do Paciente'),
        ),
    ]
