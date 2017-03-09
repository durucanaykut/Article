from django import forms

from .models import Reporter

class reporterform(forms.ModelForm):

    class Meta:
        model = Reporter
        fields = ('profession','first_name',
                  'last_name','email')
