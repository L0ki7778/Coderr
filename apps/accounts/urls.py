from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView, LoginView, ProfileViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('',include(router.urls)),
]
