from cpf_field.models import CPFField
from django.db import models


# from django_choices_field import TextChoicesField

# Create your models here.

class Usuario(models.Model):
    choices_raca = (
        ("Pardo", "Pardo"), ("Branco", "Branco"), ("Preto", "Preto"), ("Amarelo", "Amarelo"), ("Indígena", "Indígena"))
    choices_estado_civil = (
        ("Solteiro", "Solteiro"), ("Casado", "Casado"), ("Divorciado", "Divorciado"), ("Viúvo", "Viúvo"))
    choices_escolaridade = (
        ("Fundamental - incompleto", "Fundamental - incompleto"), ("Fundamental - completo", "Fundamental - completo"),
        ("Médio - incompleto", "Médio - incompleto"), ("Médio - completo", "Médio - completo"),
        ("Superior - incompleto", "Superior - incompleto"), ("Superior - completo", "Superior - completo"),
        ("Pós-graduação - incompleto", "Pós-graduação - incompleto"),
        ("Pós-graduação - completo", "Pós-graduação - completo"), ("Mestrado - incompleto", "Mestrado - incompleto"),
        ("Mestrado - completo", "Mestrado - completo"), ("Doutorado - incompleto", "Doutorado - incompleto"),
        ("Doutorado - completo", "Doutorado - completo"), ("Pós-doutorado - incompleto", "Pós-doutorado - incompleto"),
        ("Pós-doutorado - completo", "Pós-doutorado - completo"), ("Não se aplica", "Não se aplica"),
        ("Não informado", "Não informado"))

    cpf = CPFField(default='', max_length=14, unique=True)
    nome = models.CharField(default='', max_length=100)
    data_nascimento = models.DateField('data de Nascimento', default='')
    estado_civil = models.CharField(default='', max_length=50, choices=choices_estado_civil)
    escolaridade = models.CharField(default='', max_length=50, choices=choices_escolaridade)
    profissao_ocupacao = models.CharField("Profissão/Ocupação", default='', max_length=100)
    raca = models.CharField("Raça", choices=choices_raca, default='', max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    prontuario = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.usuario.nome

# class Colaborador(models.Model):
#     nome = models.OneToOneField(Usuario, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.nome
