# urls.py
from . import views
from django.urls import path,include
#from .views import submit_form

urlpatterns = [
    path('', views.index ,name='index'),
    path('verification/',views.verification,name='verification'),
    path('adding/', views.adding, name='adding'),
    path('success/', views.success, name='success'),
    #path('submit/', views.submit_form, name='submit_form'),
   
]
