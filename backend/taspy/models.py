from django.db import models

from datetime import datetime

class Task(models.Model):
    name = models.CharField(max_length=255)
    expiration_dm = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('OPEN', 'OPEN'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('CLOSED', 'CLOSED')
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='OPEN',
    )
