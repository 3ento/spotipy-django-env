from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import PlaylistComparisonForm
from ..spotipy.base.getters import get_track_object
from ..spotipy.base.classes import Album, Artist
from ..spotipy.functions.playlists_compare import get_playlist_comparison

# class Index(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['temp'] = get_track_object('spotify:track:2Sr5xgV9NxH56BVBAgVP3U')
#         return context

class Info(TemplateView):
    template_name = 'info.html'

def playlist_comparison_view(request, pl1, pl2):
    template_name = 'index.html'

    if request.method == 'POST':
        form = PlaylistComparisonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('playlist comparison'))
        else:
            form = PlaylistComparisonForm()

    context = {
        'results': get_playlist_comparison(pl1, pl2)
    }

    return render(request, template_name, context)

