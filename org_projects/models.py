from django.db import models
from department_mng.models import Department
from employee_mng.models import Employee 
class Projects(models.Model):
    name = models.CharField(max_length=100)
    project_lead = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, default=1)
    description = models.TextField()
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Pending')
    dep_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.id