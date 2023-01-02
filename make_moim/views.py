from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from make_moim.models import Make_Moim

# Create your views here.
class Make_Moim(LoginRequiredMixin, CreateView):
    model = Make_Moim
    fields = ['name','commend','imgfile','location','max_people']