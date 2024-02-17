from django.urls  import path 
from student import views



urlpatterns = [
    path('',views.add,name = 'add'),
    path('delete<int>/',views.delete,home='delete'),
]
