from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
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
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        action_type = request.POST.get("action_type")
        
        if action_type == "complete":
            task.complete()
            task.save()

        elif action_type == "edit":
            edit_text = request.POST.get("editText")
            task.name = edit_text
            task.save()
        
        elif action_type == "delete":
            task.delete()
            
        elif action_type == "increase_priority":
            task.increasePriority()
            
        elif action_type == "decrease_priority":
            task.decreasePriority()
            
    return HttpResponseRedirect("/tasks")
