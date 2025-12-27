from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Applicant(models.Model):
    APPLICATION_TYPES=[
        ("undergraduate","Undergraduate"),
        ("postgraduate", "Postgraduate"),
        ("sandwich", "Sandwich")
    ]
    ADMISSION_STATUSES = [
        ("pending", "Pending"),
        ("rejected", "Rejected"),
        ("admitted", "Admitted")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # form details
    application_type = models.CharField(max_length=20, choices=APPLICATION_TYPES)
    personal_detail_completed = models.BooleanField(default=False)
    history_completed = models.BooleanField(default=False)
    choices_completed = models.BooleanField(default=False)
    summary_completed = models.BooleanField(default=False)
    emergency_contact_completed = models.BooleanField(default=False)
    application_status = models.BooleanField(default=False)
    admission_status = models.CharField(max_length=25, choices=ADMISSION_STATUSES)
    

    def __str__(self):
        return self.user.first_name
    
    
class PersonalDetails(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="applicant_details", on_delete=models.CASCADE)
    gender = models.CharField()
    marital_status = models.CharField()
    date_of_birth = models.DateField()
    nationality = models.CharField()
    secondary_email = models.EmailField()
    religion = models.CharField()
    postal_address = models.CharField()
    postal_country = models.CharField()
    postal_region = models.CharField()
    postal_town = models.CharField()


class History(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="applicant_records", on_delete=models.CASCADE)
    academic_history = models.JSONField()
    work_experience = models.JSONField()


class Choices(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="applicant_choices", on_delete=models.CASCADE)
    first_choice = models.CharField()
    second_choice = models.CharField()
    third_choice = models.CharField()
    remarks = models.TextField()


class ApplicationUploads(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="applicant_upload", on_delete=models.CASCADE)
    certificates = models.JSONField()
    id_card = models.JSONField()


class Vouchers(models.Model):
    serial_number = models.CharField(max_length=256)
    pin = models.CharField(max_length=8)
    valid_status = models.BooleanField(default=True)
    



