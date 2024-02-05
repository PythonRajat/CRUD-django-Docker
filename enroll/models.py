from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name