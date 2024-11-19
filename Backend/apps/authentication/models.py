from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient'), ('Receptionist', 'Receptionist'), ('Nurse', 'Nurse')]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='patient')
    # Additional fields for user profile, e.g., contact info, etc.
  
