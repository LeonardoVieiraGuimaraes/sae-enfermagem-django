from django import forms
from django.forms import DateInput

from .models import Usuario, Paciente


################################################# Forms Usuario ######################
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'}),
        }


################################################# Forms Paciente ######################
# class DateInput(forms.DateInput):
#     input_type = 'date'
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"


#####################################################################

# # CIRURGIA PROPOSTA
# cirurgia_proposta = forms.CharField()

# # Sala Cirurgica:
# sala_cirugica = forms.CharField()

# # Data da Cirurgia:
# data_cirurugia = forms.DateField()
# # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
# modalidade = forms.CharField()

# # COMORBIDADE
# comorbidade = forms.CharField()
# class UsuarioForm(forms.ModelForm):

#     # data_nascimento = forms.DateField(widget=forms.DateInput(
#     #     format='%Y-%m-%d', attrs={"type": 'date'}))

#     # data_cadastro = forms.DateField(widget=forms.DateInput(
#     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

#     # cpf = forms.CharField(label="CPF")

#     # nome_mae = forms.CharField(label="Nome da Mãe")
#     # nome_pai = forms.CharField(label="Nome do Pai", required=False)

#     class Meta:
#         model = Usuario
#         fields = "__all__"


# # class PacienteForm(UsuarioForm):

# #     # data_nascimento = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date'}))

# #     # data_cadastro = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

# #     # cpf = forms.CharField(label="CPF")

# #     # nome_mae = forms.CharField(label="Nome da Mãe")
# #     # nome_pai = forms.CharField(label="Nome do Pai", required=False)

# #     # USUÁRIO
# #     # DATA NASCIMENTO
# #     # NOME DA MÃE
# #     # usuario = forms.ModelChoiceField(queryset = Usuario.objects.all(), label = "Usuario", widget = forms.Select())
# #     # PRONTUÁRIO
# #     # prontuario = forms.CharField()

# #     # # CIRURGIA PROPOSTA
# #     # cirurgia_proposta = forms.CharField()

# #     # # Sala Cirurgica:
# #     # sala_cirugica = forms.CharField()

# #     # # Data da Cirurgia:
# #     # data_cirurugia = forms.DateField()
# #     # # Modalidade ( ) Eletiva (  )Urgência ( )Emergência
# #     # modalidade = forms.CharField()

# #     # # COMORBIDADE
# #     # comorbidade = forms.CharField()

# #     # data_cadastro = forms.DateField(widget=forms.DateInput(
# #     #     format='%Y-%m-%d', attrs={"type": 'date', 'readonly': 'readonly'}), initial=date.today())

# #     class Meta:
# #         model = Paciente
# #         fields = "__all__"
