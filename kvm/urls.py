from django.urls import path
from . import views

app_name = 'kvm'

urlpatterns = [

    path('kvm/create/', views.createKvm, name='Kvm_create'),
    path('kvm/list/', views.index, name='Kvm_index'),
    path('kvm/start/<int:id>', views.startKvm, name='Kvm_start'),
    path('kvm/delete/<int:id>', views.destroy, name='Kvm_delete'),
    path('kvm/deletePage/<int:id>', views.destroyConfirmPage, name='Kvm_delete_page'),
   
]