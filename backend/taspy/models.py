from django.db import models

from datetime import datetime

class Task(models.Model):
    name = models.CharField(max_length=255)
    expiration_dm = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    _OPEN = 'OP'
    _IN_PROGRESS = 'IN'
    _CLOSED = 'CL'
    STATUS_CHOICES = [
        (_OPEN, 'OPEN'),
        (_IN_PROGRESS, 'IN_PROGRESS'),
        (_CLOSED, 'CLOSED')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=_OPEN,
    )
