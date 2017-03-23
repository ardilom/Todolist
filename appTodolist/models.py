from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    
    name = models.CharField(max_length=20)
    status = models.BooleanField(default = False)
    
    def isFinished(self):
        return self.status
        
    def complete(self):
        self.status = True
    