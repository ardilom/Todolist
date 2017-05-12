from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from models import Task

import json
from django.http import QueryDict
# Create your views here.

### ROUTES ###

def tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'tasks.html', {'tasks': tasks})
        
    if request.method == "POST": #TODO Usar vista de clases para responder al POST (upgraded en django 1.10)
        name = request.POST.get("name")
        task = Task(name=name)
        task.save()
        return HttpResponseRedirect('/tasks')
        
def index(request):
    return HttpResponseRedirect('/tasks')
 

def update_task(request, task_id):
    if request.method == "POST":
        action_type = request.POST.get("action_type")
        
        if action_type == "complete":
            complete_task(task_id)

        elif action_type == "edit":
            edit_text = request.POST.get("editText")
            edit_task(task_id, edit_text)
        
        elif action_type == "delete":
            delete_task(task_id) 
            
        elif action_type == "increase_priority":
            increase_priority_task(task_id)
            
        elif action_type == "decrease_priority":
            decrease_priority_task(task_id)
            
    return HttpResponseRedirect("/tasks")

  
### METHODS ### 

def complete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.complete()
    task.save()
    
def edit_task(task_id, edit_text):
    task = Task.objects.get(id=task_id)
    task.name = edit_text
    task.save()
    
def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()


def increase_priority_task(task_id):
    task = Task.objects.get(id=task_id)
    task.increasePriority()
    
def decrease_priority_task(task_id):
    task = Task.objects.get(id=task_id)
    task.decreasePriority()
