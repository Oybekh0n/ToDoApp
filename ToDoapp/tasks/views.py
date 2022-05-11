from django.shortcuts import redirect, render

from .forms import TaskForm


from .models import Task

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    tasks = Task.objects.all()
    context = {
        'tasks':tasks,
        'form':form,
    }
    return render(request, 'tasks/list.html', context)
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form,
    }
    return render(request, 'tasks/update.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {
        'task':task,
    }
    return render(request,'tasks/delete.html', context)