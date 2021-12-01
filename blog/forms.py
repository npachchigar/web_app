from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class EmailPostForm(forms.Form):
    name = forms.CharField(_('name'),
                           max_length=25)
    email = forms.EmailField(_('e-mail'))
    to = forms.EmailField(_('e-mail'))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)