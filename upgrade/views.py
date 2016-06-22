from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from upgrade.models import Turma, Nota, Aluno, Professor, Pessoa


def cadastrarTurma(request, capacidade, horarioInicial, horarioFinal, professor, sala, status):
    turma = Turma()

    turma.capacidade = capacidade
    turma.horarioInicial = horarioInicial
    turma.horarioFinal = horarioFinal
    turma.matriculaProfessor = professor
    turma.sala = sala
    turma.status = status

    if turma.professorDisponivel(professor, horarioInicial):
        return HttpResponse("Professor já ocupado no horário")

    def professorDisponivel(matriculaProfessor, horarioInicial):
        turmas = turmasProfessor(matriculaProfessor)

        if turmas is not None:
            for turma in turmas:
                if turma.horarioInicial == horarioInicial:
                    return False

        return True

    def turmasProfessor(matriculaProfessor):
        return Turma.objects.filter(matriculaProfessor__in=matriculaProfessor)



    return HttpResponse("Adicionada nova turma")



def aprovaAluno(request, mat_aluno, id_turma, nota_aluno):
    nota = Nota()
    nota.matriculaAluno = Aluno.objects.get(matricula=mat_aluno)
    nota.idTurma = Turma.objects.get(id=id_turma)
    nota.idMateria = Turma.objects.get(id=id_turma).idMateria
    nota.nota = Decimal(nota_aluno)

    media = Turma.objects.get(id=id_turma).media

    if int(nota_aluno) >= media:
        nota.aprovado = True
    else:
        nota.aprovado = False

    situacao = ""

    if nota.aprovado:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    nota.save()

    response = "{ \"mat_aluno\": \"" + mat_aluno + "\", \"situação\": \"" + situacao + "\" }"

    httpResponse = HttpResponse(response)
    httpResponse['Content-Type'] = 'application/json'
    return httpResponse

def listarAlunos(request):
    response = "{\"alunos\" : ["

    contaAlunos = Aluno.objects.count()

    i = 1;
    for a in Aluno.objects.all():
        pessoa = Pessoa.objects.get(aluno__matricula=a.matricula)

        response = response + "{\"aluno\": \"" + pessoa.nome + \
                   "\",  \"matricula\": \"" + a.matricula + "\" , \"cpf\": \"" + pessoa.cpf + "\" }"
        if (i < contaAlunos):
            response = response + ","
        i = i + 1

    response = response + "]}"

    httpResponse = HttpResponse(response)
    httpResponse['Content-Type'] = 'application/json'

    return httpResponse