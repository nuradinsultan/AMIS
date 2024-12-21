# views.py

from django.shortcuts import render
from .models import Patient, PatientNote, GlassPrescription, Investigation, Consultation

def patient_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    notes = PatientNote.objects.filter(patient=patient)
    prescriptions = GlassPrescription.objects.filter(patient=patient)
    investigations = Investigation.objects.filter(patient=patient)
    consultations = Consultation.objects.filter(patient=patient)
    
    context = {
        'patient': patient,
        'notes': notes,
        'prescriptions': prescriptions,
        'investigations': investigations,
        'consultations': consultations,
    }
    return render(request, 'patient_detail.html', context)
