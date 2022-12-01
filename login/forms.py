from django import forms
from login.models import login_1

class formulariocadastro(forms.ModelForm):
    class Meta:
        model = login_1
        fields = '__all__'
