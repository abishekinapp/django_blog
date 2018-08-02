from django import forms
from home.models import Post



class HomeForm(forms.ModelForm):
    title= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Write a Title...'}))
    post=forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Write a Post...'}))
    class Meta:
        model = Post
        fields = ('title','post',)