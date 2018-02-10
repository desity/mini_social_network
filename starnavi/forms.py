from django.forms import ModelForm
from .models import User, Post
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)