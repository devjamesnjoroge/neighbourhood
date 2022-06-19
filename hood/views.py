from django.shortcuts import redirect, render
from django.contrib.auth.models import User as auth_User
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
        hood_user = User.objects.create(user=user)
        hood_user.save()
        return redirect('/auth/login/')
    return render(request, 'authentication/register.html')


@login_required(login_url='/auth/login/')
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

@login_required(login_url='/auth/login/')
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            if Admin.objects.filter(user=request.user).exists():
                admin = Admin.objects.get(user=request.user)
            else:
                admin = Admin.objects.create(user=request.user)
            hood.admin = admin
            hood.save()
            return redirect('/')

    else:
        form = NeighbourhoodForm()
    return render(request, 'create_hood.html', {'form': form})

@login_required(login_url='/auth/login/')
def hood_profile(request, hood_id):
    hood = Neighbourhood.find_neighbourhood(hood_id)
    if User.objects.filter( user=request.user, neighbourhood=hood).exists():
        status = 'Member'
    else:
        status = 'Not Member'
    return render(request, 'hood_profile.html', {'hood': hood, 'status': status})

@login_required(login_url='/auth/login/')
def join_hood(request, hood_id):
   
    hood = Neighbourhood.find_neighbourhood(hood_id)
    user = User.objects.get(user=request.user)
    user.neighbourhood = hood
    user.save()
    return redirect('/neighbourhoods/')