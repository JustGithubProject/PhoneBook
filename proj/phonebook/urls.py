from django.urls import path
from .views import HomePageView, AddPhoneFormView, DeletePhoneView, Search

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("add/", AddPhoneFormView.as_view(), name="add"),
    path("delete/<int:pk>", DeletePhoneView.as_view(), name="delete"),
    path('search/', Search.as_view(), name="search")
]