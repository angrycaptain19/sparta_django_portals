from django.shortcuts import get_object_or_404, redirect

from hackaton.models import HackatonChallenge

from django.urls import reverse_lazy
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class HackatonChallengeListView(ListView):
    model = HackatonChallenge
    template_name = 'hackaton_challenge_list_view.html'

    def get_queryset(self):
        return HackatonChallenge.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class HackatonChallengeDetailView(DetailView):
    model = HackatonChallenge
    template_name = 'hackaton_challenge_detail_view.html'
