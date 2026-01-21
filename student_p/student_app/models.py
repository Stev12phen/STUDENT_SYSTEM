from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    image= models.ImageField(upload_to='images/')
    email= models.EmailField()
    age= models.IntegerField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Department(models.Model):
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=100)
    head_of_department= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Program(models.Model):
    name= models.CharField(max_length=50)
    duration= models.IntegerField(help_text="Duration in years")
    department= models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Lecture(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=15)
    image= models.ImageField(upload_to='images/')
    email= models.EmailField()
    department= models.ForeignKey(Department, on_delete=models.SET_NULL, null= True)
    def __str__(self):
        return self.name
    

