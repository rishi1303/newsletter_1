from django import forms
from first_app.models import UserSignUp
class UserForm(forms.ModelForm):
    class Meta():
        model = UserSignUp
        fields = ['email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email