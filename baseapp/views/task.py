from django.shortcuts import render, redirect
from ..models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def create(request):
    if request.method == 'POST':
        values = { key:value for key,value in request.POST.items() }
        values['complete'] =  request.POST.get('complete', False)
        if 'csrfmiddlewaretoken' in values: del values['csrfmiddlewaretoken']

        Task.objects.create(**values)
        return redirect('tasks')

    return render(request, 'tasks/create.html')

def update(request, id):
    task = Task.objects.get(pk=id)

    if request.method == 'POST':
        data = request.POST

        task.title = data['title']
        task.description = data['description']
        task.complete = data.get('complete', False)
        task.save()

        return redirect('tasks')

    return render(request, 'tasks/update.html', {'task': task})

def delete(request):
    return render(request, 'tasks/create.html')