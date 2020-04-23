from django.shortcuts import redirect, render

from User_app.models import PatientForm


# Create your views here.
def home_patient(request):
    return render(request, 'Treatment/home_patient.html')

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = PatientForm()
    return render(request, 'Treatment/create_patient.html', {'form': form})

def create_treatment(request, patient_id):
    return render(request, 'Treatment/create_treatment.html')

def home_treatment(request):
    return render(request, 'Treatment/home_treatment.html')


def home_diagnosis(request):
    return render(request, 'Treatment/home_diagnosis.html')

def examination_room(request, room_id):
    return render(request, 'Treatment/examination_room.html')
