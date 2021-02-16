from django.db import models
from user.models import UserModel

# Create your models here.
class answers(models.Model):
    answer = models.CharField(max_length=1000)


class questions(models.Model):
    question_name = models.CharField(max_length=500)
    asked_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    answer_ques = models.ManyToManyField(answers,blank=True)

    def __str__(self):
        return self.question_name
