from django.db import models

# Create your models here.
from core.user.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, verbose_name='Remitente')
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE,verbose_name='Receptor')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.username} {self.recipient.username}'