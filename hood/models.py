from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    
    def find_neighbourhood(self):
        return Neighbourhood.objects.filter(id=self.id)

    def update_neighbourhood(self):
        self.save()

    def update_occupants(self):
        self.save()


    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, default=password)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.name