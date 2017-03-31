from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Task

# Create your views here.

def add_task(request):
    if request.method == "POST": #TODO Usar vista de clases para responder al POST (upgraded en django 1.10)
        name = request.POST.get("name")
        task = Task(name=name)
        task.save()
        return HttpResponseRedirect('/list_task')
        
def list_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})
        
def complete_tasks(request):
    if request.method == "POST":
        id = request.POST.get("id")
        task = Task.objects.get(id=id)
        task.complete()
        task.save()
        return HttpResponseRedirect("/list_task")

