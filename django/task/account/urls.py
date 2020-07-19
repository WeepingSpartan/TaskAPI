from django.urls import path
from .import views

app_name="account"

urlpatterns = [
    path('signup/', views.signup ,name='signup'),
    path('login/', views.loginform ,name='login'),
    path('logout/', views.logoutopp ,name='logout'),
    path('random/', views.randomizer, name='random')    
]
