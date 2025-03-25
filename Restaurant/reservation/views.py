from django.shortcuts import render, redirect
from .forms import ReservationForm
from datetime import date, time, datetime
from .models import Reservation

def reserver_table(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Convertir les objets date et time en chaînes de caractères
            cleaned_data = form.cleaned_data
            if isinstance(cleaned_data.get('date_reservation'), date):
                cleaned_data['date_reservation'] = cleaned_data['date_reservation'].isoformat()
            if isinstance(cleaned_data.get('heure_reservation'), time):
                cleaned_data['heure_reservation'] = cleaned_data['heure_reservation'].isoformat()
            request.session['reservation'] = cleaned_data
            return redirect('reservation:confirmation_reservation')
    else:
        form = ReservationForm()
    return render(request, 'reserver_table.html', {'form': form})

def confirmation_reservation(request):
    reservation = request.session.get('reservation')
    if not reservation:
        return redirect('reservation:reserver_table')
    
    # Reconversion des champs date_reservation et heure_reservation
    if 'date_reservation' in reservation:
        reservation['date_reservation'] = datetime.strptime(reservation['date_reservation'], "%Y-%m-%d").date()
    if 'heure_reservation' in reservation:
        reservation['heure_reservation'] = datetime.strptime(reservation['heure_reservation'], "%H:%M:%S").time()
    
    if request.method == "POST":
        # Sauvegarder la réservation dans la base de données
        Reservation.objects.create(**reservation)
        del request.session['reservation']  # Nettoyer la session
        return render(request, 'confirmation_reussie.html')
    
    return render(request, 'confirmation_reservation.html', {'reservation': reservation})
