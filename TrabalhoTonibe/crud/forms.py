from django import forms
from .models import Banco


class addForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'

    
