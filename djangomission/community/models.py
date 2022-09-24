from django.db import models
from contentshub.models import Klass
from accounts.models import User

class Comment(models.Model):
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='question')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    contents = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    created_at = models.DateTimeField(auto_now_add=True)