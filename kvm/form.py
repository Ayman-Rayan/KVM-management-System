from pyexpat import model
from django.forms import ModelForm
from .models import Kvmm

class KvmForm(ModelForm):
    class  Meta:
        model = Kvmm
        fields = '__all__'
        