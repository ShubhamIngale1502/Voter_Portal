from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


def cheack(value):
    if not value.isalpha():
        raise ValidationError("Only alphabets are allowed")
    if len(value) < 2:
        raise ValidationError("First name should contain at least 2 characters.")

class Voter(models.Model):
    Gender=[('Male','Male'),('Female','Female'),('Other','Other')]
    voter_id = models.CharField(max_length=10, unique=True, editable=False,auto_created=True)
    first_name = models.CharField(max_length=45,validators=[cheack])
    last_name = models.CharField(max_length=45,validators=[cheack])
    gender = models.CharField(max_length=40, choices=Gender)
    address = models.TextField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pincode = models.CharField(max_length=6,
        validators=[
            RegexValidator(r'^\d{6}$', "Pincode must have exactly 6 digits.")
        ])
    date_of_birth = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.voter_id:
            
            import random
            import string
            self.voter_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super(Voter, self).save(*args, **kwargs)

    def clean(self):
        super(Voter, self).clean()
        if not self.date_of_birth:
            raise ValidationError("Date of birth must be provided.")
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        if age < 18:
            raise ValidationError("Age must be 18 or above.")
    contact = PhoneNumberField(region='IN')
    

    

