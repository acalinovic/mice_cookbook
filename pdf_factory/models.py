from django.db import models


# Create your models here.
from django.utils.timezone import now


class PDFFile(models.Model):
    name = models.TextField(max_length=128, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=False)

