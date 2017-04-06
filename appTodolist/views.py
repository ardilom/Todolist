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
    elif request.method == "PUT":
        body = request.body.decode('utf-8')
        try:
            body = json.loads(body)
        except ValueError:
            return HttpResponseNotFound('<h1>Error</h1>')
        task = Task.objects.get(id=body.get('id'))
        task.name = body.get('name')
        task.save()
        return HttpResponseRedirect('/list_task')
        
def list_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})
        
def complete_tasks(request):
    if request.method == "POST":
        id = request.POST.get("id")
        type = request.POST.get("action_type") # elegir que tipo de accion llega del template, edit o complete
        if type == "Complete":
            task = Task.objects.get(id=id)
            task.complete()
            task.save()
            return HttpResponseRedirect("/list_task")
        else:
            body = request.body.decode('utf-8')
            try:
                body = json.loads(body)
            except ValueError:
                return HttpResponseNotFound('<h1>Error</h1>')
            task = Task.objects.get(id=id)
            task.name = request.POST.get("editText")
            task.save()
            return HttpResponseRedirect("/list_task")

def delete_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        task = Task.objects.get(id=id)
        try:
            task = Task.objects.get(foo='bar')
        except Task.DoesNotExist:
            task = None
            
        if task != None:
            task.delete()
            return HttpResponseRedirect('/list_tasks')
        
        else:
            return HttpResponseNotFound('Error')
        



