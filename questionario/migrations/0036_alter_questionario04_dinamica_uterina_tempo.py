# Generated by Django 4.2.3 on 2023-09-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questionario", "0035_alter_questionario05_contracoes_uterinas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionario04",
            name="dinamica_uterina_tempo",
            field=models.TimeField(default="", verbose_name="Tempo"),
        ),
    ]
