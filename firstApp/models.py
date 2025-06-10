from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    enrollment_date = models.DateField(auto_now_add=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name = 'students')

    def __str__(self): #This is two underscore not one
        return f"{self.first_name} {self.last_name}"