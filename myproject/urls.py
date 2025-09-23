from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("counter", views.counter, name="counter"),
    path("signup", views.signup, name = "signup"),
    path("signin", views.signin, name = "signin"),
    path("logout", views.logout, name = "logout"),
    
    # 9. Dynamic Routing
    path("post/<str:pk>", views.post, name="post"),
]