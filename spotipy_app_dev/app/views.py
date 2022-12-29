from django.shortcuts import render
from django.views.generic import TemplateView
from ..spotipy.base.getters import get_track_object
from ..spotipy.base.classes import Album, Artist


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['temp'] = get_track_object('spotify:track:2Sr5xgV9NxH56BVBAgVP3U')
        return context

class Info(TemplateView):
    template_name = 'info.html'