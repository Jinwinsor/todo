from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


def addTask(request):
    # print(request.POST['task'])  # 'task' : Input 'name'
    task = request.POST['task']  # Input 'name'
    # task = 'task' from models. / and task of above task.
    Task.objects.create(task=task)
    return redirect('home')
