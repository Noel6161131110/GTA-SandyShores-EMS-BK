from django.db import models
from employee_mng.models import Employee
class Department(models.Model):
    name = models.CharField(max_length=100)
    manager_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.id
