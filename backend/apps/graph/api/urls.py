from django.urls import path
from .views import *

app_name = 'graph'

urlpatterns = [
    path(
        'route-between-<int:prof_edu_id_1>-<int:prof_edu_id_2>/',
        get_builded_route_AB, name='route_between'
    ),
    path(
        'route-by-<int:prof_edu_id_1>/',
        get_builded_route_A, name='route_by'
    ),
    path(
        'route-to-<int:prof_edu_id_2>/',
        get_builded_route_B, name='route_to'
    ),   
]