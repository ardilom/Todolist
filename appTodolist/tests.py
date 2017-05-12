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
        response = client.post("/tasks", {"name":"tarea_1"})
        count = Task.objects.all().count()
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEqual(1, count)
        
    def test_get_list_tasks(self):
        #arrange
        client = Client()
        #act
        client.post("/tasks", {"name":"tarea_1"})
        client.post("/tasks", {"name":"tarea_2"})
        response = client.get("/tasks")
        #assert
        self.assertEqual(200,response.status_code)
        #tasks = Task.objects.all()
        self.assertIn('tarea_1',response.content)
        self.assertIn('tarea_2',response.content)
        self.assertIn('completed',response.content)
        self.assertIn('Editar',response.content)
        self.assertIn('Completar',response.content)
        
    def test_finish_tasks(self):
        #arrange
        client = Client()
        #act
        client.post("/tasks", {"name":"tarea_1"})
        response = client.post("/tasks/1/", {"action_type": "complete"})
        #assert
        self.assertEqual(302,response.status_code)
        task = Task.objects.get(id=1)
        self.assertTrue(task.isFinished())
    
    def test_edit_task(self):
        #arrange
        client = Client()
        #act
        client.post("/tasks", {"name":"tarea_1"})
        response = client.post("/tasks/1/", {'action_type': "edit", 'editText': "tarea_editada"})
        #assert
        self.assertEqual(302,response.status_code)
        task = Task.objects.get(id=1)
        self.assertEquals("tarea_editada", task.name)
        
        
    def test_delete_task(self):
        #arrange
        client = Client()
        task = Task(name='Delete task')
        task.save()
        #act
        response = client.post("/tasks/1/", {'action_type': "delete" })
        count = Task.objects.all().count()
        #assert
        self.assertEquals(302, response.status_code)
        self.assertEquals(0, count)
        
        
    def test_priority_empty(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        #act
        #assert
        self.assertEquals(1, Task.objects.get(id=1).priority)
        
    def test_priority_threeTasks(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        #assert
        self.assertEquals(1, Task.objects.get(id=1).priority)
        self.assertEquals(2, Task.objects.get(id=2).priority)
        self.assertEquals(3, Task.objects.get(id=3).priority)

    def test_increase_priority(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        response = client.post("/tasks/3/", {'action_type': "increase_priority" })
        response2 = client.post("/tasks/3/", {'action_type': "increase_priority" })
        response3 = client.post("/tasks/2/", {'action_type': "increase_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(1, Task.objects.get(id=3).priority)
        self.assertEquals(2, Task.objects.get(id=2).priority)
        self.assertEquals(3, Task.objects.get(id=1).priority)
        
    def test_increase_priority_1_task(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        #act
        response = client.post("/tasks/1/", {'action_type': "increase_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(1, Task.objects.get(id=1).priority)
        
    def test_increase_priority_2_task(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        #act
        response = client.post("/tasks/2/", {'action_type': "increase_priority" })
        response2 = client.post("/tasks/1/", {'action_type': "increase_priority" })
        response3 = client.post("/tasks/1/", {'action_type': "increase_priority" })
        response4 = client.post("/tasks/2/", {'action_type': "increase_priority" })
        response5 = client.post("/tasks/2/", {'action_type': "increase_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(1, Task.objects.get(id=2).priority)
        self.assertEquals(2, Task.objects.get(id=1).priority)
        
    def test_increase_priority_with_deletion(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        response = client.post("/tasks/2/", {'action_type': "delete" })
        response2 = client.post("/tasks/3/", {'action_type': "increase_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(2, Task.objects.all().count())
        self.assertEquals(1, Task.objects.get(id=3).priority)
        self.assertEquals(3, Task.objects.get(id=1).priority)
        
    def test_decrease_priority_2_tasks(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        #act
        response = client.post("/tasks/1/", {'action_type': "decrease_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(1, Task.objects.get(id=2).priority)
        self.assertEquals(2, Task.objects.get(id=1).priority)
        
    def test_decrease_priority_1_task(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        #act
        response = client.post("/tasks/1/", {'action_type': "decrease_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(1, Task.objects.get(id=1).priority)
        
    def test_decrease_priority_with_deletion(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        response = client.post("/tasks/2/", {'action_type': "delete" })
        response2 = client.post("/tasks/1/", {'action_type': "decrease_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(2, Task.objects.all().count())
        self.assertEquals(1, Task.objects.get(id=3).priority)
        self.assertEquals(3, Task.objects.get(id=1).priority)
    
    def test_decrease_and_increase_priority_1(self):
        #arrange
        client = Client()
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        response = client.post("/tasks/2/", {'action_type': "decrease_priority" })
        response = client.post("/tasks/3/", {'action_type': "increase_priority" })
        #assert
        self.assertEqual(302 ,response.status_code)
        self.assertEquals(2, Task.objects.get(id=1).priority)
        self.assertEquals(3, Task.objects.get(id=2).priority)
        self.assertEquals(1, Task.objects.get(id=3).priority)