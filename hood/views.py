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
    businesses = Business.objects.filter(neighbourhood=hood)
    return render(request, 'hood_profile.html', {'hood': hood, 'status': status, 'businesses': businesses})

@login_required(login_url='/auth/login/')
def join_hood(request, hood_id):
   
    hood = Neighbourhood.find_neighbourhood(hood_id)
    user = User.objects.get(user=request.user)
    if user.neighbourhood is not None:
        return render(request, 'error/already_member.html')
    else:
        user.neighbourhood = hood
        user.save()
    return redirect('/neighbourhoods/' + str(hood_id))

@login_required(login_url='/auth/login/')
def leave_hood(request, hood_id):
    hood = Neighbourhood.find_neighbourhood(hood_id)
    user = User.objects.get(user=request.user)
    user.neighbourhood = None
    user.save()
    return redirect('/neighbourhoods/' + str(hood_id))

@login_required(login_url='/auth/login/')
def create_business(request, hood_id):
    hood = Neighbourhood.find_neighbourhood(hood_id)
    user = User.objects.get(user=request.user)

    if request.method == 'POST':
        if user.neighbourhood != hood:
            return render(request, 'error/403.html')
        else:
            error = False
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            user = User.objects.get(user=request.user)
            neighbourhood = user.neighbourhood
            business.user = user
            business.neighbourhood = neighbourhood
            business.save()
            return redirect('/neighbourhoods/')
    else:
        form = BusinessForm()
        error = False
    return render(request, 'create_business.html', {'form': form, 'error': error})

@login_required(login_url='/auth/login/')
def delete_business(request, hood_id, business_id):
    business = Business.objects.get(id=business_id)
    user = User.objects.get(user=request.user)
    if business.user == user:
        business.delete()
        return redirect('/neighbourhoods/' + str(hood_id))
    else:
        return render(request, 'error/403.html')

@login_required(login_url='/auth/login/')
def edit_business(request, hood_id, business_id):
    business = Business.objects.get(id=business_id)
    user = User.objects.get(user=request.user)
    if business.user == user:
        if request.method == 'POST':
            form = BusinessForm(request.POST, request.FILES, instance=business)
            if form.is_valid():
                form.save()
                return redirect('/neighbourhoods/' + str(hood_id))
        else:
            form = BusinessForm(instance=business)
        return render(request, 'edit_business.html', {'form': form})
    else:
        return render(request, 'error/403.html')