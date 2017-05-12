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
 

def update_task(request, task_id):
    if request.method == "POST":
        action_type = request.POST.get("action_type")
        
        if action_type == "complete":
            complete_task(task_id)
            return HttpResponseRedirect("/list_task")

        elif action_type == "edit":
            edit_text = request.POST.get("editText")
            edit_task(task_id, edit_text)

        return HttpResponseRedirect("/list_task")

            
def complete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.complete()
    task.save()
    
def edit_task(task_id, edit_text):
    task = Task.objects.get(id=task_id)
    task.name = edit_text
    task.save()
    
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