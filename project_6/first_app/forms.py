from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label="Full Name:",initial="Mahfuza",help_text="Total length must be 70 characters",
                           required=False, 
                           widget=forms.Textarea(attrs={'id': 'text_area',
                        'placeholder': 'Enter your name here', 'rows': 5, 'cols': 40}))
    file=forms.FileField()
    email = forms.EmailField(label="UserEmail")
    #age=forms.IntegerField()
    #weight=forms.FloatField()
    #balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'})) 
    Choices=[('S','small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
    meal=[('p','pepperoni'),('M',"Mashroom"),('B',"Beef")]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<10:
            raise forms.ValidationError("Enter a name with at least 10 characters")
        else:
            return valname
    def clean_email(self):
        valemail=self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("Your email must contain .com")
        return valemail

    # def clean(self):
    #     cleaned_data= super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
def len_checK(value):
    if len(value)<10:
         raise forms.ValidationError("Enter a value with at least 10 characters")
class StudentData(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        validators=[
            validators.MinLengthValidator(10,
             message="Enter a name with at least 10 characters")
             ]
             
        )
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[
            validators.EmailValidator
            ]
        )
    age = forms.IntegerField(
        validators=[
            validators.MaxValueValidator(35),
            validators.MinValueValidator(24)
        ]
    ) 
    file=forms.FileField(
        validators=[
            validators.FileExtensionValidator(allowed_extensions=
                                              [
                                                  'pdf','png'
                                              ])
        ]
    )  
    text=forms.CharField(
        widget=forms.TextInput,
        validators=[
             len_checK
        ]
    )

class passwordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput) 

    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['confirm_password']
        if(val_conpass!=val_pass):
            raise forms.ValidationError("password doenot match")
        
        
