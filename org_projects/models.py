from django.db import models
from department_mng.models import Department

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    dep_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.id