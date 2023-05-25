from . import views
from django.urls import path

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mrk_as_d/<int:pk>/', views.mrk_as_d, name='mrk_as_d'),
    path('mrk_as_ud/<int:pk>/', views.mrk_as_ud, name='mrk_as_ud'),

    #EDIT
    path('edit/<int:pk>/', views.edit, name='edit'),

    #DELETE
    path('delete/<int:pk>/', views.delete, name='delete'),

]
