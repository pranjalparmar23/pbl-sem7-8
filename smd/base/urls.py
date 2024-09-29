from django.urls import path, include
from .views import authView, home, about, contact, services, footer

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("services/", services, name="services"),
    path("footer/", footer, name="footer"),
    path("accounts/", include("django.contrib.auth.urls")),
]