from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_joining = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    assigned_role = models.CharField(max_length=100,default='employee',blank=True)
    current_project = models.IntegerField(null=True,default=0)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,default='Prefer not to say')
    current_department = models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.id
    


    

    
    