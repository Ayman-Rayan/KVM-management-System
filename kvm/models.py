from django.db import models
from django.utils.translation import gettext_lazy as _
import re
from networks.models import Network



class Kvm(models.Model):
    name = models.CharField(error_messages={'required': _('No Virtual Machine name has been entered')},max_length=20)
    vcpus = models.IntegerField(error_messages={'required': _('No VCPU has been entered')})
    disk = models.IntegerField(blank=False)
    memory = models.IntegerField(error_messages={'required': _('No RAM size has been entered')})
    networks = models.ForeignKey(Network,blank=True,default='network',on_delete=models.CASCADE)
    storage = models.CharField(max_length=200, blank=False)
    iso = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000,blank=True)
    hdd_size = models.IntegerField(blank=False)
    mac = models.CharField(max_length=200,blank=True,default='52:54:00:25:fc:b8')
    kvmcreator =  models.IntegerField('kvm creator',blank=False,default=1)
    instance = models
 

    

    def clean_name(self):
        name = self.cleaned_data['name']
        have_symbol = re.match('^[a-zA-Z\d._-]+$', name)
        if not have_symbol:
            raise models.ValidationError(_('The name of the virtual machine must not contain any special characters'))
        elif len(name) > 20:
            raise models.ValidationError(_('The name of the virtual machine must not exceed 20 characters'))
        return name
    class Meta:
        verbose_name_plural = "NET"
    def __str__(self):
        return self.name
    
class Kvmm(models.Model):
    name = models.CharField(error_messages={'required': _('No Virtual Machine name has been entered')},max_length=20)
    vcpus = models.IntegerField(error_messages={'required': _('No VCPU has been entered')})
    disk = models.IntegerField(blank=False)
    memory = models.IntegerField(error_messages={'required': _('No RAM size has been entered')})
    networks = models.ForeignKey(Network,blank=True,default='network',on_delete=models.CASCADE)
    storage = models.CharField(max_length=200, blank=False)
    iso = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000,blank=True)
    hdd_size = models.IntegerField(blank=False)
    mac = models.CharField(max_length=200,blank=True,default='52:54:00:25:fc:b8')
    kvmcreator =  models.IntegerField('kvm creator',blank=False,default=1)
    instance = models
 
    
    

    def clean_name(self):
        name = self.cleaned_data['name']
        have_symbol = re.match('^[a-zA-Z\d._-]+$', name)
        if not have_symbol:
            raise models.ValidationError(_('The name of the virtual machine must not contain any special characters'))
        elif len(name) > 20:
            raise models.ValidationError(_('The name of the virtual machine must not exceed 20 characters'))
        return name
    class Meta:
        verbose_name_plural = "Kvm"
    def __str__(self):
        return self.name
