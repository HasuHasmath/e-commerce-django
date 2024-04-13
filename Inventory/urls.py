from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomePage),
    path('about/', AboutPage),
    path('service/', ServicePage),
    path('contact/', ContactPage),

]
