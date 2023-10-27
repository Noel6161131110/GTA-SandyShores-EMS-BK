from django.db import models
from employee_mng.models import Employee
from department_mng.models import Department

class Manager(models.Model):
    manager_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return self.id