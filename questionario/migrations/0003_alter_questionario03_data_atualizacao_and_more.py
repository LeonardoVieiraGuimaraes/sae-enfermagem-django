# Generated by Django 4.2.2 on 2023-06-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0002_questionario03_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario03',
            name='data_atualizacao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='questionario03',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
