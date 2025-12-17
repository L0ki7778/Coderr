from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationView,
    LoginView,
    ProfileRetrieveUpdateView,
    ProfileTypeListView,
)

list_profile_patterns = [
    path("business/", ProfileTypeListView.as_view(profile_type="business")),
    path("customer/", ProfileTypeListView.as_view(profile_type="customer")),
]
urlpatterns = [
    path("registration/", RegistrationView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/<int:pk>/", ProfileRetrieveUpdateView.as_view()),
    path(
        "profiles/",
        include(list_profile_patterns),
    ),
]
