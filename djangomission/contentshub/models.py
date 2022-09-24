from django.db import models
from accounts.models import Master

class Klass(models.Model):
    writer = models.ForeignKey(Master, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)