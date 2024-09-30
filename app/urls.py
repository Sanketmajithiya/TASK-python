from django.urls import path
from  .views import *

urlpatterns = [
   path("", insert_Data, name="insertpage"),
   path("Insert/",InsertData,name="insert"), 
   path('showpage/',showpage,name="showpage"),
   path('edit/<int:pk>/',edit_page, name='editpage'),
   path('Update<int:pk>', UpdateData ,name="Update"),
   path('Delete/<int:pk>',DeleteData,name="Delete")

#    path('edit/<int:pk>/',Editpage, name='editpage'),
   
#  path('editpage/<int:pk>/', Editpage, name="editpage")
]

#name se view ko call karate hai isko  html page me {% url 'insert'%}