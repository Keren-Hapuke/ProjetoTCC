from django.urls import path
from .views import AutorCreate, OrientadorCreate, CursoCreate, RelatorioCreate
from .views import AutorUpdate, OrientadorUpdate, CursoUpdate, RelatorioUpdate
from .views import AutorDelete, OrientadorDelete, CursoDelete, RelatorioDelete
from .views import OrientadorList, RelatorioList


urlpatterns = [
    path('cadastrar/autor', AutorCreate.as_view(), name='cadastrar-autor'),
    path('cadastrar/orientador', OrientadorCreate.as_view(), name='cadastrar-orientador'),
    path('cadastrar/curso', CursoCreate.as_view(), name='cadastrar-curso'),
    path('cadastrar/relatorio', RelatorioCreate.as_view(), name='cadastrar-relatorio'),

    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name="editar-autor"),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name="editar-orientador"),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name="editar-curso"),
    path('editar/relatorio/<int:pk>/', RelatorioUpdate.as_view(), name="editar-relatorio"),

    path('excluir/autor/<int:pk>/', AutorDelete.as_view(), name="excluir-autor"),
    path('excluir/orientador/<int:pk>/', OrientadorDelete.as_view(), name="excluir-orientador"),
    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name="excluir-curso"),
    path('excluir/relatorio/<int:pk>/', RelatorioDelete.as_view(), name="excluir-relatorio"),

    path('lista/orientadores/', OrientadorList.as_view(), name="listar-orientadores"),
    path('lista/relatorios/', RelatorioList.as_view(), name="listar-relatorios"),
]