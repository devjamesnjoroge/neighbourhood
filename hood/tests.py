from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.

class AdminTest(TestCase):
    def setUp(self):
        self.admin = Admin.objects.create(username='testuser', email = 'test@gmail.com', password='12345', confirm_password='12345', phone='0712345678')

    def test_instance(self):
        self.assertTrue(isinstance(self.admin, Admin))