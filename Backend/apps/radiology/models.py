class RadiologyImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='radiology_images/')
    description = models.TextField()
    date_of_scan = models.DateTimeField()
  
