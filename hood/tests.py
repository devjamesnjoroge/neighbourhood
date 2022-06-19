from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.

class AdminTest(TestCase):
    def setUp(self):
        self.admin = Admin.objects.create(username='testuser', email = 'test@gmail.com', password='12345', confirm_password='12345')

    def test_instance(self):
        self.assertTrue(isinstance(self.admin, Admin))

    def test_save_admin(self):
        self.admin.save_admin()
        self.assertTrue(isinstance(self.admin, Admin))

class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.admin = Admin.objects.create(username='testuser', email = 'test@gmail.com', password='12345', confirm_password='12345')
        self.neighbourhood = Neighbourhood.objects.create(name='test', location='test', occupants=0, admin=self.admin)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_delete_neighbourhood(self):
        self.neighbourhood.delete_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_find_neighbourhood(self):
        self.neighbourhood.find_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_update_neighbourhood(self):
        self.neighbourhood.update_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_search_neighbourhood(self):
        self.neighbourhood.search_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))