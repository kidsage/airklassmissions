from django.db import models
from accounts.models import User, Master

class Klass(models.Model):
    writer = models.ForeignKey(Master, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)


class Comment(models.Model):
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='klass')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    contents = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    created_at = models.DateTimeField(auto_now_add=True)