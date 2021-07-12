from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class myForm(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    img = forms.ImageField()
    time = forms.DateTimeField()
    name = forms.CharField()
