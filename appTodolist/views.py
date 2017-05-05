from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from models import Task

import json
from django.http import QueryDict
# Create your views here.

def add_task(request):
    if request.method == "POST": #TODO Usar vista de clases para responder al POST (upgraded en django 1.10)
        name = request.POST.get("name")
        task = Task(name=name)
        task.save()
        return HttpResponseRedirect('/list_task')
        
def list_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'tasks.html', {'tasks': tasks})
        
def complete_tasks(request):
    if request.method == "POST":
        id = request.POST.get("id")
        type = request.POST.get("action_type")
        if type == "Completar":
            task = Task.objects.get(id=id)
            task.complete()
            task.save()
            return HttpResponseRedirect("/list_task")
        else:
            task = Task.objects.get(id=id)
            task.name = request.POST.get("editText")
            task.save()
            return HttpResponseRedirect("/list_task")

def delete_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect('/list_tasks')


def increase_priority_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        task = Task.objects.get(id=id)
        task.increasePriority()
        return HttpResponseRedirect('/list_tasks')

def decrease_priority_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        task = Task.objects.get(id=id)
        task.decreasePriority()
        return HttpResponseRedirect('/list_tasks')