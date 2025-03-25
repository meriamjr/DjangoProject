from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views import View

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige vers la page de connexion après l'enregistrement
        return render(request, 'registration/register.html', {'form': form})

def Logout_view(request):
    logout(request)
    return redirect('/')
