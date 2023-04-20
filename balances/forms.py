from django import forms
from .models import Balance

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ('title', 'select1_content', 'select2_content', 'image_1', 'image_2',)