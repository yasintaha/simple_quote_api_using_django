from django.db import models

# Create your models here.
class Quote_model(models.Model):
    quote = models.CharField(max_length=243)
    date = models.DateTimeField(auto_now_add=True)
    