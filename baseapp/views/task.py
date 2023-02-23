from django.shortcuts import render, redirect
from ..models import Task
from django.http import JsonResponse
from django.forms.models import model_to_dict


def index(request):
    context = {
        'tasks': Task.objects.all(),
        'states': Task.states
    }
    return render(request, 'tasks/index.html', context)

def create(request):
    if request.method == 'POST':
        values = { key:value for key,value in request.POST.items() }
        values['complete'] =  request.POST.get('complete', False)
        values['state'] = 'new'
        if 'csrfmiddlewaretoken' in values: del values['csrfmiddlewaretoken']

        rec = Task.objects.create(**values)
        data = model_to_dict(rec)

        return JsonResponse({
            'success': True,
            'msg': 'Task has been created',
            'data': data
        })

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