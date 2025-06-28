from django import forms
from .models import Participant

class RegistrationForm(forms.Form):
  email = forms.EmailField(
      label='Your Email',
      max_length=254,
      widget=forms.EmailInput(attrs={
          'placeholder': 'Enter your email',
          'class': 'form-control',
      })
  )
