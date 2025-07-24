from django.urls import path
from earth.views import *

urlpatterns = [
    path('index/', index, name='Home'),
    path('country/<int:pk>/', country, name='country'),
]