from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .models import Oferta
from .models import Candidato
from django.contrib import messages


# Create your views here.
@login_required
def data(request):

    usuario = request.user

    if request.method == "POST":
        pass

    return render(request, 'front/detalles.html', {'usuario': usuario})


def singup(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get(('password'))
            user = authenticate(username = usuario, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logeado como {usuario}")
                return redirect('home')
            else:
                messages.error(request, "No se pudo")

        else:
            messages.error(request, "No se pudo 2")
    form = AuthenticationForm()
    return render(request, "registration/LogIn.html", {"form": form})


def home(request):
    return render(request, 'front/home.html')

def ofertas(request):
    Ofertas = Oferta.objects.all()
    return render(request, 'front/Ofertas.html',{'ofertas': Ofertas})

def candidatos(request):
    candidatos= Candidato.objects.all()
    return render(request, 'front/candidatos.html',{'candidatos': candidatos})

def logout_rq(request):
    logout(request)
    messages.info(request, 'YA SALISTE')
    return redirect("home")
