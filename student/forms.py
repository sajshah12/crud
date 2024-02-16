from django import forms
from.models import User
class Userregister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'forms_control'}),
            'email':forms.TextInput(attrs={'class':'forms_control'}),
            'password':forms.TextInput(attrs={'class':'forms_control'}),
     
            
     
           
        }
        
        