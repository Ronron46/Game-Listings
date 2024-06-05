"""
URL configuration for game_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='plateforme'),
    path('games/', views.games, name='game_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('games/add/', views.game_create, name='game_create'),
    path('games/<int:game_id>/edit/', views.game_edit, name='game_edit'),
    path('games/<int:game_id>/delete/', views.game_delete, name='game_delete'),
    path('plateformes/', views.plateformes, name='plateformes'),
    path('plateformes/<int:plateforme_id>/', views.plateforme_detail, name='plateforme_detail'),
    path('plateformes/add/', views.plateforme_add, name='plateforme_add'),
    path('plateformes/<int:plateforme_id>/delete/', views.plateforme_delete, name='plateforme_delete'),
    path('plateformes/<int:plateforme_id>/edit/', views.plateforme_edit, name='plateforme_edit')
]
