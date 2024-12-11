from django.db import models
from django.core.exceptions import ValidationError 
import os

def validate_image_size(value):
    file_size = value.size
    limit = 2 * 1024 * 1024  # 2 MB par image 
    if file_size > limit:
        raise ValidationError("L'image dépasse la taille maximale autorisée (2 Mo).")
# Génération automatique du trigramme (exemple basique)
def save(self, *args, **kwargs):
        self.trigram = (self.first_name[:1] + self.last_name[:2]).lower()
        super(Trainee, self).save(*args, **kwargs)
def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Trainee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    company_logo = models.ImageField(upload_to='company_logos/', validators=[validate_image_size], null=True, blank=True)

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    birth_date = models.DateField()

class Recruiter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

