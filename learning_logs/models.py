from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """class for user topics"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text= models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """entry associted with topics"""
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE)
    body= models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural= 'entries'

    def __str__(self):
        """return a string representation of the model"""
        return self.body[:50] + '...'