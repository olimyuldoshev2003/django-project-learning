from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from .models import Someone
# Create your views here.

# no html
############################################################
# def index(request):
#     return HttpResponse("<h1>Hello man, how are you?</h1>")
############################################################

# 1.
#############################################################
# def index(request):
#     fullName = "Olim Yuldoshev"
#     return render(request, "index.html", {"fullName": fullName})
#############################################################

# 2.   
##############################################################
# def index(request):
#     user = {
#         "name": "Olim",
#         "surname": "Yuldoshev",
#         "age": 21
#     }
#     return render(request, "index.html", user)
###############################################################

# 3. 
###############################################################
# def index(request):
#     return render(request, "index.html")

# def counter(request):
#     name = request.GET['name']
#     wordLength = len(name.split())
#     return render(request, 'counter.html', {"length": wordLength})
################################################################

# 4.
################################################################
# def index(request):
#     return render(request, "index.html")

# def counter(request):
#     text = request.POST['text']
#     return render(request, 'counter.html', {"text": text})
#################################################################

# 5.
#################################################################
# def index(request):
#     return render(request, "index.html")
#################################################################

# 6.
#################################################################
# def index(request):
    # person
    # person1 = Someone()
    # person1.id = 0
    # person1.fullName = "Olim Yuldoshev"
    # person1.age = 21

    # people
    # person1 = Someone()
    # person1.id = 0
    # person1.fullName = "Olim Yuldoshev"
    # person1.age = 21
    # person1.is_old = False

    # person2 = Someone()
    # person2.id = 1
    # person2.fullName = "Cristiano Ronaldo"
    # person2.age = 40
    # person2.is_old = True

    # person3 = Someone()
    # person3.id = 2
    # person3.fullName = "Pathman Senathirajah"
    # person3.age = 50
    # person3.is_old = True

    # person4 = Someone()
    # person4.id = 3
    # person4.fullName = "Saidmurod Davlatov"
    # person4.age = 40
    # person4.is_old = True

    # people = [person1, person2, person3, person4]
    
    #person 
    # return render(request, "index.html", {"person": person1})

    #people 
    # return render(request, "index.html", {"people": people})
#################################################################

# 7.
#################################################################
# def index(request):
#     people = Someone.objects.all()
#     return render(request, "index.html", {"people": people})
#################################################################

# 8.
#################################################################
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmPassword"]
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "This email exists")
                return redirect("signup")
            elif User.objects.filter(username = username).exists():
                messages.info(request, "This user exists")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username = username, 
                    email = email, 
                    password = password
                )
                user.save()
                return redirect("signin")
        else:
            messages.info(request, "Password isn't the same with confirm password")
            redirect("signup")
    else:
        return render (request, "signup.html")
    
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials invalid")
            return redirect("signin")
    return render(request, "signin.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

#################################################################

# 9. Dynamic Routing
#################################################################
def post(request, pk):
    return render(request, "post.html", {"pk": pk})

def counter(request):
    posts = [
        "Post 1",
        "Post 2",
        "Post 3",
        "Post 4",
        "Post 5", 1, 2, 3, 4, 5
    ]
    return render(request, "counter.html", )
#################################################################

