from email.policy import default
from django.db import models
from django.contrib.auth.models import User as auth_User
from cloudinary.models import CloudinaryField
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(auth_User, on_delete=models.CASCADE, default=None)

    def save_admin(self):
        self.save()


    def __str__(self):
        return self.user.username
    

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, unique=True)
    occupants = models.IntegerField()
    hood_image = CloudinaryField('image', default='')
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    
    def find_neighbourhood(id):
        return Neighbourhood.objects.get(id=id)

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
    user = models.OneToOneField(auth_User, on_delete=models.CASCADE, default=None)
    neighbourhood = models.OneToOneField(Neighbourhood, on_delete=models.CASCADE, default='', null=True, blank=True)

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def delete_neighbourhood(self):
        self.neighbourhood.delete()

    def __str__(self):
        return self.user.username


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