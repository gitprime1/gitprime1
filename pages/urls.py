from django.urls import path
from .views import HomePageView, AboutPageView, Basic
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("basic/", Basic.as_view(), name="basic")
]
