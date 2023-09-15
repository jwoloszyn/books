from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Ksiazka, Gatunek_literacki, Ocena, Pisarz
# Register your models here.

# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
    fields = ["okladka", "tytul", "autor", "rok_wydania", "wydawnictwo", "gatunek", "opis"]
    #list_display = ("tytul", "autor")
    search_fields = ("tytul", "opis", "autor", "wydawnictwo")

@admin.register(Pisarz)
class PisarzAdmin(admin.ModelAdmin):
    fields = ["autor", "biogram", "dzielo", "zdjecie"]
    search_fields = ("autor", "dzielo")


admin.site.register(Gatunek_literacki)
admin.site.register(Ocena)
#admin.site.register(Pisarz)
