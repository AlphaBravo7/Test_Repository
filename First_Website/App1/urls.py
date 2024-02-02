from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("A", views.A, name="A"),
    path("B", views.B, name="B"),
]