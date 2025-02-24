from django import forms

class CreateNewRequest(forms.Form):
    asunto = forms.CharField(label="Asunto", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    cliente = forms.CharField(label="Cliente", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs={'class': 'form-control col-md-6', 'type': 'date'}), required=False)
    hora = forms.TimeField(label="Hora", widget=forms.TimeInput(attrs={'class': 'form-control col-md-6', 'type': 'time'}), required=False)
    done = forms.BooleanField(label="Listo", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input large-checkbox col-md-6'}))