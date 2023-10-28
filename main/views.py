# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# Create your views here.

# class BaseView(TemplateView):
#     template_name = "base/main.html"

class MainView(TemplateView):
    template_name = "main/index.html"
# # class Cabecalho(TemplateView):
# #     template_name = "base/cabeçalho.html"
