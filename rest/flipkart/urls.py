from django.urls import path
from .views import flipkart
urlpatterns  = [
    path('home/',flipkart.as_view())
]