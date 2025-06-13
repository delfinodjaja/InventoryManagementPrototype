from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import patient_log
from django.utils import timezone

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class PatientLogForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = patient_log
        fields = ['name', 'type', 'breed', 'category', 'date', 'doctor']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date <= timezone.now():
            raise forms.ValidationError("Date must be in the future.")
        return date