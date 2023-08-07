from django.urls import path 
import with_medicine_userapp.views

urlpatterns = [
    path('signup/', with_medicine_userapp.views.signup, name='signup'),
    path('login/', with_medicine_userapp.views.login, name='login'),
    path('logout/', with_medicine_userapp.views.logout, name='logout'),
    
]
