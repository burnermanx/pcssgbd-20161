from django.contrib import admin
from .models import Pessoa, Aluno, Turma, Materia, Curso, Professor, Nota, Endereco

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Nota)
admin.site.register(Endereco)
