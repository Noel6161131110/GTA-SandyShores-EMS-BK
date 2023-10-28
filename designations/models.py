from django.db import models

class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True, default='employee')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.id