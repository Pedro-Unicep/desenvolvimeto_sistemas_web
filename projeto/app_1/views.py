from django.shortcuts import render, redirect
from .forms import UserForm, TaskForm
from .models import User

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(cpf=form.cleaned_data['cpf']).exists():
                return redirect('user_in_database')
            else:
                form.save()
                return redirect('successful_user_creation')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

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

def successful_task_creation(request):
    return render(request, 'successful_task_creation.html')

def list_tasks(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = user.tasks.all()
    return render(request, 'list_tasks.html', {'user': user,'tasks': tasks})
