from django.db import models
from django.utils.translation import gettext_lazy as _
import re

class Network(models.Model):
    title = models.CharField(error_messages={'required': _('No pool name has been entered')},
                           max_length=20)
    subnet = models.CharField(error_messages={'required': _('No subnet has been entered')},
                             max_length=20)
    forward = models.CharField(max_length=100)
    bridge_name = models.CharField(max_length=20)


    class Meta:
        verbose_name_plural = "Network"

    def __str__(self):
        return self.title

    @property
    def clean_name(self):
        title = self.cleaned_data['title']
        have_symbol = re.match('^[a-zA-Z\d._:\-]+$', title)
        if not have_symbol:
            raise models.ValidationError(_('The pool name must not contain any special characters'))
        elif len(title) > 20:
            raise models.ValidationError(_('The pool name must not exceed 20 characters'))
        return title

    def clean_subnet(self):
        subnet = self.cleaned_data['subnet']
        have_symbol = re.match('^[\d./]+$', subnet)
        if not have_symbol:
            raise models.ValidationError(_('The pool subnet must not contain any special characters'))
        elif len(subnet) > 20:
            raise models.ValidationError(_('The pool subnet must not exceed 20 characters'))
        return subnet

    def clean_bridge_name(self):
        bridge_name = self.cleaned_data['bridge_name']
        if self.cleaned_data['forward'] == 'bridge':
            have_symbol = re.match('^[a-zA-Z\d._:\-]+$', bridge_name)
            if not have_symbol:
                raise models.ValidationError(_('The pool bridge name must not contain any special characters'))
            elif len(bridge_name) > 20:
                raise models.ValidationError(_('The pool bridge name must not exceed 20 characters'))
            return bridge_name