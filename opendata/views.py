from django.shortcuts import get_object_or_404, redirect

from accounts.models import LocalGovUnit
from opendata.models import LocalGovernmentChallenge

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


class LocalGovernmentUnitListView(ListView):
    model = LocalGovUnit
    template_name = 'opendata.html'

    def get_queryset(self):
        return LocalGovUnit.objects.order_by('user__is_active')


class LocalGovernmentUnitDetailView(DetailView):
    model = LocalGovUnit
    template_name = 'local_government_unit_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(LocalGovernmentUnitDetailView, self).get_context_data(**kwargs)
        context['lgu_challenges'] = LocalGovernmentChallenge.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')
        return context


class LocalGovernmentChallengeListView(ListView):
    model = LocalGovernmentChallenge
    template_name = 'local_government_unit_challenge_list_view.html'

    def get_queryset(self):
        return LocalGovernmentChallenge.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
