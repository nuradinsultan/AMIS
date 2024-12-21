# models.py

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PatientNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.patient.name}"


class GlassPrescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.TextField()
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.name}"


class Investigation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    result = models.TextField()
    test_date = models.DateTimeField()

    def __str__(self):
        return f"Investigation for {self.patient.name}"


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=200)
    consultation_details = models.TextField()
    consultation_date = models.DateTimeField()

    def __str__(self):
        return f"Consultation with {self.patient.name}"


class Procedure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    procedure_name = models.CharField(max_length=200)
    procedure_date = models.DateTimeField()

    def __str__(self):
        return f"Procedure for {self.patient.name}"


class Physiotherapy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapy_details = models.TextField()
    start_date = models.DateTimeField()

    def __str__(self):
        return f"Physiotherapy for {self.patient.name}"


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    prescribed_date = models.DateTimeField()

    def __str__(self):
        return f"Medication for {self.patient.name}"


class VitalSigns(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=20)
    temperature = models.FloatField()
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"Vital signs for {self.patient.name}"


class Assignment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    assigned_by = models.CharField(max_length=200)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"Assignment for {self.patient.name}"


class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Admission for {self.patient.name}"


class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=200)
    report_content = models.TextField()
    generated_at = models.DateTimeField()

    def __str__(self):
        return f"Report for {self.patient.name}"
