from django.urls import path
from .views import *


urlpatterns = [
   path('',home,name='home'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('services/',services,name='services'),
   path('register/',register,name='register'),
   path('login/',login,name='login'),
   path('savedata/',savedata,name='savedata'),
   path('logindata/',logindata,name='logindata'),
   path("query/",query,name="query"),
   path('showdata/<str:pk>',showdata,name='showdata'),
   path('delete/<int:pk>',delete,name='delete'),
   path('edit/<int:pk>',edit,name='edit'),
   path('update/<int:pk>',update,name='update'),
   path('search/<str:pk>',search,name='search')

  
]