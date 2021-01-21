from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    name=models.CharField(max_length=50) 

    def __str__(self):
        return self.name



class Userprofile(models.Model):
    name = models.CharField(max_length=100)
    coverpicture = models.ImageField(upload_to='images',default=None)
    photo = models.ImageField(upload_to='images',default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    doctor_name=models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 