from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView

from .forms import UsuarioForm, PacienteForm
from .models import Usuario, Paciente


class UsuarioView(TemplateView):
    template_name = "usuario/index.html"


# # class Cabecalho(TemplateView):
# #     template_name = "base/cabeçalho.html"

class UsuarioListView(ListView):
    model = Usuario
    form_class = UsuarioForm
    context_object_name = 'usuario'
    template_name = "usuario/usuario/usuario_list.html"

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            usuario = Usuario.objects.filter(
                nome__icontains=txt_nome)

        else:
            usuario = Usuario.objects.all()

        return usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario/usuario_create.html"

    # success_url = reverse_lazy('usuario.detail')

    def get_success_url(self):
        return reverse_lazy('usuario.detail', kwargs={'pk': self.object.pk})


class UsuarioDetailView(DetailView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario/usuario_detail.html"


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/usuario/usuario_delete.html"
    success_url = reverse_lazy('usuario.list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario/usuario_update.html"
    success_url = reverse_lazy('usuario.list')


class PacienteListView(ListView):
    model = Paciente
    context_object_name = 'paciente'
    template_name = "usuario/paciente/paciente_list.html"

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            paciente = Paciente.objects.filter(
                nome__icontains=txt_nome)

        else:
            paciente = Paciente.objects.all()

        return paciente


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_create.html"
    success_url = reverse_lazy('paciente.list')

    # def get_success_url(self):
    #     return reverse_lazy('usuario.detail', kwargs={'pk': self.object.pk})


class PacientePKCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_create.html"
    success_url = reverse_lazy('paciente.list')

    def get_initial(self):
        # usuario = Usuario.objects.all().filter(pk=self.kwargs["pk"])[0]
        # # usuario = self.kwargs["pk"]
        # print(usuario)
        # # print(usuario)
        # return {'usuario': usuario}
        return {'usuario': self.kwargs["pk"]}

    def get_success_url(self):
        return reverse_lazy('paciente.detail', kwargs={'pk': self.object.pk})


class PacienteDetailView(DetailView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_detail.html"


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = "usuario/paciente/paciente_delete.html"
    success_url = reverse_lazy('paciente.list')


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "usuario/paciente/paciente_update.html"

    def get_success_url(self):
        return reverse_lazy('paciente.detail', kwargs={'pk': self.object.pk})
