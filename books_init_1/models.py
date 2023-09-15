from django.db import models

# Create your models here.


class Gatunek_literacki(models.Model):
    GATUNEK = {
        (0, "inne"),
        (1, "powieść"),
        (2, "kryminał"),
        (3, "przygodowa"),
        (4, "thriller"),
        (5, "obyczajowa"),
        (6, "popularno-naukowa"),
        (7, "komedia"),
        (8, "naukowa"),
        (9, "podróżnicza"),
        (10, "reportaż")
    }
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Ksiazka(models.Model):
    okladka = models.ImageField(upload_to="plakaty", null=True, blank=True)
    tytul = models.CharField(max_length=64, blank=False, null=True)
    #autor = models.ManyToManyField('Pisarz', related_name="+", default=None, unique=False)
    #autor = models.ForeignKey('Pisarz', default=None, on_delete=models.CASCADE)
    #autor = models.CharField(max_length=72, blank=False)
    #autor = models.ForeignKey("Pisarz", unique=True, on_delete=models.CASCADE)
    #autor = models.OneToOneField("Pisarz", on_delete=models.CASCADE)
    autor = models.ManyToManyField("Pisarz", blank=True)
    rok_wydania = models.PositiveSmallIntegerField(default=2000)
    wydawnictwo = models.CharField(max_length=64, blank=False)
    gatunek = models.OneToOneField(Gatunek_literacki, on_delete=models.CASCADE, null=True, blank=True)
    opis = models.TextField(default="")

    def __str__(self):
        return self.tytul

    """def __str__(self):
        return self.dane_ksiazki()

    def dane_ksiazki(self):
        return "{} ({})".format(self.tytul, self.autor)"""



class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)


class Pisarz(models.Model):
    autor = models.CharField(max_length=72, blank=False, null=True, unique=False)
    #autor = Ksiazka.autor
    #autor = models.OneToOneField(Ksiazka, on_delete=models.CASCADE)
    #autor = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, limit_choices_to={'autor':True}, related_name="+")
    biogram = models.TextField(default="", unique=False)
    #tytul = models.ManyToManyField(Ksiazka, related_name="+", unique=False)
    #dzielo = models.TextField(default="", unique=False)
    dzielo = models.ManyToManyField(Ksiazka, blank=True)
    #dzielo = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, related_name="+")
    zdjecie = models.ImageField(upload_to="zdjecia", null=True, blank=True,unique=False)

    def __str__(self):
        return self.autor

