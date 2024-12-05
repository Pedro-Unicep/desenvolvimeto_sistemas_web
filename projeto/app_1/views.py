from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import UserForm, TaskForm, UserDeleteForm
from .models import User, Task

def index(request):
    return render(request, 'index.html')

def create_and_delete_user(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                if User.objects.filter(cpf=user_form.cleaned_data['cpf']).exists():
                    return redirect('user_in_database')
                else:
                    user_form.save()
                    return redirect('successful_user_creation')
        elif 'delete_user' in request.POST:
            delete_form = UserDeleteForm(request.POST)
            if delete_form.is_valid():
                cpf = delete_form.cleaned_data['cpf']
                user = User.objects.get(cpf=cpf)
                user.delete()
                messages.success(request, "User successfully deleted.")
                return redirect('user_successfully_deleted')
    else:
        user_form = UserForm()
        delete_form = UserDeleteForm()
    return render(request, 'create_user.html', {'user_form': user_form, 'delete_form': delete_form})

def user_successfully_deleted(request):
    return render(request, 'user_successfully_deleted.html')

def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})

def user_in_database(request):
    return render(request, 'user_in_database.html')

def successful_user_creation(request):
    return render(request, 'successful_user_creation.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successful_task_creation')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'success': True})

def successful_task_creation(request):
    return render(request, 'successful_task_creation.html')

def list_tasks(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = user.tasks.all()
    return render(request, 'list_tasks.html', {'user': user,'tasks': tasks})
