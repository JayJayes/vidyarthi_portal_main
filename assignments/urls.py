from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.teacher_assignment_upload, name='teacher_assignment_upload'),
]
