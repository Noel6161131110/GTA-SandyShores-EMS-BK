from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.id 


