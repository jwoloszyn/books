from django.forms import ModelForm
from .models import Ksiazka, Gatunek_literacki, Ocena, Pisarz

class FormKsiazka(ModelForm):
    class Meta:
        model = Ksiazka
        fields = ["okladka", "tytul", "autor", "rok_wydania", "wydawnictwo", "opis"]

class FormGatunek(ModelForm):
    class Meta:
        model = Gatunek_literacki
        fields = ["gatunek"]


class FormOcena(ModelForm):
    class Meta:
        model = Ocena
        fields = ["gwiazdki", "recenzja"]

class FormPisarz(ModelForm):
    class Meta:
        model = Pisarz
        fields = ["zdjecie", "autor", "biogram", "dzielo"]