# Generated by Django 4.2.3 on 2023-07-04 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0017_alter_questionario0302_seguranca_emocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario0302',
            name='questionario03',
            field=models.OneToOneField(default='elementary', on_delete=django.db.models.deletion.CASCADE, to='questionario.questionario03', verbose_name='Nome do Paciente'),
        ),
        migrations.AlterField(
            model_name='questionario0302',
            name='seguranca_emocional',
            field=models.CharField(blank=True, choices=[('alterações de humor', 'Alterações de Humor'), ('Crises de Choro', 'Crises de Choro'), ('Emotividade Exacerbada', 'Emotividade Exacerbada'), ('Insegurança', 'Insegurança'), ('Irritabilidade', 'Irritabilidade'), ('Tristeza', 'Tristeza'), ('Alegria', 'Alegria'), ('Medo', 'Medo'), ('Ansiedade', 'Ansiedade')], default='Alterações de Humor', max_length=200, null=True),
        ),
    ]
