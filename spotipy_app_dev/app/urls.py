from django.urls import path

from spotipy_app_dev.app.views import Index, Info, playlist_comparison_view

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('info/', Info.as_view(), name='info'),
    path('playlist-comparison/<str:pl1>+<str:pl2>', playlist_comparison_view, name='playlist comparison')
]