from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from questionario.forms import (
    Questionario03Form,
    Questionario0301Form,
    Questionario0302Form,
    Questionario0303Form,
    Questionario0304Form,
    Questionario04Form, Questionario05Form,
)
from questionario.models import (
    Questionario03,
    Questionario0301,
    Questionario0302,
    Questionario0303,
    Questionario0304,
    Questionario04, Questionario05,
)
from usuario.models import Paciente


class Questionario03CreateView(CreateView):
    form_class = Questionario03Form
    model = Questionario03
    template_name = "questionario/questionario03/questionario03_create.html"

    # success_url = reverse_lazy('questionario01.detail')

    def get_success_url(self):
        return reverse_lazy("questionario03.detail", kwargs={"pk": self.object.pk})


# Create your views here.
class Questionario03PKCreateView(CreateView):
    form_class = Questionario03Form
    model = Questionario03
    template_name = "questionario/questionario03/questionario03_create.html"

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"paciente": self.kwargs["pk"]}

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("questionario03.detail", kwargs={"pk": self.object.pk})


class Questionario03ListView(ListView):
    model = Questionario03
    form_class = Questionario03Form
    template_name = "questionario/questionario03/questionario03_list.html"


# NECESSIDADES PSICOBIOLÓGICAS:
class Questionario03DetailView(DetailView):
    model = Questionario03
    form_class = Questionario03Form
    template_name = "questionario/questionario03/questionario03_detail.html"


class Questionario03UpdateView(UpdateView):
    model = Questionario03
    form_class = Questionario03Form
    template_name = "questionario/questionario03/questionario03_update.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("questionario03.detail", kwargs={"pk": self.object.pk})


class Questionario03DeleteView(DeleteView):
    model = Questionario03
    form_class = Questionario03Form
    template_name = "questionario/questionario03/questionario03_delete.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.pk})


class Questionario0301PKCreateView(CreateView):
    form_class = Questionario0301Form
    model = Questionario0301
    template_name = (
        "questionario/questionario03/questionario0301/questionario0301_create.html"
    )

    def get_success_url(self):
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"questionario03": self.kwargs["pk"]}


class Questionario0301DetailView(DetailView):
    model = Questionario0301
    form_class = Questionario0301Form
    template_name = (
        "questionario/questionario03/questionario0301/questionario0301_detail.html"
    )

