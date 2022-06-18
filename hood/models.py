from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.name

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