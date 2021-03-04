from django.shortcuts import get_object_or_404, redirect

from infosite.models import HomeCarouselPhoto

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


class HomeCarouselPhotoListView(ListView):
    template_name = 'portal/components/home.html'
    model = HomeCarouselPhoto
    paginate_by = 4

    def get_queryset(self):
        return HomeCarouselPhoto.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class HomeView(TemplateView):
    template_name = 'portal/components/home.html'


class AboutView(TemplateView):
    template_name = 'portal/components/about.html'

