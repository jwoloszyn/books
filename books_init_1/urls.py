from django.urls import path
from books_init_1.views import wszystkie_ksiazki, nowa, edytuj, usun, pozycja, pisarz, nowy_pisarz
urlpatterns = [
    path('wszystkie/', wszystkie_ksiazki, name="wszystkie_ksiazki"),
    path('nowa/', nowa, name="nowa"),
    path('edytuj/<int:id>/', edytuj, name="edytuj"),
    path('usun/<int:id>/', usun, name="usun"),
    path('pozycja/<int:id>/', pozycja, name="pozycja"),
    path('pisarz/<int:id>/', pisarz, name="pisarz"),
    path('nowy-pisarz/', nowy_pisarz, name="nowy")
]
