from django.urls import path
from .views import Manager
app_name = 'apps.manager'

urlpatterns = [
    path('', Manager , name="index")
]