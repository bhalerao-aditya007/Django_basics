from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.student_profile, name= 'student_profile'),
]


  