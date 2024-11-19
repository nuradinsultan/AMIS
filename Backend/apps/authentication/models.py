from django.contrib.auth.models import AbstractUser

  class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('Receptionist', 'Receptionist'), ('nurse', 'Nurse'), ('patient', 'Patient')])
    last_login = models.DateTimeField(auto_now=True)
      # Additional fields for user profile, e.g., contact info, etc
