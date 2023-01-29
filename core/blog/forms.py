from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)



# class PostCreateForm(forms.Form):
#     title = forms.CharField(max_length=110)
#     image = forms.ImageField()
#     content = forms.Textarea()
#     status = forms.BooleanField(widget=forms.CheckboxInput())
