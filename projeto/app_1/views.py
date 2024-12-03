from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def index(request):
    return render(request, 'home.html')

def submit_form(request):
    if request.method == 'POST':
        try:
            nome_user = request.POST.get('nome')
            senha_user = request.POST.get('senha')
            try:
                usuario = Usuario.objects.get(nome = nome_user, senha=senha_user)
                return HttpResponse('Dados conferem com registro existente.')
            except Usuario.DoesNotExist:
                return HttpResponse('Dados não encontrados no banco de dados.')
        except Exception as e:
            return HttpResponse('Erro ao processar a requisição.', status=500)
    return render('Método não permitido', status=405)

