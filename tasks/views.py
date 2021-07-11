import json, requests

from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request, 'tasks/index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
        'task' : task
    }
    return render(request, 'tasks/delete.html', context)

def crossTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('/')

def uncrossTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = False
    task.save()
    return redirect('/')

def projects(request):
    """Here we'll read data from a json file and pass it to projects.html"""
    final = []
    with open('tasks/api.json') as json_data:
        my_var = json.load(json_data)
        for i in range(len(my_var)):
            projects = {}
            project_name = my_var[i]['name']
            url = my_var[i]['html_url']
            projects["name"] = project_name
            projects["url"] = url

            final.append(projects)

    context = {
        'projects' : final
    }

    return render(request, 'tasks/projects.html', context)
