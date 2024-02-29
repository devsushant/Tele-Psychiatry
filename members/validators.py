from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re

def validate_name(name):
    if not name:
        raise ValidationError("Name cannot be empty.")
    if any(char.isdigit() for char in name):
        raise ValidationError("Name should not contain numeric characters.")

def validate_password(password):
    if not password:
        raise ValidationError("Password cannot be empty.")
    # Ensure password is at least 8 characters long and contains at least one digit and one special character
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalnum() for char in password):
        raise ValidationError("Password should be at least 8 characters long and contain at least one digit and one special character.")

def validate_email_domain(email):
    if not email:
        raise ValidationError("Email cannot be empty.")
    if not email.endswith('@gmail.com'):
        raise ValidationError("Email should end with @gmail.com.")


    
