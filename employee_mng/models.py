from django.db import models
from department_mng.models import Department
from org_projects.models import Projects

class Designation(models.Model):
    designation_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id
    
    
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_joining = models.CharField(max_length=100)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    assigned_role = models.CharField(max_length=100,default='Employee')
    current_project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,default='Prefer not to say')
    current_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.id
    
    

    
    