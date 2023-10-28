from django import forms
from django.forms import RadioSelect

from questionario.models import (
    Questionario03,
    Questionario0301,
    Questionario0302,
    Questionario0303,
    Questionario0304,
    Questionario04, Questionario05,
)


class Questionario03Form(forms.ModelForm):
    class Meta:
        model = Questionario03
        fields = "__all__"
        widgets = {
            "data_parto": forms.DateInput(attrs={"type": "date"}),
            "hora_parto": forms.TimeInput(attrs={"type": "time"}),
        }


# NECESSIDADES PSICOBIOLÓGICAS:
class Questionario0301Form(forms.ModelForm):
    # perineo = forms.MultipleChoiceField(choices=Questionario0301.choices_perineo, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Questionario0301
        fields = "__all__"


class Questionario0302Form(forms.ModelForm):
    class Meta:
        model = Questionario0302
        fields = "__all__"


class Questionario0303Form(forms.ModelForm):
    avaliacao_01 = forms.ChoiceField(
        label="Avaliação",
        widget=RadioSelect(),
        choices=Questionario0303.choices_avaliacao,
    )
    avaliacao_02 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_03 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_04 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_05 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_06 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_07 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_08 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_09 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_10 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )
    avaliacao_11 = forms.ChoiceField(
        label="", widget=RadioSelect(), choices=Questionario0303.choices_avaliacao
    )

    class Meta:
        model = Questionario0303
        fields = "__all__"


class Questionario0304Form(forms.ModelForm):
    class Meta:
        model = Questionario0304
        fields = "__all__"


class Questionario04Form(forms.ModelForm):
    class Meta:
        model = Questionario04
        fields = "__all__"
        widgets = {
            "data_adminissao": forms.DateInput(attrs={"type": "date"}),
            "data_parto": forms.DateInput(attrs={"type": "date"}),
            "dpp": forms.DateInput(attrs={"type": "date"}),
            "hora_admissao": forms.TimeInput(attrs={"type": "time"}),
            "hora_nascimento": forms.TimeInput(attrs={"type": "time"}),
            "toque_vaginal_hora_toque": forms.TimeInput(attrs={"type": "time"}),
            "dinamica_uterina_tempo": forms.TimeInput(attrs={"type": "time"}),
            "apgar_1": forms.TimeInput(attrs={"type": "time"}),
            "apgar_5": forms.TimeInput(attrs={"type": "time"}),
            "apgar_10": forms.TimeInput(attrs={"type": "time"}),

        }

class Questionario05Form(forms.ModelForm):
    class Meta:
        model = Questionario05
        fields = "__all__"
