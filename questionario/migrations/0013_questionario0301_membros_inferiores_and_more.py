# Generated by Django 4.2.2 on 2023-06-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0012_questionario0301_abdome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario0301',
            name='membros_inferiores',
            field=models.CharField(choices=[('Sem alterações', 'Sem alterações'), ('Edema', 'Edema'), ('Varizes', 'Varizes'), ('Deambulante', 'Deambulante')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='questionario0301',
            name='sinal_homans',
            field=models.CharField(choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='questionario0301',
            name='sono_repouso',
            field=models.CharField(choices=[('Satisfatório', 'Satisfatório'), ('Insatisfatório', 'Insatisfatório')], default='', max_length=30),
        ),
    ]
