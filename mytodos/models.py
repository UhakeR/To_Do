from django.db import models
from django.urls import reverse

class ToDo(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    done = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.title