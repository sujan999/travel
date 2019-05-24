from django import forms
from .models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'slug', 'image', 'tag',
                  'photographer', 'date', 'content', 'draft']
