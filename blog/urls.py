from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add', views.add, name="add_new_project"),
    path('delete', views.delete, name='delete'),
    #path('change_up',views.change_up, name='change_up'),
    #path('change_down',views.change_down, name='change_down'),
    path('change',views.change, name='change'),
    path("", views.home, name="homepage"),
    path("view", views.view, name="viewer"),
    path("show", views.show, name="show"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
