from django import forms
from .models import Voter

Gender=[('Male','Male'),('Female','Female'),('Other','Other')]
class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = '__all__'
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light'
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light'
                }),
            'gender':forms.Select(choices='Gender',attrs={
                'class': 'form-control bg-dark text-light'
                 }),
            'address': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light',
                'rows': 3,
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'picode': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'date_of_birth':forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light'
            })
            
                                           
        }