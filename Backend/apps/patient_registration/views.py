from django.shortcuts import render
from .forms import PatientForm
import json

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = {
                "resourceType": "Patient",
                "id": form.cleaned_data['identifier'],
                "identifier": [{"use": "official", "system": "http://hospital.example.org/patients", "value": form.cleaned_data['identifier']}],
                "name": [{"use": "official", "family": form.cleaned_data['family_name'], "given": [form.cleaned_data['given_name']]}],
                "gender": form.cleaned_data['gender'],
                "birthDate": form.cleaned_data['birth_date'].strftime('%Y-%m-%d'),
                "telecom": [
                    {"system": "phone", "value": form.cleaned_data['phone'], "use": "mobile"},
                    {"system": "email", "value": form.cleaned_data['email'], "use": "home"}
                ],
                "address": [{"use": "home", "line": [form.cleaned_data['address']], "city": "Unknown", "state": "Unknown", "postalCode": "0000", "country": "Unknown"}],
            }
            # Here you could save patient data to a database or process it as required.
            return render(request, 'patient_registration/success.html', {'patient': json.dumps(patient_data, indent=4)})
    else:
        form = PatientForm()
    return render(request, 'patient_registration/register.html', {'form': form})
