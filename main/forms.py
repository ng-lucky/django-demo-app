from django import forms

class PostFormNew(forms.Form):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    photo_url = forms.CharField(max_length=2000)


class TestForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    message = forms.CharField(widget=forms.Textarea)
    