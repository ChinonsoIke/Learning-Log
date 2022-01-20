from dataclasses import field
from pyexpat import model
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields= ['text']
        labels= {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model= Entry
        fields= ['body']
        labels= {'body': ''}
        widgets= {'body': forms.Textarea(attrs={'cols':80})}