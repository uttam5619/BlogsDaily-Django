from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    #image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Post
        fields = ('title', 'subject', 'category', 'url', 'author', 'descriptions', 'image')
        
        
class CommentForm(forms.ModelForm):
    comment =forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'comment here...'}))
    class Meta:
        model = Comment
        fields = ('comment',)