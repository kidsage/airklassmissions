from django.db import models
from contentshub.models import Klass
from accounts.models import User

class Question(models.Model):
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='question_klass')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_writer')
    content = models.TextField()

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_writer')
    content = models.TextField()

    def __str__(self):
        return self.content