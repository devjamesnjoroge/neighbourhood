from django.shortcuts import redirect, render
from django.contrib.auth.models import User as auth_User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = auth_User.objects.create_user(username, email, password)
        user.save()
        return redirect('/')
    return render(request, 'authentication/register.html')