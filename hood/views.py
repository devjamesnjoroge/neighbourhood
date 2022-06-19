from django.shortcuts import redirect, render
from django.contrib.auth.models import User as auth_User
from .models import *
from .forms import *

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


def search_hood(request):
    if request.method == 'POST':
        hood_name = request.POST['hood_name']
        all = False
        hoods = Neighbourhood.objects.filter(name__icontains=hood_name)
        if len(hoods) == 0:
            hood = 'No results found'
            results = False
        return render(request, 'search.html', {'hood': hood})

    else:
        all = True
        hoods = Neighbourhood.objects.all()
      
    return render(request, 'search.html', {'hoods': hoods, 'all': all})

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            admin = Admin.objects.create(user=request.user)
            hood.admin = admin
            hood.save()
            return redirect('/')

    else:
        form = NeighbourhoodForm()
    return render(request, 'create_hood.html', {'form': form})
