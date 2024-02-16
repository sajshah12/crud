from django.urls  import path 
from student import views



urlpatterns = [
    path('<int>/',views.delete,home='delete'),
]
