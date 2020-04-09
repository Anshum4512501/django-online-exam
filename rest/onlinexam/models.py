from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('question-list')   
# args=[str(self.id)]
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    


class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    def get_absolute_url(self):
            from django.urls import reverse
            return reverse('question-detail')  