from django.shortcuts import render
from todos.models import Task


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at')
    c_task = Task.objects.filter(is_completed = True)
    context = {
        'tasks' : task,
        'c_tasks' : c_task
    }
    return render(request, 'home.html', context)