
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Network



class NetworkBaseView(View):
    model = Network
    fields = '__all__'
    success_url = reverse_lazy('networks:all')

class NetworkListView(NetworkBaseView, ListView):
    """View to list all networks.
    Use the 'network_list' variable in the template
    to access all Network objects"""

class NetworkDetailView(NetworkBaseView, DetailView):
    """View to list the details from one network.
    Use the 'network' variable in the template to access
    the specific network here and in the Views below"""

class NetworkCreateView(NetworkBaseView,CreateView):
    """View to create a new network"""


class NetworkUpdateView(NetworkBaseView, UpdateView):
    """View to update a network"""

class NetworkDeleteView(NetworkBaseView, DeleteView):
    """View to delete a network"""
# Create your views here.
