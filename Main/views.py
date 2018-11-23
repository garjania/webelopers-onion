from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

user = None

# Create your views here.

def index(request):
    return render(request, "index.html",{
        "logged" : request.user.is_authenticated
    })

def sign_in(request):
    username, password = "", ""
    error = False
    if request.POST:
        username = request.POST.get("user-name")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            error = True
    return render(request, "sign_in.html",{
        "error": error
    })



def contact_us(request):
    error = False
    succ = False
    if request.POST:
        title = request.POST.get("title")
        text = request.POST.get("text")
        if len(title) != 0 and len(text) > 9 and len(text) < 251:
            succ = True
        else:
            error = True
    return render(request, "contact_us.html",{
        "error": error,
        "succ": succ
    })


def sign_up(request):
    error = False
    error2 = False
    error3 = False
    if request.POST:
        users = User.objects.filter(username=request.POST.get("user-name"))
        if users:
            error = True
        users = User.objects.filter(email=request.POST.get("email"))
        if users:
            error2 = True
        if request.POST.get("password") != request.POST.get("repeat-password"):
            error3 = True

        if error or error2 or error3:
            return render(request, "sign_up.html", {
                "logged": request.user.is_authenticated,
                "error3": error3,
                "error2": error2,
                "error": error
            })
        user = User.objects.create_user(username=request.POST.get("user-name"), email=request.POST.get("email"), password=request.POST.get("password"), first_name=request.POST.get("first-name"),last_name=request.POST.get("last-name"))

        user.save()

        return HttpResponseRedirect("/")
    return render(request, "sign_up.html",{
        "logged": request.user.is_authenticated,
        "error":False,
        "error2":False,
        "error3":False
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")

def show_prof(request):
    return render(request, "user_page.html", {
        "name": request.user.first_name,
        "lastname": request.user.last_name,
        "username": request.user.username,
        "logged": request.user.is_authenticated
    })

def edit_user(request):
    if request.POST:
        name = request.POST.get("first-name")
        last = request.POST.get("last-name")
        request.user.first_name = name
        request.user.last_name = last
        request.user.save()
        return HttpResponseRedirect("/user")
    return render(request, "edit_user.html")


