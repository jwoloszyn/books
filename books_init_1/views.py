from django.shortcuts import render, get_object_or_404, redirect
from .models import Ksiazka, Gatunek_literacki, Ocena, Pisarz
from .forms import FormKsiazka, FormGatunek, FormOcena, FormPisarz
from django.contrib.auth.decorators import login_required
#from rest_framework import viewsets
from django.contrib.auth.models import User
#from .serializers import UserSerializer, FilmSerializer

# Create your views here.
def wszystkie_ksiazki(request):
    wszystkie = Ksiazka.objects.all()
    return render(request, 'ksiazki.html', {'ksiazki': wszystkie})

@login_required
def nowa(request):
    form_ksiazka = FormKsiazka(request.POST or None, request.FILES or None)
    form_gatunek = FormGatunek(request.POST or None)
    if all((form_ksiazka.is_valid(), form_gatunek.is_valid())):
        ksiazka = form_ksiazka.save(commit=False)
        gatunek = form_gatunek.save()
        ksiazka.gatunek = gatunek
        ksiazka.save()
        return redirect(wszystkie_ksiazki)
    return render(request, 'ksiazka_form.html', {'form': form_ksiazka, 'form_gatunek': form_gatunek, 'oceny': None, 'form_ocena': None, 'nowa': True})


@login_required
def edytuj(request, id):
    ksiazka = get_object_or_404(Ksiazka, pk=id)
    oceny = Ocena.objects.filter(ksiazka=ksiazka)
    try:
        gatunek = Gatunek_literacki.objects.get(ksiazka=ksiazka.id)
    except Gatunek_literacki.DoesNotExist:
        gatunek = None
    form_ksiazka = FormKsiazka(request.POST or None, request.FILES or None, instance=ksiazka)
    form_gatunek = FormGatunek(request.POST or None, instance=gatunek)
    form_ocena = FormOcena(None)


    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.ksiazka = ksiazka
            ocena.save()
    if all((form_ksiazka.is_valid(), form_gatunek.is_valid())):
        ksiazka = form_ksiazka.save(commit=False)
        gatunek = form_gatunek.save()
        ksiazka.gatunek = gatunek
        ksiazka.save()
        return redirect(wszystkie_ksiazki)
    return render(request, 'ksiazka_form.html', {'form':  form_ksiazka, 'form_gatunek': form_gatunek, 'oceny': oceny, 'now': True})


@login_required
def usun(request, id):
    ksiazka = get_object_or_404(Ksiazka, pk=id)
    if request.method=="POST":
        ksiazka.delete()
        return redirect(wszystkie_ksiazki)

    return render(request, 'potwierdz.html', {'ksiazka': ksiazka})


def pozycja(request, id):
    ksiazka = get_object_or_404(Ksiazka, pk=id)
    return render(request, 'pozycja.html', {'ksiazka': ksiazka})

@login_required
def pisarz(request, id):
    #ksiazka = get_object_or_404(Ksiazka, pk=id)
    pisarz = get_object_or_404(Pisarz, pk=id)

    return render(request, 'pisarz.html', {'pisarz': pisarz})

#ksiazka': ksiazka

@login_required
def nowy_pisarz(request):
    form_pisarz = FormPisarz(request.POST or None, request.FILES or None)
    if form_pisarz.is_valid():
        pisarz = form_pisarz.save(commit=False)
        pisarz.save()
        return redirect(wszystkie_ksiazki)
    return render(request, 'pisarz_form.html', {'form_pisarz': form_pisarz, 'nowy': True})


def pisarz_edytuj():
    pass






