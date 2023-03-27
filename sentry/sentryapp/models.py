from django.db import models

# Create your models here.

class UsageMonitor(models.Model):
    pid = models.IntegerField()
    name = models.TextField()
    snap_time = models.DateTimeField(auto_now=True)
    memory = models.TextField()
    command = models.TextField()
    cpu = models.TextField()
    username = models.TextField()


    def __str__(self):
        return str(self.pid)
    
    