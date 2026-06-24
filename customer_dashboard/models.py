from django.db import models

from django.contrib.auth.models import User

class CustomerStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    PENDING = "PENDING", "Pending"
    BLOCKED = "BLOCKED", "Blocked"
    
class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"
    PREFER_NOT_TO_SAY = "PREFER_NOT_TO_SAY", "Prefer Not To Say"

class PersonalDetils(models.Model):
    user_details=models.OneToOneField(User, on_delete=models.CASCADE)
    cm_phone = models.CharField(unique=True, max_length=50)
    cm_gender = models.CharField(max_length=20, choices=Gender.choices)
    cm_dob = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='userprofile/')
    cm_status = models.CharField(max_length=20, choices=CustomerStatus.choices, default=CustomerStatus.PENDING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_details.username
    


