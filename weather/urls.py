from django.urls import path
from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('sign_up/', sign_up_user, name='sign_up_user'),
    path('logout/', logout_user, name='logout_user'),
    path('login/', login_user, name='login_user'),
    path('delete/<slug:city_name>/', delete_city, name='delete_city')
]