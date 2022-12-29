from django.urls import path

from spotipy_app_dev.app.views import Index, Info

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('info/', Info.as_view(), name='info'),
]