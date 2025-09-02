from django.shortcuts import render
from django.http import HttpResponse

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
def index(requests):
    return render(requests, "index.html")

def counter(requests):
    # name = request.GET("name")
    return render(requests, "counter.html")
################################################################