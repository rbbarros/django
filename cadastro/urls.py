from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('home/', views.pagina_home, name='home')
]