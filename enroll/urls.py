from django.urls import path, include
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='addstudent'),
    path('update_data/<int:id>/', views.update_data, name='updatedata'),
    path('delete_data/<int:id>/', views.delete_data, name='deletedata'),
]