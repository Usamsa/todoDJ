from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def addTask(request):
    add_tkn = request.POST['task']
    Task.objects.create(task = add_tkn)
    return redirect('home')

def mrk_as_d(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mrk_as_ud(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_tasks': get_task
        }
        return render(request, 'edit.html', context)
    
def delete(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')
