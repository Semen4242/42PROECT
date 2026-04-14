from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect("/users/")
    else:
        form = UserForm()
        return render(request, "add_user.html",{"form": form})

def main(request):
    if not request.session.get("user_id"):
        return redirect("/registration")
    
    login = request.session.get("username")
    return render(request, "main.html", {"username": registration})

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(login=username)
        except User.DoesNotExist:
            return redirect("/registration")
        
        if password != user.password:
            return redirect("/registration")
        
        request.session["user_id"] = user.id
        request.session["login"] = user.login
        
        return redirect("/main")
    
    return render(request, "registration.html")

def logout(request):
    request.session.flush()
    messages.info(request, "вы вышли из системы")
    return redirect("/registration")
    

# Create your views here.
