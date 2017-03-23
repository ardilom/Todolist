from django.test import TestCase
from appTodolist.models import *

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