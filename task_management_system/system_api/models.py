from django.db import models


class Task(models.Model):
    STATUS = [
        ('in the queue', 'в очереди'),
        ('running', 'выполняется'),
        ('completed', 'завершена'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUS, default='in the queue', max_length=150)
    data_created = models.DateTimeField(auto_now_add=True)
