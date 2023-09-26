from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render

def alunoView(request):
    aluno_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': aluno_list}) #caso apareça erro verificar o plural de aluno(s)
