from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import DivingRecord
from .forms import DivingRecordForm


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

@login_required
def add_diving_record(request):
    if request.method == 'POST':
        form = DivingRecordForm(request.POST)
        if form.is_valid():
            diving_record = form.save(commit=False)
            diving_record.user = request.user
            diving_record.save()
            return redirect('profile')  # Redirect to a profile page or list of records
    else:
        form = DivingRecordForm()

    return render(request, 'add_diving_record.html', {'form': form})


@login_required
def edit_diving_record(request, record_id):
    record = get_object_or_404(DivingRecord, id=record_id, user=request.user)

    if request.method == 'POST':
        form = DivingRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Nebo na jinou stránku dle potřeby
    else:
        form = DivingRecordForm(instance=record)

    return render(request, 'edit_diving_record.html', {'form': form})