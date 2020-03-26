from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', max_length=100)

class LikedBool(forms.Form):
    likedBoolean = forms.BooleanField(initial=False)
    
