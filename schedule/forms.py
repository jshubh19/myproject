from django import forms
from .models import Student
from django.forms import ModelForm

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        #fields = ['name', 'last_name', 'location', 'email', 'image', 'file']
        fields='__all__'

    #name=forms.CharField(required=True)
    #last_name=forms.CharField(required=True)
    #location=forms.CharField(required=True)
    #email=forms.EmailField(label='E_mail',required=True)
    #image=forms.ImageField(required=False)
    #file=forms.FileField(required=False)


    #class meta():
     #   model= Student
      #  fields=['name','last_name','location','email','image','file']




class UserForm(forms.Form):
    username=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)

