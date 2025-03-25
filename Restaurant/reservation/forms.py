from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_client', 'email', 'date_reservation',
        'heure_reservation', 'nombre_personnes', 'commentaires']
        widgets = {
        'date_reservation': forms.DateInput(attrs={'type': 'date'}),
        'heure_reservation': forms.TimeInput(attrs={'type': 'time'}),
        }