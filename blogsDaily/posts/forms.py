from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subject', 'category', 'url', 'author', 'descriptions', 'image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            #'category' : forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'descriptions' : forms.Textarea(attrs={'class':'form-control'}),
        }