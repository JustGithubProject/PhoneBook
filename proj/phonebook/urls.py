from django.urls import path
from .views import HomePageView, AddPhoneFormView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("add/", AddPhoneFormView.as_view(), name="add"),
]