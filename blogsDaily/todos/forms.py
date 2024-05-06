from django import forms
from .models import todo


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ('title','subject','description', 'crux', 'user' )
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'crux' : forms.TextInput(attrs={'class':'form-control'}),
        }
