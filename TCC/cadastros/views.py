from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Autor, Orientador, Curso, Relatorio
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

class AutorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'sobrenome']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('index')

class OrientadorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Orientador
    fields = ['nome', 'sobrenome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CursoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class RelatorioCreate(GroupRequiredMixin,LoginRequiredMixin ,CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Relatorio
    fields = ['autor', 'orientador', 'supervisor', 'resumo', 'resumo', 'palavras_chave', 'ano_documento', 'local_estagio', 'curso', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('index')

                                 ## UPDATE ##

class AutorUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'sobrenome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class OrientadorUpdate(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Orientador
    fields = ['nome', 'sobrenome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-orientadores')

class CursoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class RelatorioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Relatorio
    fields = ['autor', 'orientador', 'supervisor', 'resumo', 'resumo', 'palavras_chave', 'ano_documento',
              'local_estagio', 'curso', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorios')



                                ##  DELETE  ##

class AutorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class OrientadorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Orientador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-orientadores')

class CursoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class RelatorioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Relatorio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-relatorios')


                                ##  LISTA  ##


class OrientadorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Orientador
    template_name = 'cadastros/listas/orientador.html'


class RelatorioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Relatorio
    template_name = 'cadastros/listas/relatorio.html'
