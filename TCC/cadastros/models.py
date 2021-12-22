from django.db import models
from django.contrib.auth.models import User

def user_path(instance, filename):

    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

class Orientador(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

class Curso(models.Model):
    MODALIDADES = (
        (1, 'Informática'),
        (2, 'Eletromecânica'),
        (3, 'Edificações')
    )
    modalidades = models.IntegerField(choices=MODALIDADES)

class Relatorio(models.Model):
    autor = models.ManyToManyField(Autor)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=150)
    resumo = models.TextField()
    palavras_chave = models.CharField(max_length=250)
    ano_documento = models.IntegerField()
    local_estagio = models.CharField(max_length=150)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='pdf/')

    def __str__(self):
        return "[{}] {} - {}/{}".format(self.pk, self.arquivo, self.curso, self.local_estagio, self.ano_documento,
                                        self.ano_documento, self.palavras_chave, self.resumo, self.supervisor, self.orientador,
                                        self.autor)