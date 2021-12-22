from django.contrib import admin
from .models import Autor, Orientador, Curso, Relatorio

admin.site.register(Autor)
admin.site.register(Orientador)
admin.site.register(Curso)
admin.site.register(Relatorio)
