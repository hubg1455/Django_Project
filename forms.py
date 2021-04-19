from django import forms
from . models import employee


class Employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }


