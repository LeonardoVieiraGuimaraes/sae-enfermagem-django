# Generated by Django 4.2.3 on 2023-07-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0018_alter_questionario0302_questionario03_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario0302',
            name='seguranca_emocional',
            field=models.CharField(blank=True, choices=[('alterações de humor', 'Alterações de Humor'), ('Crises de Choro', 'Crises de Choro'), ('Emotividade Exacerbada', 'Emotividade Exacerbada'), ('Insegurança', 'Insegurança'), ('Irritabilidade', 'Irritabilidade'), ('Tristeza', 'Tristeza'), ('Alegria', 'Alegria'), ('Medo', 'Medo'), ('Ansiedade', 'Ansiedade')], default='', max_length=200, null=True),
        ),
    ]
