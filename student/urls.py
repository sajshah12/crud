from django.urls  import path 
from student import views



urlpatterns = [
    path('delete<int>/',views.delete,home='delete'),
]
