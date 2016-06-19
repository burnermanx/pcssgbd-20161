from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.CharField(primary_key=True, null=False, max_length=14)
    nome = models.CharField(null=False, max_length=255)
    telefoneResidencial = models.CharField(max_length=50)
    telefoneCelular = models.CharField(max_length=50)
    dataNascimento = models.DateField(null=False)

class Endereco(models.Model):
    logradouro = models.CharField(null=False, max_length=150)
    numero = models.CharField(null=False, max_length=50)
    cep = models.IntegerField(null=False)
    cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = (('logradouro', 'numero', 'cep', 'cpf'),)

class Professor(models.Model):
    cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=False)
    matricula = models.CharField(primary_key=True, null=False, max_length=50)
    dataContratacao = models.DateField(null=False)
    dataSaida = models.DateField

class Aluno(models.Model):
    matricula = models.CharField(primary_key=True, null=False, max_length=50)
    cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=False)

class Curso(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    nome = models.CharField(null=False, max_length=150)
    numModulos = models.IntegerField(null=False)

class InscricaoCurso(models.Model):
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False)
    matriculaAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = (('idCurso', 'matriculaAluno'),)

class Materia(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    idCurso = models.ForeignKey(Curso, null=False)
    nome = models.CharField(null=False, max_length=150)
    cargaHoraria = models.IntegerField(null=False)
    modulo = models.CharField(null=False, max_length=150)

class Turma(models.Model):
    id = models.IntegerField(primary_key=True, null= False)
    idMateria = models.ForeignKey(Materia, null=False)
    dataInicio = models.DateField(null=False)
    dataFim = models.DateField(null=False)
    media = models.IntegerField(null=False)
    status = models.CharField(null=False, max_length=150)
    horarioTurma = models.TimeField(null=False)
    matriculaProfessor = models.ForeignKey(Professor, null=False)
    matriculaAluno = models.ForeignKey(Aluno, null=False)

class Nota(models.Model):
    matriculaAluno = models.ForeignKey(Aluno, null=False)
    idMateria = models.ForeignKey(Materia, null=False)
    idTurma = models.ForeignKey(Turma, null=False)
    nota = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    aprovado = models.BooleanField
    class Meta:
        unique_together = (('matriculaAluno', 'idMateria', 'idTurma'),)