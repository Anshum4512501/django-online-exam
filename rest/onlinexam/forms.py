from django.forms import Form
from django.db import models
from django.forms import ModelForm
from .models import Question,Choice
class QuestionForm(ModelForm):
    
   class Meta:
        model = Question
        fields = '__all__'


class ChoiceForm(ModelForm):
    
   class Meta:
        model = Choice
        fields = '__all__'


                