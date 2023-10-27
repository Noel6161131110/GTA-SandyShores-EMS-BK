from django.db import models

class Department(models.Model):
    dep_id = models.IntegerField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager_id = models.IntegerField()
    
    def __str__(self):
        return self.id
