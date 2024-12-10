from django import forms
from .models import ConsultationRequest

class ConsultationRequestForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['name', 'email', 'contact_number', 'date']
        widgets = {
             'date': forms.DateInput(attrs={'type': 'date'}),
        #     'time_slot': forms.Select(),
         }