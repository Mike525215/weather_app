from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('weatherCards/', weather_page, name='cards'),
    path('delete/', delete_card, name='delete_card'),
    path('logout/', logout_method, name='logout'),
    path('sign_up/', SignUp.as_view(), name='sign_up'),
    path('login/', Login.as_view(), name='login')
]