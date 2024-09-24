from django.urls import path
from .views import *


urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('add/',add,name="add"),
    path('delete/<int:student_id>/',delete,name='delete'),
    path('edit/<int:student_id>/',edit,name='edit'),
]
