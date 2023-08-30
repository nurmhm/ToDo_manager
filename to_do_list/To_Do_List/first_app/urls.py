from django.urls import path
from . import views
urlpatterns = [
     path('', views.home, name = 'homepage'),
     path('add_to/', views.add_TODO , name = 'add_to'),
     path('show_list/', views.show_list, name = 'show_list'),
     path('complete_list/', views.com, name = 'com_list'),
     path("edit_list/<int:id>", views.edit_list, name = 'edit_list'),
     path("delete_list/<int:id>", views.delete, name = 'delete_list'),
     path("completa_list/<int:id>", views.completa, name = 'complete_list'),
   
  
 ]
 