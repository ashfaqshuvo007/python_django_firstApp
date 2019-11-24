from django.urls import path
from dj_vscode import views

urlpatterns = [
    path("", views.home, name="home"),
]