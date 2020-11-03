
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from Dashboard.models import room


class LoginView (View):
    def get(self, request):
        room1 = room.objects.all()
        context = {'room1':room1}
        return render (request,'IOT/login.html',context)


class IndexView (ListView):
    model = room
    template_name = 'IOT/index.html'
    context_object_name = 'ind'
