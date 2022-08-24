from django.urls import path
from . import views

app_name = 'networks'

urlpatterns = [
    path('', views.NetworkListView.as_view(), name='all'),
    path('networks/<int:pk>/detail', views.NetworkDetailView.as_view(), name='network_detail'),
    path('networks/create/', views.NetworkCreateView.as_view(), name='network_create'),
    path('networks/<int:pk>/update/', views.NetworkUpdateView.as_view(), name='network_update'),
    path('networks/<int:pk>/delete/', views.NetworkDeleteView.as_view(), name='network_delete'),
]