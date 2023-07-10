
from django.urls import path
from .views import home, contact, about_us, servicios

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about-us/', about_us, name="about_us"),
    path('servicios/', servicios, name="servicios"),
]

