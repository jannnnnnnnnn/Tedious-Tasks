from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Sum

# Create your views here.


def home(request):
    task_list = Task.objects.all()
    task_form = TaskForm()
    total = Task.objects.aggregate(Sum('time'))
    print(total)
    return render(request, 'index.html', {'task_list': task_list, 'task_form': task_form, 'total': total})


def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.save()
    return redirect('home')


def remove_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')
