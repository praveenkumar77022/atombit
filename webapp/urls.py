from django.urls import path

from .views import *

urlpatterns = [
    path('',home ,name="home"),
    path('about',about ,name="about"),
    path('term-and-condition',term ,name="term"),
    path('privacy-policy',privacy ,name="privacy"),









]