from django.urls import path
from blog import views


urlpatterns = [
    path('add', views.add, name="add_new_project"),
    path('delete', views.delete, name='delete'),
    #path('change_up',views.change_up, name='change_up'),
    #path('change_down',views.change_down, name='change_down'),
    path('change',views.change, name='change'),
]
