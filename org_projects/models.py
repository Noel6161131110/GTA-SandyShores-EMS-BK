from django.db import models

class Projects(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id