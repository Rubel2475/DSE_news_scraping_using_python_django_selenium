from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import userInput


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user




 
class inputForm(forms.ModelForm):
  class Meta:
    model = userInput
    fields = ["trading_code",]
    #fields = ["username", "trading_code",]
    #labels = {'username': "username", "Trading_Code ": "Enter company's trading code",}
    
    
# class inputForm(forms.Form):
# 	#username = forms.CharField(label='username')
# 	trading_code = forms.CharField(label='trading_code')


class contact_form(forms.Form):
    full_name = forms.CharField(label='full_name')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='message')
    
    

    

