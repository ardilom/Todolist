from __future__ import unicode_literals

from django.db import models

# Create your models here.

def new_priority():
    tasks = Task.objects.all()
    if tasks.count()==0:
        return 1
    else:
        return tasks.order_by('-priority')[0].priority + 1

class Task(models.Model):
    
    name = models.CharField(max_length=20)
    status = models.BooleanField(default = False)
    priority = models.IntegerField(default=new_priority, blank=False, null=False)
    
    def isFinished(self):
        return self.status
        
    def complete(self):
        self.status = True
        
