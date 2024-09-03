from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import DivingRecord


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def pb_list(request):
    DivingRecords = DivingRecord.objects.all()  # Získá všechny produkty z databáze
    return render(request, 'pb.html', {'pbs': DivingRecords})


@login_required
def profile(request):
    DivingRecords_filter = DivingRecord.objects.filter(user=request.user)  # Získá všechny produkty z databáze pro usera
    return render(request, 'profile.html', {'pbsf': DivingRecords_filter})