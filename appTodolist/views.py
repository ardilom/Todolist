from django.shortcuts import render, HttpResponse
from models import Task

# Create your views here.

def add_task(request):
    if request.method == "POST": #TODO Usar vista de clases para responder al POST (upgraded en django 1.10)
        name = request.POST.get("name")
        task = Task(name=name)
        task.save()
        return HttpResponse("", status=200)
        
def list_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        response = []
        for t in tasks:
            response.append(t.name)
        response = '-'.join(response)
        return HttpResponse(response, status=200)
        
def complete_tasks(request):
    if request.method == "POST":
        name = request.POST.get("name")
        task = list(Task.objects.filter(name=name))[0]
        task.complete()
        task.save()
        return HttpResponse("", status=200)