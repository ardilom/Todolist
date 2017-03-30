from django.test import TestCase, Client
from appTodolist.models import *
import json

# Create your tests here.

class TodoTest (TestCase):
    
    def test_empty(self):
        #arrange
        #act
        #assert
        self.assertEquals(0, Task.objects.all().count())
        
    def test_add_task(self):
        #arrange
        t = Task.objects.create(name="Task 1")
        #act
        #assert
        self.assertEquals(1, Task.objects.all().count())

    def test_list_tasks(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        tasks = Task.objects.all()
        #assert
        self.assertEquals([t1, t2, t3], list(Task.objects.all()))
    
    def test_pending_task(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        #act
        #assert
        self.assertFalse(t1.isFinished()) 
    
    def test_done_task(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        #act
        t1.complete()
        #assert
        self.assertTrue(t1.isFinished())
        
    def test_post_task(self):
        #arrange
        client = Client()
        #act
        response = client.post("/task", {"name":"tarea_1"})
        count = Task.objects.all().count()
        #assert
        self.assertEqual(200,response.status_code)
        self.assertEqual(1, count)
        
    def test_get_list_tasks(self):
        #arrange
        client = Client()
        #act
        client.post("/task", {"name":"tarea_1"})
        client.post("/task", {"name":"tarea_2"})
        response = client.get("/list_task")
        #assert
        self.assertEqual(200,response.status_code)
        #tasks = Task.objects.all()
        self.assertEquals("tarea_1-tarea_2", response.content)
        
    def test_finish_tasks(self):
        #arrange
        client = Client()
        #act
        client.post("/task", {"name":"tarea_1"})
        response = client.post("/complete_task", {"name":"tarea_1"})
        #assert
        self.assertEqual(200,response.status_code)
        task = list(Task.objects.filter(name="tarea_1"))[0]
        self.assertTrue(task.isFinished())