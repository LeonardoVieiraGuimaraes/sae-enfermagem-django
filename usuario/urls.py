from django.urls import path

from .views import UsuarioCreateView, UsuarioView, UsuarioListView, PacienteListView, PacienteCreateView, \
    UsuarioDetailView, UsuarioUpdateView, UsuarioDeleteView, PacientePKCreateView, PacienteDetailView, \
    PacienteUpdateView, PacienteDeleteView

urlpatterns = [

    ################################ Url para Usuario ############################
    # path("", UsuarioView.as_view(), name="usuario.home"),
    path("", UsuarioView.as_view(), name="usuario.view"),
    path("usuario_listar", UsuarioListView.as_view(), name="usuario.list"),
    path("usuario_cadastrar", UsuarioCreateView.as_view(), name="usuario.create"),
    path("usuario_detalhar/<int:pk>", UsuarioDetailView.as_view(), name="usuario.detail"),
    path("usuario_editar/<int:pk>", UsuarioUpdateView.as_view(), name="usuario.update"),
    path("usuario_deletar/<int:pk>", UsuarioDeleteView.as_view(), name="usuario.delete"),

    ################################ Url para Paciente ############################
    path("paciente_listar", PacienteListView.as_view(), name="paciente.list"),
    path("paciente_cadastrar", PacienteCreateView.as_view(), name="paciente.create"),
    path("pacientepk_cadastrar/<int:pk>", PacientePKCreateView.as_view(), name="pacientepk.create"),
    path("paciente_detalhar/<int:pk>", PacienteDetailView.as_view(), name="paciente.detail"),
    path("paciente_editar/<int:pk>", PacienteUpdateView.as_view(), name="paciente.update"),
    path("paciente_deletar/<int:pk>", PacienteDeleteView.as_view(), name="paciente.delete"),

]
