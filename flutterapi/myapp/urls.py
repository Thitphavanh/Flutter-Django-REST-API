from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('api/all-todolist/', all_todolist),

]
