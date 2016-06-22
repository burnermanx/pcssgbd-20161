from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/5/
    url(r'^turma/(?P<id_turma>.+)/aluno/(?P<mat_aluno>[0-9]+)/nota/(?P<nota_aluno>[0-9]+)/$', views.aprovaAluno, name='aprovaaluno'),
    # ex: /polls/5/results/
    url(r'^turma/(?P<question_id>[0-9]+)/results/$', views.cadastrarTurma, name='cadastraturma'),

    url(r'^alunos/', views.listarAlunos, name='listarAlunos')
]