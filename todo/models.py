from django.conf import settings
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=256)
    memo = models.TextField(blank=True, null=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    completed = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
