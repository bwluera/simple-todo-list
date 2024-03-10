from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    print(request)
    form = TaskForm()
    context = {"tasks" : Task.objects.filter(user=request.user), "taskform" : form}
    return render(request, "home.html", context)

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task()
            new_task.user = request.user
            new_task.title = form.cleaned_data['title']
            new_task.description = form.cleaned_data["description"]
            new_task.date_created = timezone.now()
            new_task.completed = False
            new_task.save()

    return redirect("/home")

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("/home")

def update_task(request, id, checked):
    task = Task.objects.get(pk=id)
    print(checked)
    if checked.lower() == "false":
        task.completed = False
    else:
        task.completed = True

    task.save()
    return redirect("/home")

def register(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/home')
    else:  
        form = UserCreationForm()  
    auth_form = AuthenticationForm()
    context = {  
        'form':form , 'login': auth_form 
    }  
    return render(request, 'register.html', context)  

def logout_view(request):
    logout(request)
    return redirect('/register')
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                )
            if user:
                login(request, user)
                return redirect('/home')
    return redirect('/register')