from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['asunto', 'cliente', 'descripcion', 'fecha_ocurrencia', 'done']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control col-md-6 mb-4'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control col-md-6 mb-4'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control mb-4'}),
            'fecha_ocurrencia': forms.DateTimeInput(attrs={'class': 'form-control mb-4', 'type': 'datetime-local'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input large-checkbox col-md-6 mb-4'}),
        }
        labels = {
            'asunto': 'Asunto',
            'cliente': 'Cliente',
            'descripcion': 'Descripción',
            'fecha_ocurrencia': 'Fecha de ocurrencia',
            'done': '¿Está resuelto?',
        }
