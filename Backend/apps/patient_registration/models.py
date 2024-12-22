from django import forms

class PatientForm(forms.Form):
    identifier = forms.CharField(label='Identifier', max_length=100)
    family_name = forms.CharField(label='Family Name', max_length=100)
    given_name = forms.CharField(label='Given Name', max_length=100)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    birth_date = forms.DateField(label='Birth Date')
    phone = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email Address')
    address = forms.CharField(label='Address', max_length=255)
