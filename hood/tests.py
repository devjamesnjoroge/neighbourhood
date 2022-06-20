from django.test import TestCase
from django.contrib.auth.models import User as auth_User
from .models import *

# Create your tests here.

class AdminTest(TestCase):
    def setUp(self):
        self.user = auth_User.objects.create(username='test', password='test', email='testuser@gmail.com')
        self.admin = Admin.objects.create(user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.admin, Admin))

    def test_save_admin(self):
        self.admin.save_admin()
        self.assertTrue(len(Admin.objects.all()) > 0)

class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.user = auth_User.objects.create(username='test', password='test', email='testuser@gmail.com')
        self.admin = Admin.objects.create(user=self.user)
        self.neighbourhood = Neighbourhood.objects.create(name='test', location='test', occupants=0, admin=self.admin)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all())>0)

    def test_delete_neighbourhood(self):
        self.neighbourhood.delete_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all())==0)

    def test_find_neighbourhood(self):
        self.neighbourhood.find_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_update_neighbourhood(self):
        self.neighbourhood.update_neighbourhood()
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_search_neighbourhood(self, hood_name = 'test'):
        search_results = self.neighbourhood.search_neighbourhood(hood_name)
        self.assertTrue(len(search_results)>0)

class BusinessTest(TestCase):
    def setUp(self):
        self.user = auth_User.objects.create(username='test', password='test', email='testuser@gmail.com')
        self.admin = Admin.objects.create(user=self.user)
        self.neighbourhood = Neighbourhood.objects.create(name='test', location='test', occupants=0, admin=self.admin)
        self.user = User.objects.create(user=self.user, neighbourhood=self.neighbourhood)
        self.business = Business.objects.create(business_name='test', business_email = 'business@gmail.com', user = self.user, neighbourhood=self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        self.assertTrue(len(Business.objects.all())>0)

    def test_delete_business(self):
        self.business.delete_business()
        self.assertTrue(len(Business.objects.all())==0)

    def test_find_business(self):
        self.business.find_business()
        self.assertTrue(isinstance(self.business, Business))

    def test_update_business(self):
        self.business.update_business()
        self.assertTrue(isinstance(self.business, Business))

    def test_search_business(self, search_term = 'test'):
        search_results = self.business.search_business(search_term)
        self.assertTrue(len(search_results)>0)