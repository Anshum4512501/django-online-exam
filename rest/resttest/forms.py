from django import forms
from .models import Emplyoee
class EmplyoeeForm(forms.ModelForm):
    def clean_eage(self):
        age = self.cleaned_data['age']
        if age<10:
            raise forms.ValidationError("Age Should be greater than 10")
    class Meta:
        model = Emplyoee
        fields = '__all__'

