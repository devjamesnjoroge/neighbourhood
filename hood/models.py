from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=50, default='', unique=True)
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    confirm_password = models.CharField(max_length=100, default=password)

    def save_admin(self):
        self.save()


    def __str__(self):
        return self.username
    

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, unique=True)
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

    @classmethod
    def search_neighbourhood(self, hood_name):
        return Neighbourhood.objects.filter(name__icontains=hood_name)


    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, default=password)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, default='', null=True, blank=True)

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.name


class Business(models.Model):
        business_name = models.CharField(max_length=50)
        business_email = models.EmailField(max_length=100)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

        def save_business(self):
            self.save()

        def delete_business(self):
            self.delete()

        def find_business(self):
            return Business.objects.filter(id=self.id)

        def update_business(self):
            self.save()

        @classmethod
        def search_business(self, search_term):
            return Business.objects.filter(business_name__icontains=search_term)

        def __str__(self):
            return self.business_name