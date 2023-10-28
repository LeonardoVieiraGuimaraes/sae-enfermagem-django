# Generated by Django 4.2.3 on 2023-07-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questionario", "0032_questionario04_data_atualizacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionario04",
            name="data_atualizacao",
            field=models.DateField(auto_now=True, verbose_name="Data de Atualização"),
        ),
        migrations.AlterField(
            model_name="questionario04",
            name="data_cadastro",
            field=models.DateField(auto_now_add=True, verbose_name="Data de Cadastro"),
        ),
    ]