class Questionario0301UpdateView(UpdateView):
    model = Questionario0301
    form_class = Questionario0301Form
    template_name = (
        "questionario/questionario03/questionario0301/questionario0301_update.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0301DeleteView(DeleteView):
    model = Questionario0301
    template_name = (
        "questionario/questionario03/questionario0301/questionario0301_delete.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0302PKCreateView(CreateView):
    form_class = Questionario0302Form
    model = Questionario0302
    template_name = (
        "questionario/questionario03/questionario0302/questionario0302_create.html"
    )

    def get_success_url(self):
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"questionario03": self.kwargs["pk"]}


class Questionario0302DetailView(DetailView):
    model = Questionario0302
    template_name = (
        "questionario/questionario03/questionario0302/questionario0302_detail.html"
    )


class Questionario0302UpdateView(UpdateView):
    model = Questionario0302
    form_class = Questionario0302Form
    template_name = (
        "questionario/questionario03/questionario0302/questionario0302_update.html"
    )

    def get_success_url(self):
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0302DeleteView(DeleteView):
    model = Questionario0302
    template_name = (
        "questionario/questionario03/questionario0302/questionario0302_delete.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0303PKCreateView(CreateView):
    form_class = Questionario0303Form
    model = Questionario0303
    template_name = (
        "questionario/questionario03/questionario0303/questionario0303_create.html"
    )

    def get_success_url(self):
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"questionario03": self.kwargs["pk"]}


class Questionario0303DetailView(DetailView):
    model = Questionario0303
    template_name = (
        "questionario/questionario03/questionario0303/questionario0303_detail.html"
    )


class Questionario0303UpdateView(UpdateView):
    model = Questionario0303
    form_class = Questionario0303Form
    template_name = (
        "questionario/questionario03/questionario0303/questionario0303_update.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0303DeleteView(DeleteView):
    model = Questionario0303
    template_name = (
        "questionario/questionario03/questionario0303/questionario0303_delete.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0304PKCreateView(CreateView):
    form_class = Questionario0304Form
    model = Questionario0304
    template_name = (
        "questionario/questionario03/questionario0304/questionario0304_create.html"
    )

    def get_success_url(self):
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"questionario03": self.kwargs["pk"]}


class Questionario0304DetailView(DetailView):
    model = Questionario0304
    template_name = (
        "questionario/questionario03/questionario0304/questionario0304_detail.html"
    )


class Questionario0304UpdateView(UpdateView):
    model = Questionario0304
    form_class = Questionario0304Form
    template_name = (
        "questionario/questionario03/questionario0304/questionario0304_update.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


class Questionario0304DeleteView(DeleteView):
    model = Questionario0303
    template_name = (
        "questionario/questionario03/questionario0303/questionario0303_delete.html"
    )

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy(
            "questionario03.detail", kwargs={"pk": self.object.questionario03_id}
        )


# MATERNIDADE
# ADMISSÃO OBSTÉTRICA
class Questionario04CreateView(CreateView):
    form_class = Questionario04Form
    model = Questionario04
    template_name = "questionario/questionario04/questionario04_create.html"

    # success_url = reverse_lazy('questionario01.detail')

    def get_success_url(self):
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.pk})


class Questionario04PKCreateView(CreateView):
    form_class = Questionario04Form
    model = Questionario04
    template_name = "questionario/questionario04/questionario04_create.html"

    def get_initial(self):
        # paciente = Paciente.objects.all()
        return {"paciente": self.kwargs["pk"]}

    def get_success_url(self):
        print(self.object.pk)
        # return para paciente.detail
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.paciente.pk})

class Questionario04ListView(ListView):
    model = Questionario04
    form_class = Questionario04Form
    template_name = "questionario/questionario04/questionario04_list.html"


class Questionario04DetailView(DetailView):
    model = Questionario04
    form_class = Questionario04Form
    template_name = "questionario/questionario04/questionario04_detail.html"


class Questionario04UpdateView(UpdateView):
    model = Questionario04
    form_class = Questionario04Form
    template_name = "questionario/questionario04/questionario04_update.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("questionario04.detail", kwargs={"pk": self.object.pk})


class Questionario04DeleteView(DeleteView):
    model = Questionario04
    form_class = Questionario04Form
    template_name = "questionario/questionario04/questionario04_delete.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.pk})

class Questionario05CreateView(CreateView):
    form_class = Questionario05Form
    model = Questionario05
    template_name = "questionario/questionario05/questionario05_create.html"

    # success_url = reverse_lazy('questionario01.detail')

    def get_success_url(self):
        return reverse_lazy("questionario05.detail", kwargs={"pk": self.object.pk})


class Questionario05PKCreateView(CreateView):
    form_class = Questionario05Form
    model = Questionario05
    template_name = "questionario/questionario05/questionario05_create.html"

    def get_initial(self):
        # pacientes = Paciente.objects.all()
        return {"paciente": self.kwargs["pk"]}

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.paciente.pk})


class Questionario05ListView(ListView):
    model = Questionario05
    form_class = Questionario05Form
    template_name = "questionario/questionario05/questionario05_list.html"


class Questionario05DetailView(DetailView):
    model = Questionario05
    form_class = Questionario05Form
    template_name = "questionario/questionario05/questionario05_detail.html"


class Questionario05UpdateView(UpdateView):
    model = Questionario05
    form_class = Questionario05Form
    template_name = "questionario/questionario05/questionario05_update.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("questionario05.detail", kwargs={"pk": self.object.pk})


class Questionario05DeleteView(DeleteView):
    model = Questionario05
    form_class = Questionario05Form
    template_name = "questionario/questionario05/questionario05_delete.html"

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy("paciente.detail", kwargs={"pk": self.object.pk})
