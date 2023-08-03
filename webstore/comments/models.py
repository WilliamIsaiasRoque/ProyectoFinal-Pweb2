from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"

class EmailMessage(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender_email = models.EmailField()
    recipient_email = models.EmailField()