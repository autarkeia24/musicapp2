from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('artistes/', views.get_artistes),
    path('songs/', views.get_songs),
    path('songs/<str:pk>', views.get_single_song),
    path('delete-song/<str:pk>', views.delete_song),
    path('update-song/<str:pk>', views.update_song)
]
