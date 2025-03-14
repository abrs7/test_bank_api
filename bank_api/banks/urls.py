from django.urls import path
from .views import get_banks, get_branches, SubmitApplication

urlpatterns = [
    path('get_banks', get_banks, name='get_banks'),
    path('get_branches', get_branches, name='get_branches'),
    path('applications/submit', SubmitApplication.as_view(), name='submit_application'),
]