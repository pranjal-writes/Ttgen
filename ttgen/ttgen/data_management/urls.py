from django.urls import path
from. import views

urlpatterns = [
    path('', views.dataManagement, name='data'),
    path('course/', views.addCourse, name='course'),
    path('professor/', views.addProfessor, name='professor'),
    path('days-time/', views.daysTime, name='days-time'),
    path('rooms/', views.rooms, name='rooms'),
]