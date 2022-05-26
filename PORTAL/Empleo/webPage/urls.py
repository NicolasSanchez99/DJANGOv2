from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('singup', views.singup, name= 'singup'),
    path('logout', views.logout_rq, name= 'logout'),
    path('details', views.data, name="details"),
    path('ofertas',views.ofertas, name = 'ofertas'),
    path('candidatos',views.candidatos, name = 'candidatos')

]