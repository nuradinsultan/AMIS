class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    date_prescribed = models.DateTimeField()
