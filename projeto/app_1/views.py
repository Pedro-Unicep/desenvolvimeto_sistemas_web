from django.shortcuts import render
from django.http import HttpResponse

from .models import Usuario

def sincrono_view(request):
    return render(request, 'sincrono.html')

def assincrono_view(request):
    return render(request, 'assincrono.html')

def fetch_teste_txt(request):
    try:
        with open('app_1/teste.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        content = 'Arquivo não encontrado.'
    return HttpResponse(content)


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

