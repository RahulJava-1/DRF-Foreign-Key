from django.db import models

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.CharField(max_length=10)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name