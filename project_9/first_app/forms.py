from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields = '__all__'
        #fields=['name','roll']
        #exclude=['roll']   
        labels={
            'name':"Student_Name",
            'roll':'Student_roll'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn-primary'}),
            #'roll':forms.PasswordInput()
        }
        help_texts ={
            'name':"Write your full name"
        }
        error_messages = {
            'name': {
                'required': 'Your name is required.'
            }
        }