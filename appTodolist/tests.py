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
        self.assertEqual(302 ,response.status_code)
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
        self.assertIn('tarea_1',response.content)
        self.assertIn('tarea_2',response.content)
        self.assertIn('incomplete',response.content)
        self.assertIn('Editar',response.content)
        self.assertIn('Completar',response.content)
        
    def test_finish_tasks(self):
        #arrange
        client = Client()
        #act
        client.post("/task", {"name":"tarea_1"})
        response = client.post("/complete_task", {"id": 1, "action_type": "Completar"})
        #assert
        self.assertEqual(302,response.status_code)
        task = Task.objects.get(id=1)
        self.assertTrue(task.isFinished())
        
    def test_edit_task(self):
        # arrange
        client = Client()
        task = Task(name='Tarea para que se va a editar')
        task.save()
        # act
        response = client.put("/task", json.dumps({'id': 1 , 'name':'Nuevo nombre del task'}))
        # assert
        self.assertEquals(302, response.status_code)
        task = Task.objects.get(id=1)
        self.assertEquals("Nuevo nombre del task", task.name)
        
#    def test_delete_task(self):
#        #arrange
#        client = Client()
#        task = Task(name='Delete task')
#        task.save()
#        #act
#        response = client.post("/delete_task", {'id': 1})
#        count = Task.objects.all().count()
#        #assert
#        self.assertEquals(200, response.status_code)
#        self.assertEquals(0, count)